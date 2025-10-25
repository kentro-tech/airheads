"""
airheads: Helper library for building social media cards, SEO tags, and head elements with air.

This library provides convenient functions to generate properly formatted meta tags,
Open Graph tags, Twitter Cards, and other head elements for optimal SEO and social sharing.
"""

from collections.abc import Sequence

from air import Head, Link, Meta, Script, Title
from air.tags.models.base import BaseTag

__version__ = "0.2.0"
__all__ = [
    "build_seo_meta",
    "build_open_graph",
    "build_twitter_card",
    "build_favicon_links",
    "build_json_ld",
    "build_social_head",
]

# Schema.org helpers are in airheads.schema submodule


def _validate_url(url: str, param_name: str) -> None:
    """
    Validate that a URL is absolute (starts with http:// or https://).

    Args:
        url: The URL to validate
        param_name: The parameter name for error messages

    Raises:
        ValueError: If the URL is not absolute
    """
    if not url.startswith(("http://", "https://")):
        raise ValueError(f"{param_name} must be an absolute URL starting with http:// or https://, got: {url!r}")


def build_seo_meta(
    description: str,
    keywords: Sequence[str] | None = None,
    canonical_url: str | None = None,
    robots: str = "index, follow",
    author: str | None = None,
    viewport: str = "width=device-width, initial-scale=1.0",
    charset: str = "utf-8",
    theme_color: str | None = None,
) -> list[BaseTag]:
    """
    Build standard SEO meta tags.

    Args:
        description: Page description for search results
        keywords: List of keywords for the page
        canonical_url: Canonical URL to avoid duplicate content issues
        robots: Robots meta tag value (default: "index, follow")
        author: Page author name
        viewport: Viewport settings for responsive design
        charset: Character encoding (default: "utf-8")
        theme_color: Theme color for browser UI

    Returns:
        List of Meta and Link tags for SEO

    Example:
        >>> from airheads import build_seo_meta
        >>> tags = build_seo_meta(
        ...     description="This is a great page",
        ...     keywords=["python", "web", "framework"],
        ...     canonical_url="https://example.com/page"
        ... )
    """
    tags: list[BaseTag] = []

    tags.append(Meta(charset=charset))
    tags.append(Meta(name="viewport", content=viewport))
    tags.append(Meta(name="description", content=description))

    if keywords:
        tags.append(Meta(name="keywords", content=", ".join(keywords)))

    if author:
        tags.append(Meta(name="author", content=author))

    tags.append(Meta(name="robots", content=robots))

    if canonical_url:
        _validate_url(canonical_url, "canonical_url")
        tags.append(Link(rel="canonical", href=canonical_url))

    if theme_color:
        tags.append(Meta(name="theme-color", content=theme_color))

    return tags


def build_open_graph(
    title: str,
    description: str,
    url: str,
    image: str,
    image_alt: str | None = None,
    image_width: int | None = None,
    image_height: int | None = None,
    type: str = "website",
    site_name: str | None = None,
    locale: str = "en_US",
    article_author: str | None = None,
    article_published_time: str | None = None,
    article_modified_time: str | None = None,
    article_section: str | None = None,
    article_tags: Sequence[str] | None = None,
) -> list[BaseTag]:
    """
    Build Open Graph meta tags for Facebook, LinkedIn, and other social platforms.

    Args:
        title: Content title
        description: Content description
        url: Canonical URL of the page
        image: URL to image for social sharing
        image_alt: Alt text for the image
        image_width: Image width in pixels (recommended: 1200)
        image_height: Image height in pixels (recommended: 630)
        type: Content type (e.g., "website", "article", "video.movie")
        site_name: Name of the overall site
        locale: Locale/language (default: "en_US")
        article_author: Article author (for type="article")
        article_published_time: ISO 8601 datetime (for type="article")
        article_modified_time: ISO 8601 datetime (for type="article")
        article_section: Article section/category (for type="article")
        article_tags: List of article tags (for type="article")

    Returns:
        List of Meta tags with Open Graph properties

    Example:
        >>> from airheads import build_open_graph
        >>> tags = build_open_graph(
        ...     title="My Article",
        ...     description="An interesting article",
        ...     url="https://example.com/article",
        ...     image="https://example.com/image.jpg",
        ...     type="article",
        ...     site_name="My Blog"
        ... )
    """
    # Validate required URLs
    _validate_url(url, "url")
    _validate_url(image, "image")

    tags: list[BaseTag] = [
        Meta(property="og:title", content=title),
        Meta(property="og:description", content=description),
        Meta(property="og:url", content=url),
        Meta(property="og:image", content=image),
        Meta(property="og:type", content=type),
        Meta(property="og:locale", content=locale),
    ]

    if image.startswith("https://"):
        tags.append(Meta(property="og:image:secure_url", content=image))
    if site_name:
        tags.append(Meta(property="og:site_name", content=site_name))
    if image_alt:
        tags.append(Meta(property="og:image:alt", content=image_alt))
    if image_width:
        tags.append(Meta(property="og:image:width", content=str(image_width)))
    if image_height:
        tags.append(Meta(property="og:image:height", content=str(image_height)))

    if type == "article":
        if article_author:
            tags.append(Meta(property="article:author", content=article_author))
        if article_published_time:
            tags.append(Meta(property="article:published_time", content=article_published_time))
        if article_modified_time:
            tags.append(Meta(property="article:modified_time", content=article_modified_time))
        if article_section:
            tags.append(Meta(property="article:section", content=article_section))
        if article_tags:
            for tag in article_tags:
                tags.append(Meta(property="article:tag", content=tag))

    return tags


def build_twitter_card(
    card_type: str = "summary_large_image",
    title: str | None = None,
    description: str | None = None,
    image: str | None = None,
    image_alt: str | None = None,
    site: str | None = None,
    creator: str | None = None,
) -> list[BaseTag]:
    """
    Build Twitter Card meta tags for Twitter/X social sharing.

    Args:
        card_type: Type of card ("summary", "summary_large_image", "app", "player")
        title: Title for the card (falls back to og:title if not specified)
        description: Description for the card (falls back to og:description if not specified)
        image: Image URL for the card (falls back to og:image if not specified)
        image_alt: Alt text for the image
        site: Twitter handle for the website (e.g., "@mysite")
        creator: Twitter handle for content creator (e.g., "@author")

    Returns:
        List of Meta tags for Twitter Cards

    Example:
        >>> from airheads import build_twitter_card
        >>> tags = build_twitter_card(
        ...     card_type="summary_large_image",
        ...     title="My Article",
        ...     description="An interesting article",
        ...     image="https://example.com/image.jpg",
        ...     site="@mysite",
        ...     creator="@author"
        ... )
    """
    tags: list[BaseTag] = [
        Meta(name="twitter:card", content=card_type),
    ]

    if title:
        tags.append(Meta(name="twitter:title", content=title))
    if description:
        tags.append(Meta(name="twitter:description", content=description))
    if image:
        tags.append(Meta(name="twitter:image", content=image))
    if image_alt:
        tags.append(Meta(name="twitter:image:alt", content=image_alt))
    if site:
        tags.append(Meta(name="twitter:site", content=site))
    if creator:
        tags.append(Meta(name="twitter:creator", content=creator))

    return tags


def build_favicon_links(
    favicon_ico: str | None = "/favicon.ico",
    favicon_svg: str | None = None,
    apple_touch_icon: str | None = None,
    icon_192: str | None = None,
    icon_512: str | None = None,
    manifest: str | None = "/manifest.json",
) -> list[BaseTag]:
    """
    Build favicon and icon link tags for various platforms and sizes.

    Args:
        favicon_ico: Path to .ico favicon (default: "/favicon.ico")
        favicon_svg: Path to .svg favicon (modern browsers)
        apple_touch_icon: Path to Apple touch icon (180x180 recommended)
        icon_192: Path to 192x192 PNG icon (Android)
        icon_512: Path to 512x512 PNG icon (Android)
        manifest: Path to web app manifest (default: "/manifest.json")

    Returns:
        List of Link tags for favicons and icons

    Example:
        >>> from airheads import build_favicon_links
        >>> tags = build_favicon_links(
        ...     favicon_ico="/static/favicon.ico",
        ...     favicon_svg="/static/favicon.svg",
        ...     apple_touch_icon="/static/apple-touch-icon.png"
        ... )
    """
    tags: list[BaseTag] = []

    if favicon_ico:
        tags.append(Link(rel="icon", href=favicon_ico, type="image/x-icon"))
    if favicon_svg:
        tags.append(Link(rel="icon", href=favicon_svg, type="image/svg+xml"))
    if apple_touch_icon:
        tags.append(Link(rel="apple-touch-icon", href=apple_touch_icon))
    if icon_192:
        tags.append(Link(rel="icon", href=icon_192, sizes="192x192", type="image/png"))
    if icon_512:
        tags.append(Link(rel="icon", href=icon_512, sizes="512x512", type="image/png"))
    if manifest:
        tags.append(Link(rel="manifest", href=manifest))

    return tags


def build_json_ld(
    json_ld_script: str,
) -> Script:
    """
    Build a JSON-LD structured data script tag.

    Args:
        json_ld_script: JSON-LD structured data as a string

    Returns:
        Script tag containing JSON-LD data

    Example:
        >>> import json
        >>> from airheads import build_json_ld
        >>> data = {
        ...     "@context": "https://schema.org",
        ...     "@type": "Article",
        ...     "headline": "My Article",
        ...     "author": {"@type": "Person", "name": "John Doe"}
        ... }
        >>> script = build_json_ld(json.dumps(data))
    """
    return Script(json_ld_script, type="application/ld+json")


def build_social_head(
    title: str,
    description: str,
    url: str,
    image: str,
    *extra_children: BaseTag,
    keywords: Sequence[str] | None = None,
    image_alt: str | None = None,
    image_width: int | None = 1200,
    image_height: int | None = 630,
    site_name: str | None = None,
    twitter_site: str | None = None,
    twitter_creator: str | None = None,
    author: str | None = None,
    canonical_url: str | None = None,
    favicon_ico: str | None = "/favicon.ico",
    theme_color: str | None = None,
    og_type: str = "website",
    twitter_card: str = "summary_large_image",
    locale: str = "en_US",
    robots: str = "index, follow",
    viewport: str = "width=device-width, initial-scale=1.0",
    charset: str = "utf-8",
    **kwargs: str,
) -> Head:
    """
    Build a complete Head tag with all social media, SEO, and standard elements.

    This is a convenience function that combines build_seo_meta(), build_open_graph(),
    build_twitter_card(), and build_favicon_links() into a single Head tag.

    Args:
        title: Page title
        description: Page description
        url: Canonical URL
        image: Social sharing image URL
        *extra_children: Additional tags to include in the head
        keywords: SEO keywords
        image_alt: Alt text for social image
        image_width: Image width in pixels (default: 1200)
        image_height: Image height in pixels (default: 630)
        site_name: Site name for Open Graph
        twitter_site: Twitter handle for the site (e.g., "@mysite")
        twitter_creator: Twitter handle for the creator (e.g., "@author")
        author: Page author
        canonical_url: Canonical URL (defaults to url if not provided)
        favicon_ico: Path to favicon (default: "/favicon.ico")
        theme_color: Browser theme color
        og_type: Open Graph type (default: "website")
        twitter_card: Twitter card type (default: "summary_large_image")
        locale: Content locale (default: "en_US")
        robots: Robots meta tag value (default: "index, follow")
        viewport: Viewport settings
        charset: Character encoding (default: "utf-8")
        **kwargs: Additional attributes for the Head tag

    Returns:
        Complete Head tag with all social and SEO elements

    Example:
        >>> from air import Html, Body, H1
        >>> from airheads import build_social_head
        >>>
        >>> html = Html(
        ...     build_social_head(
        ...         title="My Awesome Site",
        ...         description="Welcome to my site",
        ...         url="https://example.com",
        ...         image="https://example.com/og-image.jpg",
        ...         site_name="Example.com",
        ...         twitter_site="@example",
        ...         keywords=["python", "web", "framework"],
        ...     ),
        ...     Body(
        ...         H1("Welcome to My Site")
        ...     )
        ... )
    """
    if canonical_url is None:
        canonical_url = url

    seo_tags = build_seo_meta(
        description=description,
        keywords=keywords,
        canonical_url=canonical_url,
        robots=robots,
        author=author,
        viewport=viewport,
        charset=charset,
        theme_color=theme_color,
    )

    og_tags = build_open_graph(
        title=title,
        description=description,
        url=url,
        image=image,
        image_alt=image_alt,
        image_width=image_width,
        image_height=image_height,
        type=og_type,
        site_name=site_name,
        locale=locale,
    )

    twitter_tags = build_twitter_card(
        card_type=twitter_card,
        site=twitter_site,
        creator=twitter_creator,
        # Twitter will fall back to og: tags if these are not specified
    )

    favicon_tags = build_favicon_links(
        favicon_ico=favicon_ico,
    )

    charset_tag = None
    other_seo_tags = []
    for tag in seo_tags:
        if hasattr(tag, "attrs") and "charset" in tag.attrs:
            charset_tag = tag
        else:
            other_seo_tags.append(tag)

    children = []
    if charset_tag:
        children.append(charset_tag)
    children.append(Title(title))
    children.extend(other_seo_tags)
    children.extend(og_tags)
    children.extend(twitter_tags)
    children.extend(favicon_tags)
    children.extend(extra_children)

    return Head(*children, **kwargs)
