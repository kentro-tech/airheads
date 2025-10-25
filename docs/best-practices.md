# Best Practices

## Images

### Sizes

Use these dimensions for optimal display:

- **Open Graph**: 1200 × 630 pixels (1.91:1 aspect ratio)
- **Twitter Cards**: 1200 × 675 pixels (16:9 aspect ratio)
- **Favicon**: 32 × 32 pixels (.ico) or scalable SVG
- **Apple Touch Icon**: 180 × 180 pixels
- **Android Icons**: 192 × 192 and 512 × 512 pixels

### Content

- Use high-quality, relevant images
- Ensure text is legible when image is small
- Include alt text for accessibility

## Content

### Titles

- Keep under 60 characters for SEO
- Make them descriptive and unique
- Include target keywords naturally

### Descriptions

- 150-160 characters for optimal search results
- Summarize page content accurately
- Include calls-to-action when appropriate

### URLs

- Use absolute URLs (https://example.com/page)
- Keep canonical URLs consistent
- Avoid URL parameters for content pages

## Twitter Cards

Twitter automatically falls back to Open Graph tags if Twitter-specific tags are missing. This reduces duplication:

```python
# Minimal Twitter Card - uses og: tags for title/description/image
twitter_tags = build_twitter_card(
    card_type="summary_large_image",
    site="@mysite",
)
```

## Structured Data

### When to use

- **Articles**: Blog posts, news, tutorials
- **Products**: E-commerce pages
- **FAQ**: Support pages, documentation
- **How-to**: Step-by-step guides
- **Video**: Video content pages

### Best combinations

Most pages benefit from 2-3 schema types:

- Article page: Article + Breadcrumb + Person (author)
- Product page: Product + Breadcrumb + Organization
- Homepage: Website + Organization + Breadcrumb

## Validation

Test your implementation with these tools:

### Social Preview & Multi-Checker Sites

These tools show how your content appears across multiple social platforms.  This is easiest:

- [OpenGraph.xyz](https://www.opengraph.xyz/) - Preview Open Graph, Twitter Cards, and more
- [HeyMeta](https://www.heymeta.com/) - Comprehensive social media preview tool
- [SocialSharePreview](https://socialsharepreview.com/) - Previews for multiple platforms

### Social Media Validators

Platform-specific validators:

- [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)

### SEO & Structured Data
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema Markup Validator](https://validator.schema.org/)
- [W3C HTML Validator](https://validator.w3.org/nu/)

## Performance

- Generate head tags server-side, not client-side
- Cache structured data when possible
- Validate URLs before including them
- Use relative URLs for favicons when possible

## Accessibility

- Always include image alt text
- Use descriptive link text
- Ensure color contrast in images
- Test with screen readers

## SEO

- Use unique titles and descriptions per page
- Include relevant keywords naturally
- Set proper canonical URLs
- Use HTTPS URLs everywhere
- Keep content fresh and updated
