# airheads

> [!WARNING]
> This is not ready for use.  Come back in a week or so!

A helper library for building social media cards, SEO tags, and head elements with the [Air framework](https://github.com/airatplants/air).

Example is deployed here, for testing: https://airheads-production.up.railway.app/

## Overview

`airheads` makes it easy to create properly formatted meta tags for:

- **SEO** - Standard meta tags that improve search engine visibility and ranking.
- **Open Graph** - Meta tags that control how your content appears when shared on Facebook, LinkedIn, and other social platforms.
- **Twitter Cards** - Special meta tags that create rich previews on Twitter/X. These make your shared links stand out with images and descriptions.
- **Favicons** - Small icons that appear in browser tabs, bookmarks, and home screens. They help users quickly identify your site.
- **JSON-LD** - Structured data that search engines use to create rich snippets (star ratings, prices, etc.) in search results. This can significantly improve click-through rates.

## Installation

This library requires the Air framework to be installed separately:

```bash
# First, install Air framework
pip install air

# Then install airheads
pip install airheads

# Or with uv
uv add air airheads
```

## Quick Start

### Simple Usage

```python
from air import Html, Body, H1
from airheads import build_social_head

# Build a complete head tag with all social and SEO elements
html = Html(
    build_social_head(
        title="My Awesome Site",
        description="Welcome to my amazing website",
        url="https://example.com",
        image="https://example.com/og-image.jpg",
        site_name="Example.com",
        twitter_site="@example",
        keywords=["python", "web", "framework"],
    ),
    Body(
        H1("Welcome to My Site")
    )
)

# Render to HTML
print(html.render())
```

### Advanced Usage

Build individual tag groups for more control:

```python
from air import Head, Title
from airheads import (
    build_seo_meta,
    build_open_graph,
    build_twitter_card,
    build_favicon_links,
)

# Build individual tag groups
seo_tags = build_seo_meta(
    title="My Article",
    description="An in-depth guide",
    keywords=["python", "tutorial"],
    canonical_url="https://example.com/article",
    author="Jane Developer",
)

og_tags = build_open_graph(
    title="My Article",
    description="An in-depth guide",
    url="https://example.com/article",
    image="https://example.com/article-cover.jpg",
    image_width=1200,
    image_height=630,
    type="article",
    site_name="My Blog",
    article_author="Jane Developer",
    article_section="Tutorials",
    article_tags=["python", "beginner"],
)

twitter_tags = build_twitter_card(
    card_type="summary_large_image",
    site="@myblog",
    creator="@janedev",
)

favicon_tags = build_favicon_links(
    favicon_ico="/static/favicon.ico",
    favicon_svg="/static/favicon.svg",
    apple_touch_icon="/static/apple-touch-icon.png",
)

# Combine them in a Head tag
head = Head(
    Title("My Article"),
    *seo_tags,
    *og_tags,
    *twitter_tags,
    *favicon_tags,
)
```

### JSON-LD Structured Data

Add structured data to help search engines display rich results (star ratings, recipes, events, etc.):

```python
import json
from airheads import build_social_head, build_json_ld

# Create structured data
article_data = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "My Article",
    "author": {
        "@type": "Person",
        "name": "Jane Developer",
    },
    "datePublished": "2025-01-15T10:00:00Z",
    "image": "https://example.com/article.jpg",
}

json_ld_tag = build_json_ld(json.dumps(article_data))

# Include in head (pass as extra positional argument)
head = build_social_head(
    json_ld_tag,  # Extra children come first as positional args
    title="My Article",
    description="An article with structured data",
    url="https://example.com/article",
    image="https://example.com/article.jpg",
)
```

## API Reference

### `build_social_head()`

The main convenience function that builds a complete `Head` tag with all social and SEO elements. Use this when you want everything set up correctly in one call without managing individual tag groups.

**Signature:**
```python
build_social_head(
    *extra_children: BaseTag,
    title: str,
    description: str,
    url: str,
    image: str,
    **kwargs
) -> Head
```

**Parameters:**
- `*extra_children`: Additional tags to include (e.g., Script, Style, custom Meta tags)
- `title` (str): Page title
- `description` (str): Page description
- `url` (str): Canonical URL
- `image` (str): Social sharing image URL
- `keywords` (list[str], optional): SEO keywords
- `image_alt` (str, optional): Alt text for social image
- `image_width` (int, optional): Image width in pixels (default: 1200)
- `image_height` (int, optional): Image height in pixels (default: 630)
- `site_name` (str, optional): Site name for Open Graph
- `twitter_site` (str, optional): Twitter handle for the site (e.g., "@mysite")
- `twitter_creator` (str, optional): Twitter handle for the creator
- `author` (str, optional): Page author
- `theme_color` (str, optional): Browser theme color
- `og_type` (str): Open Graph type (default: "website")
- `twitter_card` (str): Twitter card type (default: "summary_large_image")

### `build_seo_meta()`

Build standard SEO meta tags. These improve your search engine visibility and help search engines understand your content's title, description, and keywords.

**Parameters:**
- `title` (str): Page title
- `description` (str): Page description
- `keywords` (list[str], optional): Keywords for the page
- `canonical_url` (str, optional): Canonical URL
- `robots` (str): Robots meta tag value (default: "index, follow")
- `author` (str, optional): Page author
- `viewport` (str): Viewport settings (default: "width=device-width, initial-scale=1.0")
- `charset` (str): Character encoding (default: "utf-8")
- `theme_color` (str, optional): Theme color for browser UI

### `build_open_graph()`

Build Open Graph meta tags for Facebook, LinkedIn, and other platforms. These control how your content appears when shared on social media, including the preview image, title, and description.

**Parameters:**
- `title` (str): Content title
- `description` (str): Content description
- `url` (str): Canonical URL
- `image` (str): Image URL for social sharing
- `image_alt` (str, optional): Alt text for the image
- `image_width` (int, optional): Image width in pixels
- `image_height` (int, optional): Image height in pixels
- `type` (str): Content type (default: "website")
- `site_name` (str, optional): Site name
- `locale` (str): Locale/language (default: "en_US")
- Article-specific: `article_author`, `article_published_time`, `article_modified_time`, `article_section`, `article_tags`

### `build_twitter_card()`

Build Twitter Card meta tags. These create rich previews on Twitter/X with images and descriptions, making your shared links more engaging.

**Parameters:**
- `card_type` (str): Type of card (default: "summary_large_image")
- `title` (str, optional): Title (falls back to og:title)
- `description` (str, optional): Description (falls back to og:description)
- `image` (str, optional): Image URL (falls back to og:image)
- `image_alt` (str, optional): Alt text for the image
- `site` (str, optional): Twitter handle for the website
- `creator` (str, optional): Twitter handle for the creator

### `build_favicon_links()`

Build favicon and icon link tags. These display your site's icon in browser tabs, bookmarks, and mobile home screens, helping users quickly identify your site.

**Parameters:**
- `favicon_ico` (str, optional): Path to .ico favicon (default: "/favicon.ico")
- `favicon_svg` (str, optional): Path to .svg favicon
- `apple_touch_icon` (str, optional): Path to Apple touch icon
- `icon_192` (str, optional): Path to 192x192 PNG icon
- `icon_512` (str, optional): Path to 512x512 PNG icon
- `manifest` (str, optional): Path to web app manifest (default: "/manifest.json")

### `build_json_ld()`

Build a JSON-LD structured data script tag. This helps search engines create rich snippets (star ratings, prices, event details, etc.) in search results, which can improve click-through rates.

**Parameters:**
- `json_ld_script` (str): JSON-LD structured data as a string

## Examples

See the [examples](./examples) directory for more detailed usage examples:

- `basic_usage.py` - Comprehensive examples of all library features

Run the examples:

```bash
uv run python examples/basic_usage.py
```

## Best Practices

### Image Sizes

For optimal social sharing:
- **Open Graph**: 1200 x 630 pixels (1.91:1 ratio)
- **Twitter**: 1200 x 675 pixels (16:9 ratio) for summary_large_image
- **Favicon**: 32x32 pixels for .ico, any size for .svg
- **Apple Touch Icon**: 180x180 pixels
- **Android Icons**: 192x192 and 512x512 pixels

### Content Guidelines

- **Title**: Keep under 60 characters for SEO
- **Description**: 150-160 characters for optimal search results
- **Image Alt Text**: Be descriptive for accessibility
- **Keywords**: Use 5-10 relevant keywords, don't stuff

### Twitter Cards

Twitter will automatically fall back to Open Graph tags if Twitter Card tags are not specified. You can use this to reduce duplication:

```python
# Minimal Twitter Card - falls back to og: tags
twitter_tags = build_twitter_card(
    card_type="summary_large_image",
    site="@mysite",
)
```

## License

This project is licensed under the same license as the Air framework.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
