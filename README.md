# StructFlow

A modern, type-safe Python library for generating HTML documents programmatically. StructFlow provides a clean, Pythonic API for creating HTML with full type hints and comprehensive tag support.

## Features

- **Type-safe**: Full type hints with mypy support
- **Complete HTML5 support**: All standard HTML5 elements and attributes
- **Clean API**: Intuitive, Pythonic interface
- **Flexible rendering**: Pretty-printing and minified output options
- **XHTML support**: Optional XHTML-compliant output
- **Extensible**: Easy to extend with custom elements and attributes

## Installation

```bash
pip install structflow
```

Or with Poetry:

```bash
poetry add structflow
```

## Quick Start

```python
from structflow import Document
from structflow.tags import div, h1, p, a, title, meta

# Create a document with head elements
doc = Document(
    title("My Page Title"),
    meta(charset="utf-8"),
    meta(name="viewport", content="width=device-width, initial-scale=1"),
    html_lang="en"
)

# Add content to body
doc.add(
    div(
        h1("Welcome to StructFlow", class_="hero-title"),
        p("A modern HTML generation library for Python."),
        a("Learn more", href="https://example.com", class_="btn btn-primary")
    )
)

# Render the document
html_output = doc.render()
print(html_output)
```

## Core Concepts

### Document Structure

The `Document` class serves as the root container for your HTML document. Head elements are passed directly to the constructor:

```python
from structflow import Document
from structflow.tags import title, meta, link

doc = Document(
    # Head elements passed directly
    title("Page Title"),
    meta(charset="utf-8"),
    meta(name="viewport", content="width=device-width, initial-scale=1"),
    link(rel="stylesheet", href="styles.css"),
    # Document options
    doctype="<!DOCTYPE html>",
    html_lang="en",
    html_dir="ltr",
    pretty=True,
    xhtml=False
)
```

### Adding Content

Head elements are specified in the document constructor, while body content is added using the `add()` method:

```python
from structflow.tags import title, meta, link, div, h1

# Create document with head elements
doc = Document(
    title("Page Title"),
    meta(charset="utf-8"),
    link(rel="stylesheet", href="styles.css")
)

# Add body content
doc.add(
    div(
        h1("Hello World"),
        class_="container"
    )
)
```

### HTML Elements

All HTML5 elements are available as classes with proper typing:

```python
from structflow.tags import (
    # Structure
    div, span, section, article, nav, aside, header, footer, main,
    
    # Text content
    h1, h2, h3, h4, h5, h6, p, blockquote, pre,
    
    # Lists
    ul, ol, li, dl, dt, dd,
    
    # Forms
    form, input, textarea, select, option, button, label,
    
    # Media
    img, video, audio, source, picture,
    
    # Tables
    table, thead, tbody, tfoot, tr, th, td,
    
    # Head elements
    title, meta, link, script, style, base,
    
    # And many more...
)
```

### Attributes

All elements support both common HTML attributes and element-specific ones:

```python
# Common attributes
div(id_="main", class_="container", style="color: blue;")

# Element-specific attributes
img(src="image.jpg", alt="Description", width=300, height=200)
input(type="email", name="email", required=True, placeholder="Enter email")
a(href="https://example.com", target="_blank", rel="noopener")
```

### Class Attribute Handling

The `class_` parameter accepts both strings and lists:

```python
# String
div(class_="btn btn-primary")

# List (automatically joined with spaces)
div(class_=["btn", "btn-primary", "btn-large"])
```

## Advanced Usage

### Head Elements

StructFlow provides comprehensive support for all head elements with proper typing:

```python
from structflow.tags import title, meta, link, script, style

doc = Document(
    # Page metadata
    title("My Application"),
    meta(charset="utf-8"),
    meta(name="description", content="A great web application"),
    meta(name="keywords", content="python, html, web"),
    meta(name="author", content="Your Name"),
    
    # Viewport for responsive design
    meta(name="viewport", content="width=device-width, initial-scale=1"),
    
    # Open Graph metadata
    meta(property="og:title", content="My Application"),
    meta(property="og:description", content="A great web application"),
    meta(property="og:image", content="https://example.com/image.jpg"),
    
    # External resources
    link(rel="stylesheet", href="styles.css"),
    link(rel="icon", href="favicon.ico", type="image/x-icon"),
    link(rel="preconnect", href="https://fonts.googleapis.com"),
    
    # Scripts
    script(src="https://cdn.example.com/library.js", defer=True),
    
    # Inline styles
    style("""
        body { 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
        }
    """),
    
    html_lang="en"
)
```

### Custom Attributes

Use `**kwargs` for custom or non-standard attributes:

```python
div(
    "Content",
    data_id="123",
    data_toggle="modal",
    aria_label="Close button"
)
```

### Nested Elements

Elements can be deeply nested:

```python
nav(
    div(
        ul(
            li(a("Home", href="/")),
            li(a("About", href="/about")),
            li(a("Contact", href="/contact"))
        ),
        class_="navbar-nav"
    ),
    class_="navbar"
)
```

### Forms

Creating forms with proper structure:

```python
form(
    fieldset(
        legend("Contact Information"),
        div(
            label("Name:", for_="name"),
            input(type="text", id_="name", name="name", required=True),
            class_="form-group"
        ),
        div(
            label("Email:", for_="email"),
            input(type="email", id_="email", name="email", required=True),
            class_="form-group"
        ),
        button("Submit", type="submit", class_="btn btn-primary")
    ),
    action="/submit",
    method="post"
)
```

### Tables

Building data tables:

```python
table(
    thead(
        tr(
            th("Name"),
            th("Age"),
            th("City")
        )
    ),
    tbody(
        tr(
            td("John Doe"),
            td("30"),
            td("New York")
        ),
        tr(
            td("Jane Smith"),
            td("25"),
            td("Los Angeles")
        )
    ),
    class_="data-table"
)
```

### Media Elements

Working with images and multimedia:

```python
# Responsive image
picture(
    source(
        srcset="image-large.jpg",
        media="(min-width: 800px)"
    ),
    source(
        srcset="image-medium.jpg", 
        media="(min-width: 400px)"
    ),
    img(
        src="image-small.jpg",
        alt="Responsive image",
        class_="responsive-img"
    )
)

# Video with multiple sources
video(
    source(src="video.mp4", type="video/mp4"),
    source(src="video.webm", type="video/webm"),
    "Your browser doesn't support video.",
    controls=True,
    width=640,
    height=480
)
```

## Rendering Options

### Pretty Printing

Enable pretty printing for readable output:

```python
doc = Document(pretty=True)
# or
html_output = doc.render(pretty=True)
```

### XHTML Mode

Generate XHTML-compliant output:

```python
doc = Document(xhtml=True)
# or
html_output = doc.render(xhtml=True)
```

### Custom Doctype

Specify a custom doctype:

```python
doc = Document(doctype="<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"")
```

## Complete Example

Here's a comprehensive example showing a complete HTML document:

```python
from structflow import Document
from structflow.tags import *

# Create document with comprehensive head
doc = Document(
    # Basic metadata
    title("StructFlow Demo - Modern HTML Generation"),
    meta(charset="utf-8"),
    meta(name="viewport", content="width=device-width, initial-scale=1"),
    meta(name="description", content="Demo of StructFlow HTML generation"),
    
    # External resources
    link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"),
    link(rel="icon", href="favicon.ico"),
    
    # Custom styles
    style("""
        .hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .hero h1 { color: white; }
    """),
    
    html_lang="en"
)

# Build the page content
doc.add(
    header(
        nav(
            div(
                a("StructFlow", href="#", class_="navbar-brand"),
                ul(
                    li(a("Home", href="#", class_="nav-link"), class_="nav-item"),
                    li(a("Docs", href="#", class_="nav-link"), class_="nav-item"),
                    li(a("GitHub", href="#", class_="nav-link"), class_="nav-item"),
                    class_="navbar-nav ms-auto"
                ),
                class_="container-fluid"
            ),
            class_="navbar navbar-expand-lg navbar-dark bg-dark"
        )
    ),
    
    main(
        section(
            div(
                div(
                    div(
                        h1("Modern HTML Generation", class_="display-4"),
                        p("Build HTML documents with Python using a clean, type-safe API.", 
                          class_="lead"),
                        a("Get Started", href="#features", class_="btn btn-light btn-lg"),
                        class_="col-md-8"
                    ),
                    class_="row justify-content-center text-center"
                ),
                class_="container py-5"
            ),
            class_="hero py-5"
        ),
        
        section(
            div(
                h2("Features", class_="text-center mb-5"),
                div(
                    div(
                        div(
                            h3("Type Safe"),
                            p("Full type hints with mypy support for error-free development."),
                            class_="card-body"
                        ),
                        class_="card h-100"
                    ),
                    div(
                        div(
                            h3("Modern API"),
                            p("Clean, Pythonic interface that feels natural to use."),
                            class_="card-body"
                        ),
                        class_="card h-100"
                    ),
                    div(
                        div(
                            h3("Complete"),
                            p("All HTML5 elements and attributes with proper validation."),
                            class_="card-body"
                        ),
                        class_="card h-100"
                    ),
                    class_="row g-4"
                ),
                class_="container py-5"
            ),
            id_="features"
        )
    ),
    
    footer(
        div(
            p("© 2025 StructFlow. Built with ❤️ and Python.", 
              class_="text-center text-muted"),
            class_="container py-4"
        ),
        class_="bg-light mt-5"
    ),
    
    # Bootstrap JavaScript
    script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js")
)

# Render the complete document
html_output = doc.render()
```

## Tag Categories

The library organizes tags into logical modules:

- **`head`**: `title`, `meta`, `link`, `script`, `style`, `base`, `noscript`, `template`
- **`edits`**: `ins`, `del_`
- **`embedded`**: `img`, `video`, `audio`, `embed`, `iframe`, `object`, `canvas`, `svg`
- **`forms`**: `form`, `input`, `textarea`, `select`, `button`, `fieldset`, etc.
- **`grouping`**: `div`, `p`, `hr`, `ul`, `ol`, `li`, `dl`, `dt`, `dd`, etc.
- **`links`**: `a`, `area`
- **`scripting`**: `script`, `noscript`, `template`
- **`sections`**: `section`, `article`, `nav`, `aside`, `header`, `footer`, `main`
- **`table`**: `table`, `thead`, `tbody`, `tr`, `th`, `td`, etc.
- **`text`**: `span`, `strong`, `em`, `code`, `abbr`, `time`, etc.

## Type Safety

StructFlow provides comprehensive type hints:

```python
from typing import Optional
from structflow.tags import div, span, meta, link

# Type-safe element creation
container: div = div(
    span("Hello", class_="greeting"),
    id_="main-container"
)

# Head elements with proper typing
metadata: meta = meta(
    name="viewport", 
    content="width=device-width, initial-scale=1"
)

# Attributes are properly typed
stylesheet: link = link(
    rel="stylesheet",  # Literal type
    href="styles.css",  # str
    media="screen"  # str
)
```

## Best Practices

1. **Organize head elements logically**: Group related metadata together
2. **Use semantic HTML**: Choose elements based on meaning, not appearance
3. **Leverage type hints**: Let your IDE help you with autocompletion
4. **Structure your code**: Break complex layouts into functions
5. **Separate concerns**: Keep head metadata separate from body content

```python
def create_page_head(title: str, description: str) -> tuple:
    """Create standard head elements for a page."""
    return (
        title(title),
        meta(charset="utf-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1"),
        meta(name="description", content=description),
        link(rel="stylesheet", href="styles.css")
    )

def create_card(title: str, content: str, image_url: str) -> div:
    """Create a reusable card component."""
    return div(
        img(src=image_url, alt=title, class_="card-image"),
        div(
            h3(title, class_="card-title"),
            p(content, class_="card-content"),
            class_="card-body"
        ),
        class_="card"
    )

# Usage
doc = Document(
    *create_page_head("My Site", "Welcome to my website"),
    html_lang="en"
)

doc.add(
    create_card(
        title="Product Name",
        content="Product description here...",
        image_url="product.jpg"
    )
)
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any problems or have questions, please open an issue on GitHub.
