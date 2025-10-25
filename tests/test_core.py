"""Simplified tests for core airheads functions."""

import json

from airheads import (
    build_favicon_links,
    build_json_ld,
    build_open_graph,
    build_seo_meta,
    build_social_head,
    build_twitter_card,
)


def test_build_seo_meta_minimal():
    """Test SEO meta with required fields."""
    tags = build_seo_meta(description="Desc")
    combined = " ".join(str(t) for t in tags)

    assert "utf-8" in combined
    assert "viewport" in combined
    assert "Desc" in combined
    assert "robots" in combined


def test_build_seo_meta_with_options():
    """Test SEO meta with optional fields."""
    tags = build_seo_meta(
        description="Desc",
        keywords=["python", "web"],
        author="Jane",
        canonical_url="https://example.com",
        theme_color="#2563eb",
    )
    combined = " ".join(str(t) for t in tags)

    assert "python, web" in combined
    assert "Jane" in combined
    assert "https://example.com" in combined
    assert "#2563eb" in combined


def test_build_open_graph_minimal():
    """Test Open Graph with required fields."""
    tags = build_open_graph(
        title="Title",
        description="Desc",
        url="https://example.com",
        image="https://example.com/img.jpg",
    )
    combined = " ".join(str(t) for t in tags)

    assert "og:title" in combined and "Title" in combined
    assert "og:description" in combined and "Desc" in combined
    assert "og:url" in combined
    assert "og:image" in combined
    assert "og:type" in combined


def test_build_open_graph_article():
    """Test Open Graph with article metadata."""
    tags = build_open_graph(
        title="Article",
        description="Desc",
        url="https://example.com",
        image="https://example.com/img.jpg",
        type="article",
        article_author="Jane",
        article_tags=["python", "web"],
    )
    combined = " ".join(str(t) for t in tags)

    assert "article:author" in combined and "Jane" in combined
    assert "article:tag" in combined and "python" in combined


def test_build_twitter_card():
    """Test Twitter Card."""
    tags = build_twitter_card(
        card_type="summary",
        title="Title",
        site="@site",
        creator="@creator",
    )
    combined = " ".join(str(t) for t in tags)

    assert "twitter:card" in combined and "summary" in combined
    assert "twitter:title" in combined and "Title" in combined
    assert "twitter:site" in combined and "@site" in combined
    assert "twitter:creator" in combined and "@creator" in combined


def test_build_favicon_links():
    """Test favicon links."""
    tags = build_favicon_links(
        favicon_ico="/favicon.ico",
        apple_touch_icon="/apple.png",
    )
    combined = " ".join(str(t) for t in tags)

    assert "/favicon.ico" in combined
    assert "/apple.png" in combined
    assert "apple-touch-icon" in combined


def test_build_social_head():
    """Test complete social head."""
    head = build_social_head(
        title="Page Title",
        description="Page description",
        url="https://example.com",
        image="https://example.com/img.jpg",
        keywords=["python"],
        site_name="My Site",
        twitter_site="@site",
    )
    head_str = str(head)

    # Title tag
    assert "<title>Page Title</title>" in head_str

    # SEO meta
    assert "Page description" in head_str
    assert "python" in head_str

    # Open Graph
    assert "og:title" in head_str
    assert "og:site_name" in head_str and "My Site" in head_str

    # Twitter
    assert "twitter:card" in head_str
    assert "twitter:site" in head_str and "@site" in head_str

    # Favicon
    assert "favicon.ico" in head_str


def test_build_social_head_with_extra_children():
    """Test social head with extra tags."""
    from air import Script

    script = Script(src="https://example.com/script.js")

    head = build_social_head(
        "Test",  # title - must be positional
        "Test",  # description - must be positional
        "https://example.com",  # url - must be positional
        "https://example.com/img.jpg",  # image - must be positional
        script,  # Extra children come after required positional args
    )
    head_str = str(head)

    assert "https://example.com/script.js" in head_str


def test_article_metadata_with_article_type():
    """Test that article:* metadata appears when og_type='article'."""
    tags = build_open_graph(
        title="Test Article",
        description="Test",
        url="https://example.com",
        image="https://example.com/img.jpg",
        type="article",
        article_author="John Doe",
        article_tags=["python", "web"],
    )
    combined = " ".join(str(t) for t in tags)

    assert 'property="article:author"' in combined
    assert "John Doe" in combined
    assert 'property="article:tag"' in combined
    assert "python" in combined


def test_article_metadata_ignored_for_website():
    """Test that article:* metadata is ignored when og_type='website'."""
    tags = build_open_graph(
        title="Test",
        description="Test",
        url="https://example.com",
        image="https://example.com/img.jpg",
        type="website",
        article_author="John Doe",
    )
    combined = " ".join(str(t) for t in tags)

    assert "article:author" not in combined


def test_head_with_custom_attributes():
    """Test that custom attributes pass through to Head tag."""
    head = build_social_head(
        title="Test",
        description="Test",
        url="https://example.com",
        image="https://example.com/img.jpg",
        prefix="og: http://ogp.me/ns#",
        **{"data-test": "value"},
    )
    html = str(head)

    assert 'prefix="og: http://ogp.me/ns#"' in html
    assert 'data-test="value"' in html


def test_build_json_ld():
    """Test JSON-LD script generation."""
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "Test Article",
    }
    json_str = json.dumps(data)
    script = build_json_ld(json_str)

    assert 'type="application/ld+json"' in script.attrs
    assert json_str in str(script)
