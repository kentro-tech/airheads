# Getting Started

## Basic usage

The easiest way to use airheads is with `build_social_head()`, which creates a complete `<head>` tag with all the essential meta tags.

```python
from airheads import build_social_head
import air

head = build_social_head(
    title="My Article",
    description="A great article about Python",
    url="https://example.com/article",
    image="https://example.com/article.jpg",
    site_name="My Blog",
    twitter_site="@myblog",
    keywords=["python", "tutorial"],
)

html = air.Html(head, air.Body(air.H1("My Article")))
```

## Individual functions

For more control, build each type of tag separately:

```python
from air import Head, Title
from airheads import (
    build_seo_meta,
    build_open_graph,
    build_twitter_card,
    build_favicon_links,
)

# SEO tags
seo_tags = build_seo_meta(
    description="A great article",
    keywords=["python", "tutorial"],
    canonical_url="https://example.com/article",
)

# Social media tags
og_tags = build_open_graph(
    title="My Article",
    description="A great article about Python",
    url="https://example.com/article",
    image="https://example.com/article.jpg",
    type="article",
    site_name="My Blog",
)

twitter_tags = build_twitter_card(
    card_type="summary_large_image",
    site="@myblog",
)

# Favicon tags
favicon_tags = build_favicon_links(
    favicon_ico="/static/favicon.ico",
)

# Combine everything
head = Head(
    Title("My Article"),
    *seo_tags,
    *og_tags,
    *twitter_tags,
    *favicon_tags,
)
```

## Structured data

Add schema.org structured data to improve search results:

```python
from airheads import build_json_ld
from airheads.schema import build_article_schema

# Create structured data
json_str = build_article_schema(
    headline="My Article",
    description="A great article about Python",
    image="https://example.com/article.jpg",
    date_published="2025-01-15T10:00:00Z",
    author_name="Jane Developer",
    publisher_name="My Blog",
)

# Add to head
json_ld_tag = build_json_ld(json_str)

head = build_social_head(
    "My Article",
    "A great article about Python",
    "https://example.com/article",
    "https://example.com/article.jpg",
    json_ld_tag,  # Add as extra child
)
```

## Image requirements

Use these sizes for best results:

- **Open Graph**: 1200 × 630 pixels
- **Twitter**: 1200 × 675 pixels
- **Favicon**: 32 × 32 pixels (or SVG)
- **Apple Touch Icon**: 180 × 180 pixels

## Testing

Validate your tags with these tools:

- [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [Open Graph Preview](https://www.opengraph.xyz/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
