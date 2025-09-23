# Mailchimp Code Block Setup Guide

This guide shows you how to use the ML Zoomcamp newsletter template as a **Code Block** in Mailchimp's drag-and-drop email builder.

## Files

- `mailchimp-code-block.html` - Production code block with Mailchimp merge tags
- `mailchimp-code-block-demo.html` - Preview version with sample content

## How to Use in Mailchimp

### Step 1: Create a New Campaign
1. Go to **Campaigns** → **Create Campaign**
2. Choose **Email** → **Regular**
3. Select your audience
4. Choose **Design Email**

### Step 2: Add the Code Block
1. In the email designer, choose a **Basic** template or start **Blank**
2. From the content blocks on the right, drag a **Code** block into your layout
3. Click on the Code block to edit it

### Step 3: Paste the Template Code
1. Copy the entire contents of `mailchimp-code-block.html`
2. Paste it into the Code block editor
3. Click **Save & Close**

### Step 4: Set Up Merge Tags
Make sure these merge tags exist in your Mailchimp audience:

**Required Tags:**
- `FNAME` - First name
- `MODULE_NUMBER` - Current module (e.g., "3")
- `TOTAL_MODULES` - Total modules (e.g., "10") 
- `PROGRESS_PERCENTAGE` - Progress as number (e.g., "30")
- `MODULE_TOPIC` - Topic name (e.g., "Classification")

**Lesson Tags:**
- `LESSON_1_TITLE` through `LESSON_5_TITLE`
- `LESSON_1_URL` through `LESSON_5_URL`

**Content Tags:**
- `OUTCOME_1`, `OUTCOME_2`, `OUTCOME_3` - Learning outcomes
- `HOMEWORK_DESCRIPTION` - Assignment description
- `HOMEWORK_SUBMIT_URL` - Homework submission link
- `MODULE_START_URL` - Link to start the module

### Step 5: Test Your Email
1. Use Mailchimp's **Preview** feature
2. Send a **Test Email** to yourself
3. Check on mobile and desktop
4. Verify all links work correctly

## Key Features

✅ **Beautiful gradient header** with progress tracking
✅ **Course overview** with clickable lesson links  
✅ **Learning outcomes** with checkmarks
✅ **Assignment section** with clear call-to-action
✅ **Mobile responsive** design
✅ **Email client compatible** (works in Gmail, Outlook, Apple Mail)

## Design Highlights

- **Purple gradient header** matches modern course platforms
- **DataTalks Club green** (#2c573e) for branding
- **Clean lesson cards** with hover effects
- **Progress bar** showing completion
- **Clear typography** optimized for readability

## Customization Tips

### Colors
You can easily change the colors by modifying these values:
- Header gradient: `#6366f1` to `#8b5cf6` 
- Brand green: `#2c573e`
- Success green: `#28a745`
- Background: `#f8f9fa`

### Content Sections
The template includes these main sections:
1. **Header** with progress
2. **Greeting** with personalization
3. **Course overview** with lessons
4. **Learning outcomes**
5. **Homework assignment**
6. **Call-to-action button**
7. **Footer message**

### Mobile Optimization
The template includes CSS media queries that:
- Reduce font sizes on mobile
- Adjust padding for smaller screens
- Ensure buttons are touch-friendly
- Maintain readability across devices

## Best Practices

### Content
- Keep lesson titles under 50 characters
- Use action-oriented homework descriptions
- Make learning outcomes specific and measurable
- Include clear next steps

### Links
- Always test all links before sending
- Use trackable URLs for analytics
- Ensure homework links go to the right assignment
- Include fallback text for broken links

### Testing
- Preview in multiple email clients
- Test on both mobile and desktop
- Check with and without images enabled
- Verify merge tags populate correctly

## Troubleshooting

**Merge tags showing as literal text?**
- Make sure the tags exist in your audience
- Check spelling: `*|TAG_NAME|*`
- Use default values for testing

**Layout looks broken?**
- Ensure you're using the Code block, not HTML block
- Check that all table tags are properly closed
- Verify CSS is inline, not external

**Images not loading?**
- Host images in Mailchimp's Content Studio
- Use absolute URLs, not relative paths
- Include alt text for accessibility

**Mobile display issues?**
- Test on actual devices, not just desktop preview
- Check that media queries are included
- Ensure touch targets are large enough

## Sample Content for Testing

```
MODULE_NUMBER: 3
TOTAL_MODULES: 10
PROGRESS_PERCENTAGE: 30
MODULE_TOPIC: Classification
LESSON_1_TITLE: Churn Prediction Project Overview
LESSON_1_URL: https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/03-classification
OUTCOME_1: Build and evaluate logistic regression models
HOMEWORK_DESCRIPTION: Build a churn prediction model using logistic regression
```

This approach gives you a professional, engaging newsletter that works perfectly within Mailchimp's system while maintaining full design control!
