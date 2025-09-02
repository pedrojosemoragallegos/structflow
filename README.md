# WebFlow

A modern, type-safe Python library for generating HTML documents programmatically. WebFlow provides a clean, Pythonic API for creating HTML with full type hints and comprehensive tag support.

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
from structflow.tags import div, h1, p, a

# Create a document
doc = Document()

# Add content to head and body
doc.add_head(
    title("My Page Title"),
    meta(charset="utf-8"),
    meta(name="viewport", content="width=device-width, initial-scale=1")
)

doc.add(
    div(
        h1("Welcome to WebFlow", class_="hero-title"),
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

The `Document` class serves as the root container for your HTML document:

```python
from structflow import Document

doc = Document(
    doctype="<!DOCTYPE html>",
    html_lang="en",
    html_dir="ltr",
    pretty=True,
    xhtml=False
)
```

### Adding Content

Content is added to the document using `add_head()` and `add()` methods:

```python
from structflow.tags import title, meta, link, div, h1

# Add metadata
doc.add_head(
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
    
    # And many more...
)
```

### Attributes

All elements support both common HTML attributes and element-specific ones:

```python
# Common attributes
div(id="main", class_="container", style="color: blue;")

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
            input(type="text", id="name", name="name", required=True),
            class_="form-group"
        ),
        div(
            label("Email:", for_="email"),
            input(type="email", id="email", name="email", required=True),
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

## Tag Categories

The library organizes tags into logical modules:

- **`edits`**: `ins`, `del_`
- **`embedded`**: `img`, `video`, `audio`, `embed`, `iframe`, `object`, `canvas`, `svg`
- **`forms`**: `form`, `input`, `textarea`, `select`, `button`, `fieldset`, etc.
- **`grouping`**: `div`, `p`, `hr`, `ul`, `ol`, `li`, `dl`, `dt`, `dd`, etc.
- **`links`**: `a`, `link`, `area`
- **`metadata`**: `title`, `meta`, `base`, `style`, `head`
- **`scripting`**: `script`, `noscript`, `template`
- **`sections`**: `section`, `article`, `nav`, `aside`, `header`, `footer`, `main`
- **`table`**: `table`, `thead`, `tbody`, `tr`, `th`, `td`, etc.
- **`text`**: `span`, `strong`, `em`, `code`, `abbr`, `time`, etc.

## Type Safety

WebFlow provides comprehensive type hints:

```python
from typing import Optional
from structflow.tags import div, span

# Type-safe element creation
container: div = div(
    span("Hello", class_="greeting"),
    id="main-container"
)

# Attributes are properly typed
img_element: img = img(
    src="photo.jpg",
    width=300,  # int
    height=200,  # int
    loading="lazy",  # Literal type
    alt="Photo description"  # str
)
```

## Error Handling

The library performs validation at runtime:

```python
# This will work
div("Valid content", class_="valid-class")

# Invalid attribute values will be caught
# img(loading="invalid-value")  # Would raise an error for invalid literal
```

## Best Practices

1. **Use semantic HTML**: Choose elements based on meaning, not appearance
2. **Leverage type hints**: Let your IDE help you with autocompletion
3. **Structure your code**: Break complex layouts into functions
4. **Use CSS classes**: Keep styling separate from structure

```python
def create_card(title: str, content: str, image_url: str) -> div:
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
card = create_card(
    title="Product Name",
    content="Product description here...",
    image_url="product.jpg"
)
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any problems or have questions, please open an issue on GitHub.
