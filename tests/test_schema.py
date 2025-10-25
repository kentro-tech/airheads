import json

from airheads.schema import (
    build_article_schema,
    build_breadcrumb_schema,
    build_faq_schema,
    build_organization_schema,
    build_product_schema,
    build_website_schema,
)


def test_build_article_schema():
    """Test article schema returns valid JSON with correct structure."""
    json_str = build_article_schema(
        headline="Test Article",
        description="A test article",
        image="https://example.com/image.jpg",
        date_published="2025-01-15T10:00:00Z",
        author_name="Jane Doe",
        publisher_name="Test Publisher",
    )

    data = json.loads(json_str)
    assert data["@type"] == "Article"
    assert data["headline"] == "Test Article"
    assert data["author"]["name"] == "Jane Doe"


def test_build_product_schema():
    """Test product schema returns valid JSON."""
    json_str = build_product_schema(
        name="Test Product",
        description="A test product",
        image="https://example.com/product.jpg",
        price=99.99,
        currency="USD",
    )

    data = json.loads(json_str)
    assert data["@type"] == "Product"
    assert data["name"] == "Test Product"
    assert data["offers"]["price"] == "99.99"


def test_build_organization_schema():
    """Test organization schema returns valid JSON."""
    json_str = build_organization_schema(
        name="Test Org",
        url="https://example.com",
        logo="https://example.com/logo.png",
    )

    data = json.loads(json_str)
    assert data["@type"] == "Organization"
    assert data["name"] == "Test Org"


def test_build_website_schema():
    """Test website schema returns valid JSON."""
    json_str = build_website_schema(
        name="My Site",
        url="https://example.com",
        search_url="https://example.com/search?q={search_term_string}",
    )

    data = json.loads(json_str)
    assert data["@type"] == "WebSite"
    assert data["potentialAction"]["@type"] == "SearchAction"


def test_build_breadcrumb_schema():
    """Test breadcrumb schema returns valid JSON."""
    json_str = build_breadcrumb_schema(
        [
            ("Home", "https://example.com"),
            ("Blog", "https://example.com/blog"),
        ]
    )

    data = json.loads(json_str)
    assert data["@type"] == "BreadcrumbList"
    assert len(data["itemListElement"]) == 2


def test_build_faq_schema():
    """Test FAQ schema returns valid JSON."""
    json_str = build_faq_schema(
        [
            ("What is this?", "This is a test."),
        ]
    )

    data = json.loads(json_str)
    assert data["@type"] == "FAQPage"
    assert data["mainEntity"][0]["@type"] == "Question"
