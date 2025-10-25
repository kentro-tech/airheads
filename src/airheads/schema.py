"""
Schema.org helpers for building JSON-LD structured data.

These functions make it easy to create properly formatted schema.org objects
without needing to know all the field names and structure.
"""

import json
from datetime import datetime
from typing import Any


def build_article_schema(
    headline: str,
    description: str,
    image: str,
    date_published: str | datetime,
    author_name: str,
    author_url: str | None = None,
    publisher_name: str = "",
    publisher_logo: str | None = None,
    date_modified: str | datetime | None = None,
    url: str | None = None,
) -> str:
    """
    Build JSON-LD Article schema for rich search results.

    Args:
        headline: Article headline/title
        description: Article description
        image: URL to article image
        date_published: Publication date (ISO 8601 string or datetime)
        author_name: Author's name
        author_url: URL to author's page/profile
        publisher_name: Publisher/site name
        publisher_logo: URL to publisher logo
        date_modified: Last modified date (ISO 8601 string or datetime)
        url: Canonical URL of the article

    Returns:
        JSON string ready to use with build_json_ld()

    Example:
        >>> from airheads.schema import build_article_schema
        >>> from airheads import build_json_ld
        >>>
        >>> json_str = build_article_schema(
        ...     headline="My Great Article",
        ...     description="An informative piece",
        ...     image="https://example.com/image.jpg",
        ...     date_published="2025-01-15T10:00:00Z",
        ...     author_name="Jane Developer",
        ...     publisher_name="My Blog"
        ... )
        >>> script = build_json_ld(json_str)
    """
    if isinstance(date_published, datetime):
        date_published = date_published.isoformat()
    if isinstance(date_modified, datetime):
        date_modified = date_modified.isoformat()

    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": description,
        "image": image,
        "datePublished": date_published,
        "author": {
            "@type": "Person",
            "name": author_name,
        },
    }

    if author_url:
        data["author"]["url"] = author_url

    if publisher_name or publisher_logo:
        data["publisher"] = {
            "@type": "Organization",
            "name": publisher_name,
        }
        if publisher_logo:
            data["publisher"]["logo"] = {
                "@type": "ImageObject",
                "url": publisher_logo,
            }

    if date_modified:
        data["dateModified"] = date_modified

    if url:
        data["url"] = url

    return json.dumps(data, indent=2)


def build_product_schema(
    name: str,
    description: str,
    image: str,
    brand: str | None = None,
    price: str | float | None = None,
    currency: str = "USD",
    availability: str = "https://schema.org/InStock",
    url: str | None = None,
    sku: str | None = None,
) -> str:
    """
    Build JSON-LD Product schema for e-commerce.

    Args:
        name: Product name
        description: Product description
        image: URL to product image
        brand: Brand name
        price: Product price (as string or number)
        currency: ISO 4217 currency code (default: "USD")
        availability: Availability URL (default: InStock)
        url: Canonical URL of the product
        sku: Stock keeping unit identifier

    Returns:
        JSON string ready to use with build_json_ld()

    Example:
        >>> from airheads.schema import build_product_schema
        >>> json_str = build_product_schema(
        ...     name="Air Framework",
        ...     description="Python web framework",
        ...     image="https://example.com/product.jpg",
        ...     brand="Kentro Tech",
        ...     price="0.00",
        ...     currency="USD"
        ... )
    """
    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": name,
        "description": description,
        "image": image,
    }

    if brand:
        data["brand"] = {
            "@type": "Brand",
            "name": brand,
        }

    if price is not None:
        data["offers"] = {
            "@type": "Offer",
            "price": str(price),
            "priceCurrency": currency,
            "availability": availability,
        }
        if url:
            data["offers"]["url"] = url

    if sku:
        data["sku"] = sku

    if url and "offers" not in data:
        data["url"] = url

    return json.dumps(data, indent=2)


def build_person_schema(
    name: str,
    url: str | None = None,
    image: str | None = None,
    job_title: str | None = None,
    works_for: str | None = None,
    description: str | None = None,
    email: str | None = None,
) -> str:
    """
    Build JSON-LD Person schema.

    Args:
        name: Person's name
        url: URL to person's website or profile
        image: URL to person's photo
        job_title: Person's job title
        works_for: Organization name
        description: Bio/description
        email: Contact email

    Returns:
        JSON string ready to use with build_json_ld()

    Example:
        >>> from airheads.schema import build_person_schema
        >>> json_str = build_person_schema(
        ...     name="Jane Developer",
        ...     job_title="Software Engineer",
        ...     works_for="Tech Corp"
        ... )
    """
    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": name,
    }

    if url:
        data["url"] = url
    if image:
        data["image"] = image
    if job_title:
        data["jobTitle"] = job_title
    if works_for:
        data["worksFor"] = {
            "@type": "Organization",
            "name": works_for,
        }
    if description:
        data["description"] = description
    if email:
        data["email"] = email

    return json.dumps(data, indent=2)


def build_organization_schema(
    name: str,
    url: str,
    logo: str | None = None,
    description: str | None = None,
    email: str | None = None,
    telephone: str | None = None,
    address: str | None = None,
) -> str:
    """
    Build JSON-LD Organization schema.

    Args:
        name: Organization name
        url: Organization website URL
        logo: URL to organization logo
        description: Organization description
        email: Contact email
        telephone: Contact phone number
        address: Physical address

    Returns:
        JSON string ready to use with build_json_ld()

    Example:
        >>> from airheads.schema import build_organization_schema
        >>> json_str = build_organization_schema(
        ...     name="Kentro Tech",
        ...     url="https://kentro.tech",
        ...     logo="https://kentro.tech/logo.png"
        ... )
    """
    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": name,
        "url": url,
    }

    if logo:
        data["logo"] = {
            "@type": "ImageObject",
            "url": logo,
        }
    if description:
        data["description"] = description
    if email:
        data["email"] = email
    if telephone:
        data["telephone"] = telephone
    if address:
        data["address"] = address

    return json.dumps(data, indent=2)


def build_website_schema(
    name: str,
    url: str,
    description: str | None = None,
    search_url: str | None = None,
) -> str:
    """
    Build JSON-LD WebSite schema for homepage/site-wide data.

    Args:
        name: Website name
        url: Website homepage URL
        description: Website description
        search_url: Search URL template (e.g., "https://example.com/search?q={search_term_string}")

    Returns:
        JSON string ready to use with build_json_ld()

    Example:
        >>> from airheads.schema import build_website_schema
        >>> json_str = build_website_schema(
        ...     name="My Site",
        ...     url="https://example.com",
        ...     search_url="https://example.com/search?q={search_term_string}"
        ... )
    """
    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": name,
        "url": url,
    }

    if description:
        data["description"] = description

    if search_url:
        data["potentialAction"] = {
            "@type": "SearchAction",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": search_url,
            },
            "query-input": "required name=search_term_string",
        }

    return json.dumps(data, indent=2)


def build_breadcrumb_schema(
    items: list[tuple[str, str]],
) -> str:
    """
    Build JSON-LD BreadcrumbList schema for navigation breadcrumbs.

    Args:
        items: List of (name, url) tuples representing the breadcrumb trail

    Returns:
        JSON string ready to use with build_json_ld()

    Example:
        >>> from airheads.schema import build_breadcrumb_schema
        >>> json_str = build_breadcrumb_schema([
        ...     ("Home", "https://example.com"),
        ...     ("Blog", "https://example.com/blog"),
        ...     ("Article", "https://example.com/blog/my-article"),
        ... ])
    """
    item_list = []
    for position, (name, url) in enumerate(items, start=1):
        item_list.append(
            {
                "@type": "ListItem",
                "position": position,
                "name": name,
                "item": url,
            }
        )

    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": item_list,
    }

    return json.dumps(data, indent=2)


def build_faq_schema(
    questions: list[tuple[str, str]],
) -> str:
    """
    Build JSON-LD FAQPage schema for frequently asked questions.

    Args:
        questions: List of (question, answer) tuples

    Returns:
        JSON string ready to use with build_json_ld()

    Example:
        >>> from airheads.schema import build_faq_schema
        >>> json_str = build_faq_schema([
        ...     ("What is Air?", "Air is a Python web framework."),
        ...     ("How do I install it?", "Run: pip install air"),
        ... ])
    """
    main_entity = []
    for question, answer in questions:
        main_entity.append(
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": answer,
                },
            }
        )

    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": main_entity,
    }

    return json.dumps(data, indent=2)


def build_howto_schema(
    name: str,
    description: str,
    steps: list[tuple[str, str]],
    image: str | None = None,
    total_time: str | None = None,
    tool: list[str] | None = None,
    supply: list[str] | None = None,
) -> str:
    """
    Build JSON-LD HowTo schema for step-by-step guides.

    Args:
        name: Title of the how-to guide
        description: Description of what the guide teaches
        steps: List of (step_name, step_text) tuples
        image: URL to image showing the completed result
        total_time: Total time in ISO 8601 duration format (e.g., "PT30M" for 30 minutes)
        tool: List of tools needed
        supply: List of supplies/materials needed

    Returns:
        JSON string ready to use with build_json_ld()

    Example:
        >>> from airheads.schema import build_howto_schema
        >>> json_str = build_howto_schema(
        ...     name="How to Install Air",
        ...     description="Learn to install the Air framework",
        ...     steps=[
        ...         ("Install Python", "Download and install Python 3.8+"),
        ...         ("Install Air", "Run pip install air"),
        ...     ],
        ...     total_time="PT5M"
        ... )
    """
    step_list = []
    for position, (step_name, step_text) in enumerate(steps, start=1):
        step_list.append(
            {
                "@type": "HowToStep",
                "position": position,
                "name": step_name,
                "text": step_text,
            }
        )

    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": name,
        "description": description,
        "step": step_list,
    }

    if image:
        data["image"] = image
    if total_time:
        data["totalTime"] = total_time
    if tool:
        data["tool"] = tool
    if supply:
        data["supply"] = supply

    return json.dumps(data, indent=2)


def build_video_schema(
    name: str,
    description: str,
    thumbnail_url: str,
    upload_date: str | datetime,
    content_url: str | None = None,
    embed_url: str | None = None,
    duration: str | None = None,
) -> str:
    """
    Build JSON-LD VideoObject schema for video content.

    Args:
        name: Video title
        description: Video description
        thumbnail_url: URL to video thumbnail image
        upload_date: Upload date (ISO 8601 string or datetime)
        content_url: Direct URL to video file
        embed_url: URL to embedded player
        duration: Video duration in ISO 8601 format (e.g., "PT1H30M" for 1h 30min)

    Returns:
        JSON string ready to use with build_json_ld()

    Example:
        >>> from airheads.schema import build_video_schema
        >>> json_str = build_video_schema(
        ...     name="Air Framework Tutorial",
        ...     description="Learn to build with Air",
        ...     thumbnail_url="https://example.com/thumb.jpg",
        ...     upload_date="2025-01-15T10:00:00Z",
        ...     embed_url="https://youtube.com/embed/abc123",
        ...     duration="PT15M"
        ... )
    """
    if isinstance(upload_date, datetime):
        upload_date = upload_date.isoformat()

    data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": name,
        "description": description,
        "thumbnailUrl": thumbnail_url,
        "uploadDate": upload_date,
    }

    if content_url:
        data["contentUrl"] = content_url
    if embed_url:
        data["embedUrl"] = embed_url
    if duration:
        data["duration"] = duration

    return json.dumps(data, indent=2)
