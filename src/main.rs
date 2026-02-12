use anyhow::{Context, Result};
use pulldown_cmark::{html, Options, Parser};
use rayon::prelude::*;
use regex::Regex;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs;
use std::path::PathBuf;
use walkdir::WalkDir;

#[derive(Debug, Deserialize, Serialize, Clone)]
struct PageFrontMatter {
    title: Option<String>,
    layout: Option<String>,
    description: Option<String>,
    subtitle: Option<String>,
    image: Option<String>,
    picture: Option<String>,
    cover: Option<String>,
    date: Option<String>,
    authors: Option<Vec<String>>,
    tags: Option<Vec<String>>,
    short: Option<String>,
    twitter: Option<String>,
    github: Option<String>,
    linkedin: Option<String>,
    math: Option<bool>,
    charts: Option<bool>,
    #[serde(flatten)]
    extra: HashMap<String, serde_yaml::Value>,
}

#[derive(Debug)]
struct Page {
    path: PathBuf,
    relative_path: String,
    frontmatter: PageFrontMatter,
    content: String,
    output_path: String,
}

struct SiteGenerator {
    source_dir: PathBuf,
    output_dir: PathBuf,
    layouts: HashMap<String, String>,
    includes: HashMap<String, String>,
    config: SiteConfig,
    data_files: HashMap<String, serde_yaml::Value>,
}

#[derive(Debug, Deserialize, Serialize, Clone)]
struct SiteConfig {
    url: String,
    name: String,
    twitter: String,
    permalink: Option<String>,
    #[serde(default)]
    collections: HashMap<String, CollectionConfig>,
    #[serde(default)]
    exclude: Vec<String>,
}

#[derive(Debug, Deserialize, Serialize, Clone)]
struct CollectionConfig {
    output: bool,
    permalink: Option<String>,
}

impl SiteGenerator {
    fn new(source_dir: PathBuf) -> Result<Self> {
        let output_dir = source_dir.join("_site");
        
        // Load config
        let config_path = source_dir.join("_config.yml");
        let config_content = fs::read_to_string(&config_path)
            .context("Failed to read _config.yml")?;
        let config: SiteConfig = serde_yaml::from_str(&config_content)
            .context("Failed to parse _config.yml")?;

        // Load layouts
        let mut layouts = HashMap::new();
        for entry in WalkDir::new(source_dir.join("_layouts"))
            .into_iter()
            .filter_map(|e| e.ok())
            .filter(|e| e.path().extension().map_or(false, |ext| ext == "html"))
        {
            let path = entry.path();
            let name = path.file_stem().unwrap().to_str().unwrap().to_string();
            let content = fs::read_to_string(path)?;
            layouts.insert(name, content);
        }

        // Load includes
        let mut includes = HashMap::new();
        for entry in WalkDir::new(source_dir.join("_includes"))
            .into_iter()
            .filter_map(|e| e.ok())
            .filter(|e| e.path().extension().map_or(false, |ext| ext == "html"))
        {
            let path = entry.path();
            let name = path.file_stem().unwrap().to_str().unwrap().to_string();
            let content = fs::read_to_string(path)?;
            includes.insert(name, content);
        }

        // Load data files from _data/
        let mut data_files = HashMap::new();
        let data_dir = source_dir.join("_data");
        if data_dir.exists() {
            for entry in WalkDir::new(&data_dir)
                .into_iter()
                .filter_map(|e| e.ok())
                .filter(|e| {
                    e.path().extension().map_or(false, |ext| {
                        ext == "yml" || ext == "yaml" || ext == "json"
                    })
                })
            {
                let path = entry.path();
                let name = path.file_stem().unwrap().to_str().unwrap().to_string();
                let content = fs::read_to_string(path)?;
                
                let data: serde_yaml::Value = if path.extension().unwrap() == "json" {
                    serde_json::from_str(&content)
                        .with_context(|| format!("Failed to parse JSON data file: {}", name))?
                } else {
                    serde_yaml::from_str(&content)
                        .with_context(|| format!("Failed to parse YAML data file: {}", name))?
                };
                
                data_files.insert(name, data);
            }
        }

        Ok(Self {
            source_dir,
            output_dir,
            layouts,
            includes,
            config,
            data_files,
        })
    }

    fn parse_frontmatter(&self, content: &str, path: &str) -> Result<(PageFrontMatter, String)> {
        // Use DOTALL flag to match across newlines
        let re = Regex::new(r"(?s)^---\s*\n(.*?)\n---\s*\n(.*)$").unwrap();
        
        if let Some(caps) = re.captures(content) {
            let yaml = caps.get(1).unwrap().as_str();
            let body = caps.get(2).unwrap().as_str();
            
            let frontmatter: PageFrontMatter = serde_yaml::from_str(yaml)
                .with_context(|| format!("Failed to parse frontmatter in {}", path))?;
            
            Ok((frontmatter, body.to_string()))
        } else {
            Ok((
                PageFrontMatter {
                    title: None,
                    layout: Some("page".to_string()),
                    description: None,
                    subtitle: None,
                    image: None,
                    picture: None,
                    cover: None,
                    date: None,
                    authors: None,
                    tags: None,
                    short: None,
                    twitter: None,
                    github: None,
                    linkedin: None,
                    math: None,
                    charts: None,
                    extra: HashMap::new(),
                },
                content.to_string(),
            ))
        }
    }

    fn markdown_to_html(&self, markdown: &str) -> String {
        let mut options = Options::empty();
        options.insert(Options::ENABLE_TABLES);
        options.insert(Options::ENABLE_FOOTNOTES);
        options.insert(Options::ENABLE_STRIKETHROUGH);
        options.insert(Options::ENABLE_TASKLISTS);
        options.insert(Options::ENABLE_SMART_PUNCTUATION);

        let parser = Parser::new_ext(markdown, options);
        let mut html_output = String::new();
        html::push_html(&mut html_output, parser);
        html_output
    }

    fn collect_pages(&self) -> Result<Vec<Page>> {
        let mut pages = Vec::new();
        let mut errors = Vec::new();

        // Process regular markdown files in root
        for entry in fs::read_dir(&self.source_dir)? {
            let entry = entry?;
            let path = entry.path();
            
            if path.is_file() && path.extension().map_or(false, |ext| ext == "md") {
                let relative_path = path.strip_prefix(&self.source_dir)
                    .unwrap()
                    .to_str()
                    .unwrap()
                    .to_string();
                
                let content = fs::read_to_string(&path)?;
                let (frontmatter, body) = match self.parse_frontmatter(&content, &relative_path) {
                    Ok(result) => result,
                    Err(e) => {
                        eprintln!("Warning: Skipping {}: {}", relative_path, e);
                        errors.push(relative_path.clone());
                        continue;
                    }
                };
                
                let file_stem = path.file_stem().unwrap().to_str().unwrap();
                let output_path = if file_stem == "index" {
                    "index.html".to_string()
                } else {
                    format!("{}.html", file_stem)
                };
                
                pages.push(Page {
                    path: path.clone(),
                    relative_path,
                    frontmatter,
                    content: body,
                    output_path,
                });
            }
        }

        // Process collections
        for (collection_name, collection_config) in &self.config.collections {
            if !collection_config.output {
                continue;
            }

            let collection_dir = self.source_dir.join(format!("_{}", collection_name));
            if !collection_dir.exists() {
                continue;
            }

            for entry in WalkDir::new(&collection_dir)
                .into_iter()
                .filter_map(|e| e.ok())
                .filter(|e| e.path().extension().map_or(false, |ext| ext == "md"))
                .filter(|e| !e.file_name().to_str().unwrap().starts_with("_template"))
            {
                let path = entry.path();
                let content = fs::read_to_string(path)?;
                
                let relative_path = path.strip_prefix(&self.source_dir)
                    .unwrap()
                    .to_str()
                    .unwrap()
                    .to_string();
                
                let (frontmatter, body) = match self.parse_frontmatter(&content, &relative_path) {
                    Ok(result) => result,
                    Err(e) => {
                        eprintln!("Warning: Skipping {}: {}", relative_path, e);
                        errors.push(relative_path.clone());
                        continue;
                    }
                };
                
                let file_stem = path.file_stem().unwrap().to_str().unwrap();
                let output_path = format!("{}/{}.html", collection_name, file_stem);
                
                pages.push(Page {
                    path: path.to_path_buf(),
                    relative_path,
                    frontmatter,
                    content: body,
                    output_path,
                });
            }
        }

        // Process blog posts
        let posts_dir = self.source_dir.join("_posts");
        if posts_dir.exists() {
            for entry in WalkDir::new(&posts_dir)
                .into_iter()
                .filter_map(|e| e.ok())
                .filter(|e| e.path().extension().map_or(false, |ext| ext == "md"))
                .filter(|e| !e.file_name().to_str().unwrap().starts_with("_template"))
            {
                let path = entry.path();
                let content = fs::read_to_string(path)?;
                
                let relative_path = path.strip_prefix(&self.source_dir)
                    .unwrap()
                    .to_str()
                    .unwrap()
                    .to_string();
                
                let (frontmatter, body) = match self.parse_frontmatter(&content, &relative_path) {
                    Ok(result) => result,
                    Err(e) => {
                        eprintln!("Warning: Skipping {}: {}", relative_path, e);
                        errors.push(relative_path.clone());
                        continue;
                    }
                };
                
                let file_name = path.file_stem().unwrap().to_str().unwrap();
                // Extract title from filename (format: YYYY-MM-DD-title)
                let title_part = if file_name.len() > 11 && file_name.chars().take(10).all(|c| c.is_numeric() || c == '-') {
                    &file_name[11..]
                } else {
                    file_name
                };
                
                let output_path = format!("blog/{}.html", title_part);
                
                pages.push(Page {
                    path: path.to_path_buf(),
                    relative_path,
                    frontmatter,
                    content: body,
                    output_path,
                });
            }
        }

        if !errors.is_empty() {
            eprintln!("\nWarning: {} files were skipped due to errors", errors.len());
        }

        Ok(pages)
    }

    fn apply_filters<'a>(&self, mut pages: Vec<&'a Page>, filters: &[&str]) -> Vec<&'a Page> {
        for filter in filters {
            let filter = filter.trim();
            
            if filter.starts_with("sort:") {
                // Extract field name from sort: 'field' or sort: "field"
                let field = filter[5..].trim().trim_matches(|c| c == '\'' || c == '"');
                
                pages.sort_by(|a, b| {
                    match field {
                        "episode" => {
                            // Try to extract episode number from frontmatter or filename
                            let a_ep = a.frontmatter.extra.get("episode")
                                .and_then(|v| v.as_i64())
                                .unwrap_or(0);
                            let b_ep = b.frontmatter.extra.get("episode")
                                .and_then(|v| v.as_i64())
                                .unwrap_or(0);
                            a_ep.cmp(&b_ep)
                        }
                        "season" => {
                            let a_season = a.frontmatter.extra.get("season")
                                .and_then(|v| v.as_i64())
                                .unwrap_or(0);
                            let b_season = b.frontmatter.extra.get("season")
                                .and_then(|v| v.as_i64())
                                .unwrap_or(0);
                            a_season.cmp(&b_season)
                        }
                        "date" => {
                            a.frontmatter.date.as_ref().cmp(&b.frontmatter.date.as_ref())
                        }
                        "title" => {
                            a.frontmatter.title.as_ref().cmp(&b.frontmatter.title.as_ref())
                        }
                        _ => std::cmp::Ordering::Equal,
                    }
                });
            } else if filter == "reverse" {
                pages.reverse();
            }
        }
        
        pages
    }
    
    fn apply_data_filters(&self, mut items: Vec<serde_yaml::Value>, filters: &[&str]) -> Vec<serde_yaml::Value> {
        for filter in filters {
            let filter = filter.trim();
            
            if filter.starts_with("sort:") {
                let field = filter[5..].trim().trim_matches(|c| c == '\'' || c == '"');
                
                items.sort_by(|a, b| {
                    let a_val = a.as_mapping().and_then(|m| {
                        m.get(&serde_yaml::Value::String(field.to_string()))
                    });
                    let b_val = b.as_mapping().and_then(|m| {
                        m.get(&serde_yaml::Value::String(field.to_string()))
                    });
                    
                    match (a_val, b_val) {
                        (Some(a), Some(b)) => {
                            // Try to compare as strings
                            match (a.as_str(), b.as_str()) {
                                (Some(a_str), Some(b_str)) => a_str.cmp(b_str),
                                _ => std::cmp::Ordering::Equal,
                            }
                        }
                        _ => std::cmp::Ordering::Equal,
                    }
                });
            } else if filter == "reverse" {
                items.reverse();
            } else if filter.starts_with("where_exp:") {
                // Simple where_exp implementation
                // Format: where_exp: "item", "item.field != value" or "item.field > site.time"
                // For now, we'll filter based on common patterns
                
                // Extract the condition - it's complex, so we'll handle specific cases
                let condition_part = filter[10..].trim();
                
                // Handle draft filter: event.draft != true
                if condition_part.contains("draft != true") {
                    items.retain(|item| {
                        if let Some(mapping) = item.as_mapping() {
                            let draft = mapping.get(&serde_yaml::Value::String("draft".to_string()))
                                .and_then(|v| v.as_bool())
                                .unwrap_or(false);
                            !draft
                        } else {
                            true
                        }
                    });
                }
                
                // Handle time filter: event.time > site.time (future events)
                if condition_part.contains("time > site.time") {
                    use chrono::Utc;
                    let now = Utc::now();
                    
                    items.retain(|item| {
                        if let Some(mapping) = item.as_mapping() {
                            if let Some(time_val) = mapping.get(&serde_yaml::Value::String("time".to_string())) {
                                if let Some(time_str) = time_val.as_str() {
                                    // Try to parse the time
                                    if let Ok(event_time) = chrono::DateTime::parse_from_str(time_str, "%Y-%m-%d %H:%M:%S") {
                                        return event_time.with_timezone(&Utc) > now;
                                    }
                                }
                            }
                        }
                        false
                    });
                }
                
                // Handle end time filter: book.end > site.time
                if condition_part.contains("end > site.time") {
                    use chrono::Utc;
                    let now = Utc::now();
                    
                    items.retain(|item| {
                        if let Some(mapping) = item.as_mapping() {
                            if let Some(end_val) = mapping.get(&serde_yaml::Value::String("end".to_string())) {
                                if let Some(end_str) = end_val.as_str() {
                                    if let Ok(end_time) = chrono::DateTime::parse_from_str(end_str, "%Y-%m-%d %H:%M:%S") {
                                        return end_time.with_timezone(&Utc) > now;
                                    }
                                }
                            }
                        }
                        false
                    });
                }
            }
        }
        
        items
    }

    fn process_template(&self, template: &str, replacements: &HashMap<String, String>, all_pages: &[Page]) -> String {
        let mut result = template.to_string();
        let mut assigned_variables: HashMap<String, Vec<&Page>> = HashMap::new();
        let mut assigned_data: HashMap<String, Vec<serde_yaml::Value>> = HashMap::new();
        
        // Process assign statements {% assign var = source | filters %}
        let assign_re = Regex::new(r"(?s)\{%\s*assign\s+(\w+)\s*=\s*(.*?)%\}").unwrap();
        let assigns: Vec<_> = assign_re.captures_iter(&result).map(|cap| {
            let var_name = cap.get(1).unwrap().as_str().to_string();
            let expression = cap.get(2).unwrap().as_str().trim().to_string();
            let full_match = cap.get(0).unwrap().as_str().to_string();
            (var_name, expression, full_match)
        }).collect();
        
        for (var_name, expression, full_match) in assigns {
            // Parse the expression to get source and filters
            let parts: Vec<&str> = expression.split('|').map(|s| s.trim()).collect();
            let source = parts[0];
            let filters = &parts[1..];
            
            // Get the source collection or data
            if source.starts_with("site.data.") {
                let data_name = &source[10..];
                if let Some(data) = self.data_files.get(data_name) {
                    if let Some(data_array) = data.as_sequence() {
                        let mut items: Vec<serde_yaml::Value> = data_array.iter().cloned().collect();
                        
                        // Apply filters
                        items = self.apply_data_filters(items, filters);
                        
                        assigned_data.insert(var_name.clone(), items);
                    }
                }
            } else if source.starts_with("site.") {
                let collection_name = &source[5..];
                let mut collection_pages: Vec<&Page> = if collection_name == "posts" {
                    all_pages.iter().filter(|p| p.relative_path.starts_with("_posts/")).collect()
                } else {
                    all_pages.iter().filter(|p| p.relative_path.starts_with(&format!("_{}/", collection_name))).collect()
                };
                
                // Apply filters
                collection_pages = self.apply_filters(collection_pages, filters);
                
                assigned_variables.insert(var_name.clone(), collection_pages);
            }
            
            // Remove the assign statement
            result = result.replace(&full_match, "");
        }
        
        // After removing all assigns, normalize whitespace to prevent code blocks
        // Remove lines that are now empty or just whitespace after assign removal
        let lines: Vec<&str> = result.lines().collect();
        let mut normalized_lines = Vec::new();
        let mut in_html_block = false;
        
        for line in lines {
            // Check if this line starts an HTML block
            if line.trim_start().starts_with('<') && !line.trim_start().starts_with("</") {
                in_html_block = true;
            }
            
            // For HTML blocks, remove leading whitespace to prevent code block interpretation
            if in_html_block && line.trim().starts_with('<') {
                normalized_lines.push(line.trim_start());
            } else if !line.trim().is_empty() || !in_html_block {
                normalized_lines.push(line);
            }
            
            // Check if this line closes the HTML block
            if line.trim().starts_with("</div>") || line.trim() == "</ul>" || line.trim() == "</p>" {
                // Check if we're closing the outermost block
                let open_count = result[..result.find(line).unwrap_or(0)].matches("<div").count();
                let close_count = result[..result.find(line).unwrap_or(0)].matches("</div>").count();
                if open_count <= close_count + 1 {
                    in_html_block = false;
                }
            }
        }
        result = normalized_lines.join("\n");
        
        // Process for loops {% for item in collection %} ... {% endfor %}
        // Updated regex to handle both direct site.collection and assigned variables
        let for_re = Regex::new(r"(?s)\{%\s*for\s+(\w+)\s+in\s+([^\s%]+)(?:\s+limit:\s*(\d+))?\s*%\}(.*?)\{%\s*endfor\s*%\}").unwrap();
        while let Some(cap) = for_re.captures(&result.clone()) {
            let item_name = cap.get(1).unwrap().as_str();
            let collection_path = cap.get(2).unwrap().as_str();
            let limit = cap.get(3).and_then(|m| m.as_str().parse::<usize>().ok());
            let loop_body = cap.get(4).unwrap().as_str();
            

            
            let mut loop_output = String::new();
            
            // Check if this is an assigned variable
            if let Some(assigned_pages) = assigned_variables.get(collection_path) {
                // Use assigned variable (already filtered/sorted)
                let items: Vec<_> = if let Some(limit_val) = limit {
                    assigned_pages.iter().take(limit_val).collect()
                } else {
                    assigned_pages.iter().collect()
                };
                
                for (idx, page) in items.iter().enumerate() {
                    let mut item_replacements = replacements.clone();
                    
                    if let Some(title) = &page.frontmatter.title {
                        item_replacements.insert(format!("{}.title", item_name), title.clone());
                    }
                    if let Some(authors) = &page.frontmatter.authors {
                        item_replacements.insert(format!("{}.authors", item_name), authors.join(", "));
                    }
                    
                    let id = page.output_path.trim_end_matches(".html");
                    item_replacements.insert(format!("{}.id", item_name), id.to_string());
                    item_replacements.insert("forloop.last".to_string(), (idx == items.len() - 1).to_string());
                    
                    let processed_body = self.process_simple_vars(&loop_body, &item_replacements);
                    loop_output.push_str(&processed_body);
                }
            } else if let Some(assigned_data_items) = assigned_data.get(collection_path) {
                // Use assigned data variable
                let items: Vec<_> = if let Some(limit_val) = limit {
                    assigned_data_items.iter().take(limit_val).collect()
                } else {
                    assigned_data_items.iter().collect()
                };
                
                for (idx, data_item) in items.iter().enumerate() {
                    let mut item_replacements = replacements.clone();
                    
                    if let Some(obj) = data_item.as_mapping() {
                        for (key, value) in obj {
                            if let Some(key_str) = key.as_str() {
                                let value_str = match value {
                                    serde_yaml::Value::String(s) => s.clone(),
                                    serde_yaml::Value::Number(n) => n.to_string(),
                                    serde_yaml::Value::Bool(b) => b.to_string(),
                                    _ => String::new(),
                                };
                                item_replacements.insert(format!("{}.{}", item_name, key_str), value_str);
                            }
                        }
                    }
                    
                    item_replacements.insert("forloop.last".to_string(), (idx == items.len() - 1).to_string());
                    
                    let processed_body = self.process_simple_vars(&loop_body, &item_replacements);
                    loop_output.push_str(&processed_body);
                }
            } else if collection_path.starts_with("site.") && !collection_path.starts_with("site.data.") {
                let collection_name = &collection_path[5..]; // Remove "site."
                
                // Get pages from collection
                let mut collection_pages: Vec<&Page> = if collection_name == "posts" {
                    all_pages
                        .iter()
                        .filter(|p| p.relative_path.starts_with("_posts/"))
                        .collect()
                } else {
                    all_pages
                        .iter()
                        .filter(|p| p.relative_path.starts_with(&format!("_{}/", collection_name)))
                        .collect()
                };
                
                // Apply limit if specified
                if let Some(limit_val) = limit {
                    collection_pages.truncate(limit_val);
                }
                
                // Generate output for each item
                for (idx, page) in collection_pages.iter().enumerate() {
                    let mut item_replacements = replacements.clone();
                    
                    // Add loop variables
                    if let Some(title) = &page.frontmatter.title {
                        item_replacements.insert(format!("{}.title", item_name), title.clone());
                    }
                    if let Some(authors) = &page.frontmatter.authors {
                        // For now, just join authors with comma
                        item_replacements.insert(format!("{}.authors", item_name), authors.join(", "));
                    }
                    
                    // Add page ID (output path without .html)
                    let id = page.output_path.trim_end_matches(".html");
                    item_replacements.insert(format!("{}.id", item_name), id.to_string());
                    
                    // Add forloop variables
                    item_replacements.insert("forloop.last".to_string(), (idx == collection_pages.len() - 1).to_string());
                    
                    // Process the loop body with item replacements
                    let processed_body = self.process_simple_vars(&loop_body, &item_replacements);
                    loop_output.push_str(&processed_body);
                }
            } else if collection_path.starts_with("site.data.") {
                // Handle data files like site.data.events
                let data_name = &collection_path[10..]; // Remove "site.data."
                
                if let Some(data) = self.data_files.get(data_name) {
                    if let Some(data_array) = data.as_sequence() {
                        let items: Vec<_> = if let Some(limit_val) = limit {
                            data_array.iter().take(limit_val).collect()
                        } else {
                            data_array.iter().collect()
                        };
                        
                        for (idx, data_item) in items.iter().enumerate() {
                            let mut item_replacements = replacements.clone();
                            
                            // Extract fields from data item
                            if let Some(obj) = data_item.as_mapping() {
                                for (key, value) in obj {
                                    if let Some(key_str) = key.as_str() {
                                        let value_str = match value {
                                            serde_yaml::Value::String(s) => s.clone(),
                                            serde_yaml::Value::Number(n) => n.to_string(),
                                            serde_yaml::Value::Bool(b) => b.to_string(),
                                            _ => String::new(),
                                        };
                                        item_replacements.insert(format!("{}.{}", item_name, key_str), value_str);
                                    }
                                }
                            }
                            
                            // Add forloop variables
                            item_replacements.insert("forloop.last".to_string(), (idx == items.len() - 1).to_string());
                            
                            // Process the loop body
                            let processed_body = self.process_simple_vars(&loop_body, &item_replacements);
                            loop_output.push_str(&processed_body);
                        }
                    }
                }
            }
            
            result = result.replace(&cap[0], &loop_output);
        }
        
        // Process includes
        let include_re = Regex::new(r"\{%\s*include\s+(\S+?)\s*%\}").unwrap();
        loop {
            let mut found = false;
            if let Some(cap) = include_re.captures(&result.clone()) {
                let include_name = cap.get(1).unwrap().as_str().replace(".html", "");
                if let Some(include_content) = self.includes.get(&include_name) {
                    let processed = self.process_template(include_content, replacements, all_pages);
                    result = result.replace(&cap[0], &processed);
                    found = true;
                }
            }
            if !found {
                break;
            }
        }
        
        // Process conditional blocks {% if %} ... {% endif %}
        let if_re = Regex::new(r"(?s)\{%\s*if\s+([^%]+?)\s*%\}(.*?)\{%\s*endif\s*%\}").unwrap();
        while let Some(cap) = if_re.captures(&result.clone()) {
            let condition = cap.get(1).unwrap().as_str().trim();
            let content = cap.get(2).unwrap().as_str();
            
            // Simple condition checking
            let should_include = if condition.starts_with("page.") {
                let key = condition.to_string();
                replacements.contains_key(&key) && !replacements.get(&key).unwrap().is_empty()
            } else {
                false
            };
            
            let replacement = if should_include {
                content.to_string()
            } else {
                String::new()
            };
            
            result = result.replace(&cap[0], &replacement);
        }
        
        // Process simple variable replacements
        result = self.process_simple_vars(&result, replacements);
        
        result
    }
    
    fn process_simple_vars(&self, template: &str, replacements: &HashMap<String, String>) -> String {
        let mut result = template.to_string();
        
        // Replace site variables first
        result = result.replace("{{ site.name }}", &self.config.name);
        result = result.replace("{{ site.url }}", &self.config.url);
        result = result.replace("{{ site.twitter }}", &self.config.twitter);
        
        // Replace all variables from replacements map
        // First pass: exact matches with spaces
        for (key, value) in replacements {
            let patterns = vec![
                format!("{{{{ {} }}}}", key),
                format!("{{{{  {}  }}}}", key),
            ];
            for pattern in patterns {
                result = result.replace(&pattern, value);
            }
        }
        
        // Handle default filter: {{ page.title | default: site.name }}
        let default_re = Regex::new(r"\{\{\s*([^|]+?)\s*\|\s*default:\s*([^}]+?)\s*\}\}").unwrap();
        for cap in default_re.captures_iter(&template) {
            let var = cap.get(1).unwrap().as_str().trim();
            let default = cap.get(2).unwrap().as_str().trim();
            
            let var_key = var.replace("page.", "page.");
            let value = if let Some(v) = replacements.get(&var_key) {
                if !v.is_empty() {
                    v.clone()
                } else if default.starts_with("site.") {
                    match default {
                        "site.name" => self.config.name.clone(),
                        _ => String::new(),
                    }
                } else {
                    default.to_string()
                }
            } else if default.starts_with("site.") {
                match default {
                    "site.name" => self.config.name.clone(),
                    _ => String::new(),
                }
            } else {
                default.to_string()
            };
            
            result = result.replace(&cap[0], &value);
        }
        
        // Remove any remaining liquid tags for now (simplified)
        let liquid_tag_re = Regex::new(r"\{%.*?%\}").unwrap();
        result = liquid_tag_re.replace_all(&result, "").to_string();
        
        // Remove any remaining variable placeholders
        let var_re = Regex::new(r"\{\{.*?\}\}").unwrap();
        result = var_re.replace_all(&result, "").to_string();
        
        result
    }

    fn render_page(&self, page: &Page, all_pages: &[Page]) -> Result<String> {
        // First, set up page variables for template processing
        let mut page_replacements = HashMap::new();
        
        if let Some(title) = &page.frontmatter.title {
            page_replacements.insert("page.title".to_string(), title.clone());
        }
        
        if let Some(subtitle) = &page.frontmatter.subtitle {
            page_replacements.insert("page.subtitle".to_string(), subtitle.clone());
        }
        
        if let Some(date) = &page.frontmatter.date {
            page_replacements.insert("page.date".to_string(), date.clone());
        }
        
        if let Some(description) = &page.frontmatter.description {
            page_replacements.insert("page.description".to_string(), description.clone());
        }
        
        if let Some(image) = &page.frontmatter.image {
            page_replacements.insert("page.image".to_string(), image.clone());
        }
        
        if let Some(picture) = &page.frontmatter.picture {
            page_replacements.insert("page.picture".to_string(), picture.clone());
        }
        
        if let Some(short) = &page.frontmatter.short {
            page_replacements.insert("page.short".to_string(), short.clone());
        }
        
        // Determine page name for conditional logic
        let page_name = if page.output_path == "index.html" {
            "index.md"
        } else {
            ""
        };
        page_replacements.insert("page.name".to_string(), page_name.to_string());
        
        let url = format!("/{}", page.output_path);
        page_replacements.insert("page.url".to_string(), url);
        
        let layout = page.frontmatter.layout.as_deref().unwrap_or("page");
        page_replacements.insert("page.layout".to_string(), layout.to_string());
        
        // Process Liquid templates in the page content BEFORE converting to HTML
        let processed_content = self.process_template(&page.content, &page_replacements, all_pages);
        
        // Now convert the processed content to HTML
        let html_content = self.markdown_to_html(&processed_content);
        
        // Add the HTML content to replacements for layout processing
        let mut replacements = page_replacements;
        replacements.insert("content".to_string(), html_content.clone());
        
        if let Some(layout_template) = self.layouts.get(layout) {
            let rendered = self.process_template(layout_template, &replacements, all_pages);
            Ok(rendered)
        } else {
            // No layout, just return the HTML content
            Ok(html_content)
        }
    }

    fn copy_assets(&self) -> Result<()> {
        // Copy assets directory
        let assets_src = self.source_dir.join("assets");
        if assets_src.exists() {
            let assets_dst = self.output_dir.join("assets");
            fs::create_dir_all(&assets_dst)?;
            
            for entry in WalkDir::new(&assets_src)
                .into_iter()
                .filter_map(|e| e.ok())
                .filter(|e| e.path().is_file())
            {
                let src_path = entry.path();
                let rel_path = src_path.strip_prefix(&assets_src).unwrap();
                let dst_path = assets_dst.join(rel_path);
                
                if let Some(parent) = dst_path.parent() {
                    fs::create_dir_all(parent)?;
                }
                
                fs::copy(src_path, dst_path)?;
            }
        }

        // Copy images directory
        let images_src = self.source_dir.join("images");
        if images_src.exists() {
            let images_dst = self.output_dir.join("images");
            fs::create_dir_all(&images_dst)?;
            
            for entry in WalkDir::new(&images_src)
                .into_iter()
                .filter_map(|e| e.ok())
                .filter(|e| e.path().is_file())
            {
                let src_path = entry.path();
                let rel_path = src_path.strip_prefix(&images_src).unwrap();
                let dst_path = images_dst.join(rel_path);
                
                if let Some(parent) = dst_path.parent() {
                    fs::create_dir_all(parent)?;
                }
                
                fs::copy(src_path, dst_path)?;
            }
        }

        // Copy other static files (favicon, robots.txt, etc.)
        let static_files = [
            "CNAME",
            "robots.txt",
            "sitemap.xml",
            "favicon.ico",
            "favicon-16x16.png",
            "favicon-32x32.png",
            "apple-touch-icon.png",
            "android-chrome-192x192.png",
            "android-chrome-512x512.png",
            "safari-pinned-tab.svg",
            "browserconfig.xml",
            "site.webmanifest",
            "mstile-150x150.png",
        ];

        for file in &static_files {
            let src = self.source_dir.join(file);
            if src.exists() {
                let dst = self.output_dir.join(file);
                fs::copy(&src, &dst)?;
            }
        }

        Ok(())
    }

    fn build(&self) -> Result<()> {
        println!("Building site...");
        
        // Clean output directory
        if self.output_dir.exists() {
            fs::remove_dir_all(&self.output_dir)?;
        }
        fs::create_dir_all(&self.output_dir)?;

        // Collect all pages
        println!("Collecting pages...");
        let pages = self.collect_pages()?;
        println!("Found {} pages", pages.len());

        // Render pages in parallel
        println!("Rendering pages...");
        let results: Vec<Result<(&Page, String)>> = pages
            .par_iter()
            .map(|page| {
                let html = self.render_page(page, &pages)?;
                Ok((page, html))
            })
            .collect();

        // Write rendered pages
        for result in results {
            let (page, html) = result?;
            let output_path = self.output_dir.join(&page.output_path);
            
            if let Some(parent) = output_path.parent() {
                fs::create_dir_all(parent)?;
            }
            
            fs::write(&output_path, html)?;
        }

        // Copy static assets
        println!("Copying assets...");
        self.copy_assets()?;

        println!("Build complete!");
        Ok(())
    }
}

fn main() -> Result<()> {
    let source_dir = std::env::current_dir()?;
    let generator = SiteGenerator::new(source_dir)?;
    
    let start = std::time::Instant::now();
    generator.build()?;
    let elapsed = start.elapsed();
    
    println!("Build took: {:.2?}", elapsed);
    
    Ok(())
}
