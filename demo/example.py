from structflow.document import Document
from structflow.tags import (
    a,
    aside,
    base,
    blockquote,
    button,
    caption,
    code,
    div,
    em,
    figcaption,
    figure,
    footer,
    form,
    h1,
    h2,
    header,
    input,
    label,
    li,
    link,
    main,
    mark,
    meta,
    nav,
    noscript,
    option,
    p,
    pre,
    script,
    section,
    select,
    small,
    span,
    strong,
    style,
    table,
    tbody,
    td,
    textarea,
    th,
    thead,
    title,
    tr,
    ul,
)


def build_html() -> str:
    doc: Document = Document(
        meta(charset="utf-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1"),
        meta(name="theme-color", content="#111827"),
        title("Structflow • Complete Example Website"),
        base(href="https://example.com/", target="_self"),
        link(rel="icon", href="/favicon.ico"),
        link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="anonymous",
        ),
        link(rel="stylesheet", href="/static/main.css"),
        style(
            """:root { --brand: #4f46e5; } body { margin:0; font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; } header, footer { background:#111827; color:#fff; padding:1rem; } nav a { margin-right:.75rem; } .container { max-width: 960px; margin: 0 auto; padding: 1rem; } .card { border:1px solid #e5e7eb; border-radius: 12px; padding: 1rem; } table { border-collapse: collapse; width:100%; } th, td { border:1px solid #e5e7eb; padding:.5rem; text-align:left; }"""
        ),
        script(src="https://cdn.example.com/lib.min.js", defer=True),
        script("""window.APP = { version: "1.0.0" };"""),
        noscript(
            "<strong>JavaScript is disabled.</strong> Some features may not work."
        ),
        html_lang="en",
    )

    doc.add(
        header(
            div(
                h1("My Demo Site"),
                p(small("A complete example generated with your tag system.")),
                class_="container",
            )
        ),
        nav(
            div(
                a("Home", href="/"),
                a("Docs", href="/docs"),
                a("About", href="/about"),
                class_="container",
            )
        ),
        main(
            div(
                section(
                    h2("Welcome"),
                    p(
                        "This page demonstrates a variety of HTML elements built with your ",
                        strong("<structflow.tags>"),
                        " package.",
                    ),
                    p(
                        "Visit the ",
                        a("documentation", href="https://example.com/docs"),
                        " to learn more.",
                    ),
                    class_="card",
                ),
                section(
                    h2("Features"),
                    ul(
                        li(
                            "Semantic sections (header/nav/main/section/article/aside/footer)"
                        ),
                        li(
                            "Typography and grouping elements (p, ul/ol/li, blockquote, pre/code)"
                        ),
                        li("Tables and forms"),
                        li(
                            "Head management (meta/link/style/script/noscript/base/title)"
                        ),
                    ),
                    class_="card",
                ),
                section(
                    h2("Quote & Code"),
                    blockquote(
                        '"Simplicity is prerequisite for reliability." — Edsger W. Dijkstra'
                    ),
                    pre(code('print("Hello, structflow!")')),
                    class_="card",
                ),
                section(
                    h2("Data Table"),
                    table(
                        caption("Example Inventory"),
                        thead(tr(th("ID"), th("Name"), th("Qty"), th("Price"))),
                        tbody(
                            tr(td("1"), td("Widget A"), td("12"), td("$9.99")),
                            tr(td("2"), td("Widget B"), td("7"), td("$14.50")),
                            tr(td("3"), td("Widget C"), td("25"), td("$4.75")),
                        ),
                    ),
                    class_="card",
                ),
                section(
                    h2("Contact Us"),
                    form(
                        div(
                            label("Name", for_="name"),
                            input(
                                id="name",
                                name="name",
                                type="text",
                                placeholder="Your name",
                                required=True,
                            ),
                        ),
                        div(
                            label("Topic", for_="topic"),
                            select(
                                option("Support", value="support"),
                                option("Sales", value="sales"),
                                option("Feedback", value="feedback"),
                                id="topic",
                                name="topic",
                            ),
                        ),
                        div(
                            label("Message", for_="msg"),
                            textarea(
                                id="msg",
                                name="message",
                                rows=4,
                                placeholder="How can we help?",
                            ),
                        ),
                        div(button("Send", type="submit")),
                        action="/contact",
                        method="post",
                        class_="card",
                    ),
                ),
                aside(
                    figure(
                        span("📦", aria_hidden="true"),
                        figcaption(em("Fast shipping on all orders")),
                        class_="card",
                    )
                ),
                class_="container",
            )
        ),
        footer(
            div(
                span("© 2025 Example Co. "),
                span("Built with "),
                mark("structflow.tags"),
                class_="container",
            )
        ),
    )

    return doc.render()


if __name__ == "__main__":
    html_out = build_html()
    with open("./demo/site.html", "w", encoding="utf-8") as f:
        f.write(html_out)
