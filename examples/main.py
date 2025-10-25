"""
AirHeads Demo Web Application

A single-file web application demonstrating the airheads library.
This app shows how to build web pages with proper SEO and social media metadata.

Run with: fastapi dev main.py
Then visit: http://localhost:8000
"""

import os

import air
from air import H1, H2, A, Body, Br, Code, Html, Li, Link, Main, P, Pre, Script, Ul

from airheads import (
    build_favicon_links,
    build_json_ld,
    build_open_graph,
    build_seo_meta,
    build_social_head,
    build_twitter_card,
)
from airheads.schema import (
    build_article_schema,
    build_breadcrumb_schema,
    build_faq_schema,
    build_howto_schema,
    build_organization_schema,
    build_person_schema,
    build_product_schema,
    build_video_schema,
    build_website_schema,
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
                    " library. Click the links below to see different examples of ",
                    "social metadata in action.",
                ),
                H2("Examples"),
                Ul(
                    Li(A("Basic Blog Post", href="/blog-post")),
                    Li(A("Article with JSON-LD", href="/article")),
                    Li(A("Product Page with Schema", href="/product")),
                    Li(A("FAQ Page with Schema", href="/faq")),
                    Li(A("How-To Guide with Schema", href="/howto")),
                    Li(A("Video Page with Schema", href="/video")),
                    Li(A("Person Profile with Schema", href="/person")),
                    Li(A("Organization Page with Schema", href="/organization")),
                    Li(A("Advanced: Individual Tag Builders", href="/advanced")),
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
    # Create JSON-LD structured data using the helper function
    json_ld_str = build_article_schema(
        headline="Advanced Python Web Development with Air",
        description=("Learn advanced patterns for building production-ready web applications with Air"),
        image="https://picsum.photos/seed/advanced-air/1200/630",
        date_published="2025-01-15T10:00:00Z",
        date_modified="2025-01-15T14:30:00Z",
        author_name="Jane Developer",
        author_url=f"{BASE_URL}/about",
        publisher_name="AirHeads Demo",
        publisher_logo="https://picsum.photos/seed/logo/200/200",
        url=f"{BASE_URL}/article",
    )

    json_ld_tag = build_json_ld(json_ld_str)

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
                    "This page includes JSON-LD structured data, which helps ",
                    "search engines understand your content better and can result in ",
                    "rich snippets in search results.",
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
                    Code(json_ld_str),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def product():
    """Example: Product page with Product schema for e-commerce."""
    json_ld_str = build_product_schema(
        name="Air Framework - Python Web Development Made Easy",
        description=(
            "Build beautiful, modern web applications with Python. Perfect for "
            "developers who want the power of FastAPI with intuitive HTML generation."
        ),
        image="https://picsum.photos/seed/air-product/1200/630",
        brand="Kentro Tech",
        price="0.00",
        currency="USD",
        availability="https://schema.org/InStock",
        url=f"{BASE_URL}/product",
    )

    json_ld_tag = build_json_ld(json_ld_str)

    return Html(
        build_social_head(
            "Air Framework - Python Web Development Made Easy",
            (
                "Build beautiful, modern web applications with Python. Perfect for "
                "developers who want the power of FastAPI with intuitive HTML generation."
            ),
            f"{BASE_URL}/product",
            "https://picsum.photos/seed/air-product/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            json_ld_tag,
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
                H2("Product Schema"),
                P(
                    "This page includes Product schema data for e-commerce. ",
                    "Search engines can use this to show price and availability in search results.",
                ),
                Pre(
                    Code(json_ld_str),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
                Br(),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def faq():
    """Example: FAQ page with FAQ schema."""
    json_ld_str = build_faq_schema(
        [
            (
                "What is airheads?",
                "airheads is a helper library for building SEO meta tags, Open Graph tags, Twitter Cards, and \
                    other social media metadata with the Air framework.",
            ),
            (
                "How do I install airheads?",
                "You can install airheads using pip: pip install airheads, or with uv: uv add airheads",
            ),
            (
                "What schema types are supported?",
                "airheads supports Article, Product, Person, Organization, WebSite, Breadcrumb, FAQ, HowTo, and Video schemas.",
            ),
            (
                "Do I need to know JSON-LD?",
                "No! The schema helpers create properly formatted JSON-LD for you. Just call the helper functions with your data.",
            ),
        ]
    )

    json_ld_tag = build_json_ld(json_ld_str)

    return Html(
        build_social_head(
            "Frequently Asked Questions - AirHeads",
            "Common questions about the airheads library and how to use it",
            f"{BASE_URL}/faq",
            "https://picsum.photos/seed/faq/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            json_ld_tag,
            keywords=["faq", "questions", "airheads", "help"],
            site_name="AirHeads Demo",
        ),
        Body(
            Main(
                H1("Frequently Asked Questions"),
                H2("What is airheads?"),
                P(
                    "airheads is a helper library for building SEO meta tags, Open Graph tags, Twitter Cards, and \
                        other social media metadata with the Air framework."
                ),
                H2("How do I install airheads?"),
                P(
                    "You can install airheads using pip: ",
                    Code("pip install airheads"),
                    ", or with uv: ",
                    Code("uv add airheads"),
                ),
                H2("What schema types are supported?"),
                P("airheads supports Article, Product, Person, Organization, WebSite, Breadcrumb, FAQ, HowTo, and Video schemas."),
                H2("Do I need to know JSON-LD?"),
                P("No! The schema helpers create properly formatted JSON-LD for you. Just call the helper functions with your data."),
                H2("FAQ Schema"),
                P("This page uses FAQ schema which can appear as expandable FAQ rich results in search engines."),
                Pre(
                    Code(json_ld_str),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def howto():
    """Example: How-to guide with HowTo schema."""
    json_ld_str = build_howto_schema(
        name="How to Use airheads in Your Project",
        description="Step-by-step guide to adding airheads to your Air application",
        steps=[
            ("Install airheads", "Run: pip install airheads or uv add airheads"),
            ("Import the library", "Add: from airheads import build_social_head"),
            ("Add to your page", "Use build_social_head() in your Html component"),
            ("Test your metadata", "Use social media validator tools to check your tags"),
        ],
        total_time="PT10M",
        tool=["Python", "pip or uv"],
    )

    json_ld_tag = build_json_ld(json_ld_str)

    return Html(
        build_social_head(
            "How to Use airheads in Your Project",
            "Step-by-step guide to adding airheads to your Air application",
            f"{BASE_URL}/howto",
            "https://picsum.photos/seed/howto/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            json_ld_tag,
            keywords=["tutorial", "how-to", "guide", "airheads"],
            site_name="AirHeads Demo",
        ),
        Body(
            Main(
                H1("How to Use airheads in Your Project"),
                P("Follow these simple steps to add SEO and social media metadata to your Air app:"),
                H2("Step 1: Install airheads"),
                P("Run: ", Code("pip install airheads"), " or ", Code("uv add airheads")),
                H2("Step 2: Import the library"),
                P("Add: ", Code("from airheads import build_social_head")),
                H2("Step 3: Add to your page"),
                P("Use ", Code("build_social_head()"), " in your Html component"),
                H2("Step 4: Test your metadata"),
                P("Use social media validator tools to check your tags"),
                H2("HowTo Schema"),
                P("This page uses HowTo schema which can show steps directly in search results."),
                Pre(
                    Code(json_ld_str),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def video():
    """Example: Video page with Video schema."""
    json_ld_str = build_video_schema(
        name="AirHeads Tutorial - Getting Started",
        description="Learn how to use the airheads library in this comprehensive video tutorial",
        thumbnail_url="https://picsum.photos/seed/video-thumb/1200/630",
        upload_date="2025-01-15T10:00:00Z",
        duration="PT15M30S",
        embed_url=f"{BASE_URL}/video",
    )

    json_ld_tag = build_json_ld(json_ld_str)

    return Html(
        build_social_head(
            "AirHeads Tutorial - Getting Started",
            "Learn how to use the airheads library in this comprehensive video tutorial",
            f"{BASE_URL}/video",
            "https://picsum.photos/seed/video-thumb/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            json_ld_tag,
            keywords=["video", "tutorial", "airheads", "learning"],
            site_name="AirHeads Demo",
            og_type="video.other",
        ),
        Body(
            Main(
                H1("AirHeads Tutorial - Getting Started"),
                P("Watch this comprehensive video tutorial to learn how to use airheads."),
                P("(This is a demo page - no actual video embedded)"),
                H2("Video Schema"),
                P("This page uses VideoObject schema which makes videos eligible for Google Video Search and video rich results."),
                Pre(
                    Code(json_ld_str),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def person():
    """Example: Person profile with Person schema."""
    json_ld_str = build_person_schema(
        name="Jane Developer",
        url=f"{BASE_URL}/person",
        image="https://picsum.photos/seed/person/400/400",
        job_title="Senior Software Engineer",
        works_for="Kentro Tech",
        description="Expert in Python web development and the Air framework",
        email="jane@example.com",
    )

    json_ld_tag = build_json_ld(json_ld_str)

    return Html(
        build_social_head(
            "Jane Developer - Senior Software Engineer",
            "Expert in Python web development and the Air framework",
            f"{BASE_URL}/person",
            "https://picsum.photos/seed/person/400/400",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            json_ld_tag,
            keywords=["developer", "engineer", "python", "profile"],
            site_name="AirHeads Demo",
            author="Jane Developer",
            og_type="profile",
        ),
        Body(
            Main(
                H1("Jane Developer"),
                P("Senior Software Engineer at Kentro Tech"),
                P("Expert in Python web development and the Air framework"),
                H2("Person Schema"),
                P("This page uses Person schema which helps establish authorship and can appear in knowledge graph entries."),
                Pre(
                    Code(json_ld_str),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def organization():
    """Example: Organization page with Organization schema."""
    json_ld_str = build_organization_schema(
        name="Kentro Tech",
        url="https://kentro.tech",
        logo="https://picsum.photos/seed/logo/200/200",
        description="Building awesome tools for web developers",
        email="hello@kentro.tech",
    )

    json_ld_tag = build_json_ld(json_ld_str)

    return Html(
        build_social_head(
            "Kentro Tech - Building Awesome Developer Tools",
            "Building awesome tools for web developers",
            f"{BASE_URL}/organization",
            "https://picsum.photos/seed/logo/1200/630",
            Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
            Script(src="https://unpkg.com/htmx.org@2.0.4"),
            json_ld_tag,
            keywords=["company", "organization", "developer tools"],
            site_name="AirHeads Demo",
            og_type="website",
        ),
        Body(
            Main(
                H1("Kentro Tech"),
                P("Building awesome tools for web developers"),
                H2("Organization Schema"),
                P("This page uses Organization schema which enables knowledge panels and brand information in search results."),
                Pre(
                    Code(json_ld_str),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
                P(A("← Back to home", href="/")),
            ),
        ),
    )


@app.page
def advanced():
    """Example: Using individual tag builders instead of build_social_head."""
    from air import Head, Title

    # Build individual tag groups with full control
    seo_tags = build_seo_meta(
        description="Advanced example showing individual tag builder functions",
        keywords=["advanced", "airheads", "seo", "tags"],
        canonical_url=f"{BASE_URL}/advanced",
        author="Kentro Tech",
        theme_color="#2563eb",
    )

    og_tags = build_open_graph(
        title="Advanced: Individual Tag Builders",
        description="Learn to use individual tag builder functions for fine-grained control",
        url=f"{BASE_URL}/advanced",
        image="https://picsum.photos/seed/advanced/1200/630",
        image_width=1200,
        image_height=630,
        type="website",
        site_name="AirHeads Demo",
    )

    twitter_tags = build_twitter_card(
        card_type="summary_large_image",
        site="@kentrotech",
    )

    favicon_tags = build_favicon_links(
        favicon_ico="/favicon.ico",
    )

    # Breadcrumb and Website schemas
    breadcrumb_json = build_breadcrumb_schema(
        [
            ("Home", f"{BASE_URL}/"),
            ("Advanced Examples", f"{BASE_URL}/advanced"),
        ]
    )

    website_json = build_website_schema(
        name="AirHeads Demo",
        url=BASE_URL,
        description="Interactive demonstration of the airheads library",
    )

    breadcrumb_tag = build_json_ld(breadcrumb_json)
    website_tag = build_json_ld(website_json)

    # Build the head manually
    head = Head(
        Title("Advanced: Individual Tag Builders"),
        *seo_tags,
        *og_tags,
        *twitter_tags,
        *favicon_tags,
        breadcrumb_tag,
        website_tag,
        Link(rel="stylesheet", href="https://unpkg.com/mvp.css"),
        Script(src="https://unpkg.com/htmx.org@2.0.4"),
    )

    return Html(
        head,
        Body(
            Main(
                H1("Advanced: Individual Tag Builders"),
                P(
                    "This page demonstrates using the individual tag builder functions ",
                    "instead of ",
                    Code("build_social_head()"),
                    " for fine-grained control.",
                ),
                H2("Individual Builders Used"),
                Ul(
                    Li(Code("build_seo_meta()"), " - SEO meta tags"),
                    Li(Code("build_open_graph()"), " - Open Graph tags"),
                    Li(Code("build_twitter_card()"), " - Twitter Card tags"),
                    Li(Code("build_favicon_links()"), " - Favicon links"),
                    Li(Code("build_breadcrumb_schema()"), " - Breadcrumb navigation"),
                    Li(Code("build_website_schema()"), " - Website schema"),
                ),
                H2("Breadcrumb Schema"),
                Pre(
                    Code(breadcrumb_json),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
                H2("Website Schema"),
                Pre(
                    Code(website_json),
                    style="background: #f5f5f5; padding: 1rem; overflow-x: auto;",
                ),
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
