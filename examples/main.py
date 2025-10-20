"""
AirHeads Demo Web Application

A single-file web application demonstrating the airheads library.
This app shows how to build web pages with proper SEO and social media metadata.

Run with: fastapi dev main.py
Then visit: http://localhost:8000
"""

import json
import os

import air
from air import A, Body, Br, Code, H1, H2, Html, Li, Link, Main, P, Pre, Script, Ul

from airheads import (
    build_json_ld,
    build_social_head,
)

# Get base URL from environment (defaults to localhost for development)
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

# Create the Air application
app = air.Air()


@app.page
def index():
    """Home page with navigation to all examples."""
    return Html(
        build_social_head(
            "AirHeads Demo - Interactive Examples",
            "Live demonstration of the airheads library for building SEO and social media metadata",
            BASE_URL,
            "https://picsum.photos/seed/airheads/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            keywords=["python", "air", "seo", "social media", "open graph"],
            site_name="AirHeads Demo",
            author="Kentro Tech",
            theme_color="#2563eb",
        ),
        Body(
            Main(
                H1("AirHeads Demo"),
                P(
                    "Welcome! This is a live demonstration of the ",
                    A("airheads", href="https://github.com/kentro-tech/air-socials"),
                    " library. Click the links below to see different examples of social metadata in action.",
                ),
                H2("Examples"),
                Ul(
                    Li(A("Basic Blog Post", href="/blog-post")),
                    Li(A("Article with JSON-LD", href="/article")),
                    Li(A("Product Page", href="/product")),
                    Li(A("About Page", href="/about")),
                ),
                P(
                    "View the source code of each page to see how the metadata is constructed. ",
                    "Use browser dev tools to inspect the ",
                    Code("<head>"),
                    " tags!",
                ),
            ),
        ),
    )


@app.page
def blog_post():
    """Example: Simple blog post with complete social metadata."""
    return Html(
        build_social_head(
            "Getting Started with Air Framework",
            "A comprehensive guide to building awesome websites with Python and Air",
            f"{BASE_URL}/blog-post",
            "https://picsum.photos/seed/air-tutorial/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            image_alt="Air Framework tutorial cover image",
            keywords=["python", "web development", "air framework", "tutorial"],
            site_name="AirHeads Demo",
            twitter_site="@kentrotech",
            author="Jane Developer",
            og_type="article",
        ),
        Body(
            Main(
                H1("Getting Started with Air Framework"),
                P(
                    "This page demonstrates basic SEO and social media metadata. ",
                    "When you share this URL on Twitter, Facebook, or LinkedIn, ",
                    "it will show a beautiful card with the title, description, and image.",
                ),
                H2("Metadata Features"),
                Ul(
                    Li("SEO meta tags (title, description, keywords)"),
                    Li("Open Graph tags for Facebook and LinkedIn"),
                    Li("Twitter Card tags"),
                    Li("Canonical URL"),
                    Li("Article-specific metadata"),
                ),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def article():
    """Example: Article with JSON-LD structured data for rich search results."""
    # Create JSON-LD structured data for search engines
    article_data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "Advanced Python Web Development with Air",
        "author": {
            "@type": "Person",
            "name": "Jane Developer",
            "url": f"{BASE_URL}/about",
        },
        "datePublished": "2025-01-15T10:00:00Z",
        "dateModified": "2025-01-15T14:30:00Z",
        "image": "https://picsum.photos/seed/advanced-air/1200/630",
        "publisher": {
            "@type": "Organization",
            "name": "AirHeads Demo",
            "logo": {
                "@type": "ImageObject",
                "url": "https://picsum.photos/seed/logo/200/200",
            },
        },
        "description": "Learn advanced patterns for building production-ready web applications with Air",
    }

    json_ld_tag = build_json_ld(json.dumps(article_data, indent=2))

    return Html(
        build_social_head(
            "Advanced Python Web Development with Air",
            "Learn advanced patterns for building production-ready web applications with Air",
            f"{BASE_URL}/article",
            "https://picsum.photos/seed/advanced-air/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            json_ld_tag,  # Extra children come after required positional args
            image_alt="Advanced Air development tutorial",
            keywords=["python", "air", "advanced", "web development"],
            site_name="AirHeads Demo",
            twitter_site="@kentrotech",
            twitter_creator="@janedev",
            og_type="article",
        ),
        Body(
            Main(
                H1("Advanced Python Web Development with Air"),
                P(
                    "This page includes JSON-LD structured data, which helps search engines ",
                    "understand your content better and can result in rich snippets in search results.",
                ),
                H2("JSON-LD Structured Data"),
                P(
                    "Open your browser's dev tools and look at the ",
                    Code('<script type="application/ld+json">'),
                    " tag in the ",
                    Code("<head>"),
                    ". This is the structured data:",
                ),
                Pre(
                    Code(json.dumps(article_data, indent=2)),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def product():
    """Example: Product page optimized for e-commerce."""
    return Html(
        build_social_head(
            "Air Framework - Python Web Development Made Easy",
            "Build beautiful, modern web applications with Python. Perfect for developers who want the power of FastAPI with intuitive HTML generation.",
            f"{BASE_URL}/product",
            "https://picsum.photos/seed/air-product/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            image_alt="Air Framework product showcase",
            image_width=1200,
            image_height=630,
            keywords=["python", "web framework", "air", "buy", "product"],
            site_name="AirHeads Demo",
            twitter_site="@kentrotech",
            og_type="product",
            theme_color="#2563eb",
        ),
        Body(
            Main(
                H1("Air Framework"),
                P("Build beautiful, modern web applications with Python."),
                H2("Product Features"),
                Ul(
                    Li("Type-safe HTML generation with Python"),
                    Li("Built on FastAPI and Starlette"),
                    Li("Perfect for HTMX and modern web apps"),
                    Li("Excellent IDE support with full type hints"),
                    Li("Pydantic-powered forms"),
                ),
                P(
                    "This page uses ",
                    Code('og_type="product"'),
                    " to optimize how it appears when shared on social media.",
                ),
                Br(),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def about():
    """About page with author information."""
    return Html(
        build_social_head(
            "About AirHeads Demo",
            "Learn about this demonstration application and the airheads library",
            f"{BASE_URL}/about",
            "https://picsum.photos/seed/about/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            keywords=["about", "airheads", "demo"],
            site_name="AirHeads Demo",
            author="Kentro Tech",
        ),
        Body(
            Main(
                H1("About This Demo"),
                P(
                    "This is a single-file web application demonstrating the ",
                    A("airheads", href="https://github.com/kentro-tech/air-socials"),
                    " library.",
                ),
                H2("What is airheads?"),
                P(
                    "airheads is a helper library for building SEO meta tags, ",
                    "Open Graph tags, Twitter Cards, and other social media metadata ",
                    "with the Air framework.",
                ),
                H2("Features Demonstrated"),
                Ul(
                    Li("Complete SEO meta tags"),
                    Li("Open Graph protocol for social sharing"),
                    Li("Twitter Card metadata"),
                    Li("JSON-LD structured data"),
                    Li("Different page types (article, product, website)"),
                    Li("Responsive social images"),
                ),
                P(A("← Back to home", href="/")),
            ),
        ),
    )
