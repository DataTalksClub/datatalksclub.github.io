# DataTalks Club Newsletter Templates for Mailchimp

This repository contains HTML email templates specifically designed for DataTalks Club's ML Zoomcamp newsletter campaigns in Mailchimp.

## Files Overview

1. **`newsletter-mailchimp.html`** - Production-ready Mailchimp template with merge tags
2. **`newsletter-demo.html`** - Sample newsletter with realistic content for preview
3. **`newsletter-template-email-safe.html`** - Generic email-safe template (fallback)
4. **`newsletter-template.html`** - Advanced template with modern CSS (web preview)

## Mailchimp Merge Tags Used

The main template (`newsletter-mailchimp.html`) uses these Mailchimp merge tags:

### Personalization Tags
- `*|FNAME|*` - Subscriber's first name
- `*|LNAME|*` - Subscriber's last name (if needed)

### Module-Specific Tags
- `*|MODULE_NUMBER|*` - Current module number (e.g., "3")
- `*|TOTAL_MODULES|*` - Total number of modules (e.g., "10")
- `*|MODULE_TOPIC|*` - Module topic (e.g., "Classification")
- `*|PROGRESS_PERCENTAGE|*` - Progress percentage for progress bar

### Learning Outcomes Tags
- `*|OUTCOME_1|*` - First learning outcome
- `*|OUTCOME_2|*` - Second learning outcome
- `*|OUTCOME_3|*` - Third learning outcome

### Check Questions Tags
- `*|CHECK_QUESTION_1|*` - First comprehension check question
- `*|CHECK_QUESTION_2|*` - Second comprehension check question

### Homework Tags
- `*|HOMEWORK_DESCRIPTION|*` - Description of the homework assignment
- `*|HOMEWORK_SUBMIT_URL|*` - URL for homework submission
- `*|TIME_ESTIMATE|*` - Estimated time to complete module

### URL Tags
- `*|MODULE_START_URL|*` - URL to start the module
- `*|QUESTIONS_URL|*` - URL for submitting questions
- `*|SLACK_URL|*` - Slack channel URL

### Lesson Tags (Course Overview Section)
- `*|LESSON_1_TITLE|*` - Title for lesson 1
- `*|LESSON_1_URL|*` - URL for lesson 1
- `*|LESSON_2_TITLE|*` - Title for lesson 2
- `*|LESSON_2_URL|*` - URL for lesson 2
- `*|LESSON_3_TITLE|*` - Title for lesson 3
- `*|LESSON_3_URL|*` - URL for lesson 3
- `*|LESSON_4_TITLE|*` - Title for lesson 4
- `*|LESSON_4_URL|*` - URL for lesson 4
- `*|LESSON_5_TITLE|*` - Title for lesson 5
- `*|LESSON_5_URL|*` - URL for lesson 5
- `*|LESSON_6_TITLE|*` - Title for lesson 6
- `*|LESSON_6_URL|*` - URL for lesson 6
- `*|LESSON_7_TITLE|*` - Title for lesson 7
- `*|LESSON_7_URL|*` - URL for lesson 7

### Required Mailchimp Tags
- `*|UNSUB|*` - Unsubscribe link (required)
- `*|UPDATE_PROFILE|*` - Update preferences link (required)
- `*|HTML:LIST_ADDRESS_HTML|*` - Mailing address (required)
- `*|HTML:REWARDS|*` - Mailchimp rewards (if enabled)

## Setting Up in Mailchimp

### 1. Create a New Campaign
1. Go to Campaigns → Create Campaign
2. Choose "Email" → "Regular"
3. Select your ML Zoomcamp audience

### 2. Import the Template
1. In the campaign builder, go to "Design Email"
2. Choose "Code your own" → "Import HTML"
3. Copy and paste the content from `newsletter-mailchimp.html`
4. Click "Import"

### 3. Set Up Merge Tags
Create these merge tags in your Mailchimp audience:

**Go to Audience → Settings → Audience fields and *|MERGE|* tags**

| Field Name | Merge Tag | Type | Default Value |
|------------|-----------|------|---------------|
| Module Number | MODULE_NUMBER | Text | 1 |
| Total Modules | TOTAL_MODULES | Text | 10 |
| Module Topic | MODULE_TOPIC | Text | Introduction |
| Progress Percentage | PROGRESS_PERCENTAGE | Number | 10 |
| Outcome 1 | OUTCOME_1 | Text | Learn the basics |
| Outcome 2 | OUTCOME_2 | Text | Apply concepts |
| Outcome 3 | OUTCOME_3 | Text | Build projects |
| Check Question 1 | CHECK_QUESTION_1 | Text | What is ML? |
| Check Question 2 | CHECK_QUESTION_2 | Text | How does it work? |
| Homework Description | HOMEWORK_DESCRIPTION | Text | Complete the exercises |
| Homework Submit URL | HOMEWORK_SUBMIT_URL | Text | https://github.com/... |
| Time Estimate | TIME_ESTIMATE | Text | 8-10 hours |
| Module Start URL | MODULE_START_URL | Text | https://github.com/... |
| Questions URL | QUESTIONS_URL | Text | https://datatalks.club/slack |
| Slack URL | SLACK_URL | Text | https://datatalks.club/slack |
| Lesson 1 Title | LESSON_1_TITLE | Text | Introduction to the Topic |
| Lesson 1 URL | LESSON_1_URL | Text | https://github.com/... |
| Lesson 2 Title | LESSON_2_TITLE | Text | Data Preparation |
| Lesson 2 URL | LESSON_2_URL | Text | https://github.com/... |
| Lesson 3 Title | LESSON_3_TITLE | Text | Model Training |
| Lesson 3 URL | LESSON_3_URL | Text | https://github.com/... |
| Lesson 4 Title | LESSON_4_TITLE | Text | Model Evaluation |
| Lesson 4 URL | LESSON_4_URL | Text | https://github.com/... |
| Lesson 5 Title | LESSON_5_TITLE | Text | Feature Engineering |
| Lesson 5 URL | LESSON_5_URL | Text | https://github.com/... |
| Lesson 6 Title | LESSON_6_TITLE | Text | Advanced Techniques |
| Lesson 6 URL | LESSON_6_URL | Text | https://github.com/... |
| Lesson 7 Title | LESSON_7_TITLE | Text | Project Implementation |
| Lesson 7 URL | LESSON_7_URL | Text | https://github.com/... |

### 4. Customize Content for Each Module
For each newsletter campaign:

1. **Update merge tag values** in your audience or use campaign-specific segments
2. **Test the email** using Mailchimp's preview and test features
3. **Check all links** are working and trackable
4. **Review on mobile** using Mailchimp's mobile preview

## Content Guidelines

### Subject Line Suggestions
- "ML Zoomcamp Module *|MODULE_NUMBER|*: *|MODULE_TOPIC|* Starts Now!"
- "*|FNAME|*, Ready for Module *|MODULE_NUMBER|*? Let's Learn *|MODULE_TOPIC|*"
- "Week *|MODULE_NUMBER|*: Your *|MODULE_TOPIC|* Journey Continues"

### Preheader Text
The template includes hidden preheader text that shows in email previews:
```
Welcome to Module *|MODULE_NUMBER|*! Let's dive into *|MODULE_TOPIC|* together.
```

## Best Practices

### Email Deliverability
- ✅ Uses table-based layout for maximum compatibility
- ✅ Inline CSS for better email client support
- ✅ Optimized for mobile devices
- ✅ Includes proper alt text for images
- ✅ Uses web-safe fonts (Arial, Helvetica, sans-serif)

### Mailchimp Optimization
- ✅ All links include `mc:trackable` for click tracking
- ✅ Required footer elements included
- ✅ Proper merge tag syntax
- ✅ Mobile-responsive design
- ✅ Dark mode considerations

### Content Strategy
- ✅ Clear hierarchy with headings
- ✅ Scannable content with bullet points
- ✅ Strong call-to-action buttons
- ✅ Progress indicators for motivation
- ✅ FAQ section for common questions

## Testing Checklist

Before sending:

- [ ] Preview in Mailchimp's email designer
- [ ] Send test email to yourself
- [ ] Check on mobile device
- [ ] Verify all merge tags populate correctly
- [ ] Test all links and buttons
- [ ] Check unsubscribe link works
- [ ] Verify images load properly
- [ ] Test in different email clients (Gmail, Outlook, Apple Mail)

## Customization Tips

### Colors
The template uses DataTalks Club brand colors:
- Primary: `#2c573e` (dark green)
- Success: `#28a745` (green)
- Warning: `#ffc107` (yellow)
- Info: `#007bff` (blue)
- Background: `#f8f9fa` (light gray)

### Fonts
- Headers: Arial, Helvetica, sans-serif (bold)
- Body: Arial, Helvetica, sans-serif (regular)
- Consistent font stack for email client compatibility

### Responsive Design
The template automatically adapts to mobile devices:
- Single column layout on mobile
- Larger touch targets for buttons
- Optimized padding and spacing
- Readable font sizes

## Troubleshooting

### Common Issues

**Merge tags not working:**
- Ensure merge tags exist in your audience
- Check spelling and syntax: `*|TAG_NAME|*`
- Use default values for testing

**Layout broken in Outlook:**
- Template uses table-based layout for Outlook compatibility
- Avoid advanced CSS features
- Test in Litmus or Email on Acid

**Images not loading:**
- Host images on reliable CDN
- Include alt text for accessibility
- Optimize file sizes for faster loading

**Mobile display issues:**
- Use Mailchimp's mobile preview
- Test on actual devices
- Check button sizes and spacing

### Support Resources
- [Mailchimp Merge Tags Guide](https://mailchimp.com/help/getting-started-with-merge-tags/)
- [Email Design Best Practices](https://mailchimp.com/help/about-email-templates/)
- [Mailchimp Testing Tools](https://mailchimp.com/help/preview-and-test-your-email/)

## Example Usage

Here's how to set up a Module 3 (Classification) newsletter:

1. **Set merge tag values:**
   - MODULE_NUMBER: "3"
   - MODULE_TOPIC: "Classification"
   - PROGRESS_PERCENTAGE: "30"
   - TIME_ESTIMATE: "8-10 hours"

2. **Update URLs:**
   - HOMEWORK_SUBMIT_URL: "https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/cohorts/2024/03-classification/homework.md"
   - MODULE_START_URL: "https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/03-classification"

3. **Customize learning outcomes:**
   - OUTCOME_1: "Build and evaluate logistic regression models"
   - OUTCOME_2: "Understand feature importance and model interpretation"
   - OUTCOME_3: "Apply regularization techniques to improve performance"

4. **Set check questions:**
   - CHECK_QUESTION_1: "What's the difference between logistic and linear regression?"
   - CHECK_QUESTION_2: "How do you interpret coefficients in logistic regression?"

This approach ensures consistent, professional newsletters that engage your ML Zoomcamp students effectively.
