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

        Ok(Self {
            source_dir,
            output_dir,
            layouts,
            includes,
            config,
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

    fn simple_replace(&self, template: &str, replacements: &HashMap<String, String>) -> String {
        let mut result = template.to_string();
        
        // Process includes first
        let include_re = Regex::new(r"\{%\s*include\s+(\S+?)\s*%\}").unwrap();
        loop {
            let mut found = false;
            if let Some(cap) = include_re.captures(&result.clone()) {
                let include_name = cap.get(1).unwrap().as_str().replace(".html", "");
                if let Some(include_content) = self.includes.get(&include_name) {
                    let processed = self.simple_replace(include_content, replacements);
                    result = result.replace(&cap[0], &processed);
                    found = true;
                }
            }
            if !found {
                break;
            }
        }
        
        // Process conditional blocks {% if %} ... {% endif %}
        let if_re = Regex::new(r"\{%\s*if\s+([^%]+?)\s*%\}(.*?)\{%\s*endif\s*%\}").unwrap();
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
        
        // Replace variables
        result = result.replace("{{ content }}", replacements.get("content").unwrap_or(&String::new()));
        result = result.replace("{{ page.title }}", replacements.get("page.title").unwrap_or(&String::new()));
        result = result.replace("{{ page.subtitle }}", replacements.get("page.subtitle").unwrap_or(&String::new()));
        result = result.replace("{{ page.date | date_to_string }}", replacements.get("page.date").unwrap_or(&String::new()));
        result = result.replace("{{ page.url }}", replacements.get("page.url").unwrap_or(&String::new()));
        result = result.replace("{{ page.image }}", replacements.get("page.image").unwrap_or(&String::new()));
        result = result.replace("{{ page.picture }}", replacements.get("page.picture").unwrap_or(&String::new()));
        result = result.replace("{{ page.description }}", replacements.get("page.description").unwrap_or(&String::new()));
        result = result.replace("{{ page.name }}", replacements.get("page.name").unwrap_or(&String::new()));
        result = result.replace("{{ page.short }}", replacements.get("page.short").unwrap_or(&String::new()));
        result = result.replace("{{ page.layout }}", replacements.get("page.layout").unwrap_or(&String::new()));
        
        // Replace site variables
        result = result.replace("{{ site.name }}", &self.config.name);
        result = result.replace("{{ site.url }}", &self.config.url);
        result = result.replace("{{ site.twitter }}", &self.config.twitter);
        
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

    fn render_page(&self, page: &Page, _all_pages: &[Page]) -> Result<String> {
        let html_content = self.markdown_to_html(&page.content);
        
        let mut replacements = HashMap::new();
        replacements.insert("content".to_string(), html_content.clone());
        
        if let Some(title) = &page.frontmatter.title {
            replacements.insert("page.title".to_string(), title.clone());
        }
        
        if let Some(subtitle) = &page.frontmatter.subtitle {
            replacements.insert("page.subtitle".to_string(), subtitle.clone());
        }
        
        if let Some(date) = &page.frontmatter.date {
            replacements.insert("page.date".to_string(), date.clone());
        }
        
        if let Some(description) = &page.frontmatter.description {
            replacements.insert("page.description".to_string(), description.clone());
        }
        
        if let Some(image) = &page.frontmatter.image {
            replacements.insert("page.image".to_string(), image.clone());
        }
        
        if let Some(picture) = &page.frontmatter.picture {
            replacements.insert("page.picture".to_string(), picture.clone());
        }
        
        if let Some(short) = &page.frontmatter.short {
            replacements.insert("page.short".to_string(), short.clone());
        }
        
        // Determine page name for conditional logic
        let page_name = if page.output_path == "index.html" {
            "index.md"
        } else {
            ""
        };
        replacements.insert("page.name".to_string(), page_name.to_string());
        
        let url = format!("/{}", page.output_path);
        replacements.insert("page.url".to_string(), url);
        
        let layout = page.frontmatter.layout.as_deref().unwrap_or("page");
        replacements.insert("page.layout".to_string(), layout.to_string());
        
        if let Some(layout_template) = self.layouts.get(layout) {
            let rendered = self.simple_replace(layout_template, &replacements);
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
