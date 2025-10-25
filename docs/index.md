# airheads

A helper library for building social media cards, SEO tags, and head elements with the [Air framework](https://github.com/airatplants/air).

## What it does

airheads generates the meta tags and structured data that make your site look good when shared on social media and rank better in search engines.

- **SEO tags**: Title, description, keywords, canonical URLs
- **Open Graph**: Facebook, LinkedIn, and other platform previews
- **Twitter Cards**: Rich previews with images on Twitter/X
- **Favicons**: Icons that appear in browser tabs and bookmarks
- **Structured Data**: JSON-LD for rich search results

## Quick start

```python
import air
from airheads import build_social_head

html = air.Html(
    build_social_head(
        title="My Site",
        description="A great website",
        url="https://example.com",
        image="https://example.com/og-image.jpg",
        site_name="My Site",
        twitter_site="@mysite",
    ),
    air.Body(
        air.H1("Welcome")
    )
)
```

## Installation

```bash
pip install airheads
```

Or with uv:

```bash
uv add air airheads
```

## Warning

This library is in early development. While we think it's ready to use, we haven't extensively tested it yet. We'll release v1.0 after several months of real-world usage when we're confident it's solid. We welcome contributions and feedback!
