# Examples

The `examples/` directory contains complete, runnable examples. Run them with:

```bash
uv run python examples/basic_usage.py
```

## Basic usage

```python
from airheads import build_social_head
import air

# Simple head with all essentials
head = build_social_head(
    title="My Site",
    description="Welcome to my amazing website",
    url="https://example.com",
    image="https://example.com/og-image.jpg",
    site_name="Example.com",
    twitter_site="@example",
    keywords=["python", "web", "framework"],
)

html = air.Html(head, air.Body(air.H1("Welcome")))
```

## Advanced usage

```python
from air import Head, Title
from airheads import (
    build_seo_meta,
    build_open_graph,
    build_twitter_card,
    build_favicon_links,
)
from airheads.schema import build_article_schema, build_breadcrumb_schema
from airheads import build_json_ld

# Build individual components for maximum control
seo_tags = build_seo_meta(
    description="An in-depth guide to Python web development",
    keywords=["python", "web", "tutorial", "beginner"],
    canonical_url="https://example.com/tutorial",
    author="Jane Developer",
)

og_tags = build_open_graph(
    title="Python Web Development Tutorial",
    description="Learn to build web apps with Python and Air",
    url="https://example.com/tutorial",
    image="https://example.com/tutorial-cover.jpg",
    image_width=1200,
    image_height=630,
    type="article",
    site_name="My Blog",
    article_author="Jane Developer",
    article_published_time="2025-01-15T10:00:00Z",
    article_section="Tutorials",
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

# Structured data
article_schema = build_json_ld(build_article_schema(
    headline="Python Web Development Tutorial",
    description="An in-depth guide to building web apps",
    image="https://example.com/tutorial-cover.jpg",
    date_published="2025-01-15T10:00:00Z",
    author_name="Jane Developer",
    publisher_name="My Blog",
))

breadcrumb_schema = build_json_ld(build_breadcrumb_schema([
    ("Home", "https://example.com"),
    ("Tutorials", "https://example.com/tutorials"),
    ("Python Web Development", "https://example.com/tutorial"),
]))

# Combine everything
head = Head(
    Title("Python Web Development Tutorial"),
    *seo_tags,
    *og_tags,
    *twitter_tags,
    *favicon_tags,
    article_schema,
    breadcrumb_schema,
)
```

## Schema types

### Article

```python
from airheads.schema import build_article_schema

json_str = build_article_schema(
    headline="My Article",
    description="Article description",
    image="https://example.com/image.jpg",
    date_published="2025-01-15T10:00:00Z",
    author_name="Jane Developer",
    publisher_name="My Blog",
)
```

### Product

```python
from airheads.schema import build_product_schema

json_str = build_product_schema(
    name="My Product",
    description="Product description",
    image="https://example.com/product.jpg",
    brand="My Brand",
    price="29.99",
    currency="USD",
)
```

### FAQ

```python
from airheads.schema import build_faq_schema

json_str = build_faq_schema([
    ("What is Air?", "Air is a Python web framework."),
    ("How do I install it?", "Run: pip install air"),
])
```

See the complete examples in the `examples/` directory for more patterns.
