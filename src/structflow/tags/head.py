from __future__ import annotations

import typing

from .base import Container, Void

if typing.TYPE_CHECKING:
    from .scripting import noscript, script, template
    from .types import AttributeValue


class head(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: title
        | meta
        | link
        | script
        | style
        | base
        | noscript
        | template
        | str,
        id_: str | None = None,
        class_: str | list[str] | None = None,
        style: str | None = None,
        title: str | None = None,
        lang: str | None = None,
        dir_: typing.Literal["ltr", "rtl", "auto"] | None = None,
        tabindex: int | None = None,
        hidden: bool | None = None,
        draggable: bool | None = None,
        contenteditable: bool | None = None,
        spellcheck: bool | None = None,
        translate: bool | None = None,
        accesskey: str | None = None,
        **kwargs: AttributeValue,
    ) -> None:
        super().__init__(
            *children,
            id_=id_,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir_=dir_,
            tabindex=tabindex,
            hidden=hidden,
            draggable=draggable,
            contenteditable=contenteditable,
            spellcheck=spellcheck,
            translate=translate,
            accesskey=accesskey,
            **kwargs,
        )


class title(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: str,
        id_: str | None = None,
        class_: str | list[str] | None = None,
        style: str | None = None,
        title: str | None = None,
        lang: str | None = None,
        dir_: typing.Literal["ltr", "rtl", "auto"] | None = None,
        tabindex: int | None = None,
        hidden: bool | None = None,
        draggable: bool | None = None,
        contenteditable: bool | None = None,
        spellcheck: bool | None = None,
        translate: bool | None = None,
        accesskey: str | None = None,
        **kwargs: AttributeValue,
    ) -> None:
        super().__init__(
            *children,
            id_=id_,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir_=dir_,
            tabindex=tabindex,
            hidden=hidden,
            draggable=draggable,
            contenteditable=contenteditable,
            spellcheck=spellcheck,
            translate=translate,
            accesskey=accesskey,
            **kwargs,
        )


class meta(Void):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        name: str | None = None,
        content: str | None = None,
        charset: str | None = None,
        http_equiv: typing.Literal[
            "content-type",
            "default-style",
            "refresh",
            "x-ua-compatible",
            "content-security-policy",
            "content-language",
        ]
        | None = None,
        property_: str | None = None,
        itemprop: str | None = None,
        id_: str | None = None,
        class_: str | list[str] | None = None,
        style: str | None = None,
        title: str | None = None,
        lang: str | None = None,
        dir_: typing.Literal["ltr", "rtl", "auto"] | None = None,
        tabindex: int | None = None,
        hidden: bool | None = None,
        draggable: bool | None = None,
        contenteditable: bool | None = None,
        spellcheck: bool | None = None,
        translate: bool | None = None,
        accesskey: str | None = None,
        **kwargs: AttributeValue,
    ) -> None:
        super().__init__(
            id_=id_,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir_=dir_,
            tabindex=tabindex,
            hidden=hidden,
            draggable=draggable,
            contenteditable=contenteditable,
            spellcheck=spellcheck,
            translate=translate,
            accesskey=accesskey,
            **kwargs,
        )

        if name is not None:
            self._attributes["name"] = name
        if content is not None:
            self._attributes["content"] = content
        if charset is not None:
            self._attributes["charset"] = charset
        if http_equiv is not None:
            self._attributes["http-equiv"] = http_equiv
        if property_ is not None:
            self._attributes["property"] = property_
        if itemprop is not None:
            self._attributes["itemprop"] = itemprop


class link(Void):  # noqa: N801
    def __init__(  # noqa: C901, PLR0913
        self,
        *,
        rel: str
        | typing.Literal[
            "alternate",  # noqa: PYI051
            "author",  # noqa: PYI051
            "canonical",  # noqa: PYI051
            "dns-prefetch",  # noqa: PYI051
            "help",  # noqa: PYI051
            "icon",  # noqa: PYI051
            "license",  # noqa: PYI051
            "manifest",  # noqa: PYI051
            "modulepreload",  # noqa: PYI051
            "next",  # noqa: PYI051
            "pingback",  # noqa: PYI051
            "preconnect",  # noqa: PYI051
            "prefetch",  # noqa: PYI051
            "preload",  # noqa: PYI051
            "prerender",  # noqa: PYI051
            "prev",  # noqa: PYI051
            "search",  # noqa: PYI051
            "shortlink",  # noqa: PYI051
            "stylesheet",  # noqa: PYI051
            "tag",  # noqa: PYI051
        ]
        | None = None,
        href: str | None = None,
        type_: str | None = None,
        media: str | None = None,
        sizes: str | None = None,
        as_: typing.Literal[
            "audio",
            "document",
            "embed",
            "fetch",
            "font",
            "image",
            "object",
            "script",
            "style",
            "track",
            "video",
            "worker",
        ]
        | None = None,
        crossorigin: typing.Literal["anonymous", "use-credentials"] | None = None,
        integrity: str | None = None,
        hreflang: str | None = None,
        referrerpolicy: typing.Literal[
            "no-referrer",
            "no-referrer-when-downgrade",
            "origin",
            "origin-when-cross-origin",
            "same-origin",
            "strict-origin",
            "strict-origin-when-cross-origin",
            "unsafe-url",
        ]
        | None = None,
        disabled: bool | None = None,
        id_: str | None = None,
        class_: str | list[str] | None = None,
        style: str | None = None,
        title: str | None = None,
        lang: str | None = None,
        dir_: typing.Literal["ltr", "rtl", "auto"] | None = None,
        tabindex: int | None = None,
        hidden: bool | None = None,
        draggable: bool | None = None,
        contenteditable: bool | None = None,
        spellcheck: bool | None = None,
        translate: bool | None = None,
        accesskey: str | None = None,
        **kwargs: AttributeValue,
    ) -> None:
        super().__init__(
            id_=id_,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir_=dir_,
            tabindex=tabindex,
            hidden=hidden,
            draggable=draggable,
            contenteditable=contenteditable,
            spellcheck=spellcheck,
            translate=translate,
            accesskey=accesskey,
            **kwargs,
        )

        if rel is not None:
            self._attributes["rel"] = rel
        if href is not None:
            self._attributes["href"] = href
        if type_ is not None:
            self._attributes["type"] = type_
        if media is not None:
            self._attributes["media"] = media
        if sizes is not None:
            self._attributes["sizes"] = sizes
        if as_ is not None:
            self._attributes["as"] = as_
        if crossorigin is not None:
            self._attributes["crossorigin"] = crossorigin
        if integrity is not None:
            self._attributes["integrity"] = integrity
        if hreflang is not None:
            self._attributes["hreflang"] = hreflang
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
        if disabled is not None:
            self._attributes["disabled"] = disabled


class style(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: str,
        media: str | None = None,
        nonce: str | None = None,
        type_: str | None = None,
        id_: str | None = None,
        class_: str | list[str] | None = None,
        style: str | None = None,
        title: str | None = None,
        lang: str | None = None,
        dir_: typing.Literal["ltr", "rtl", "auto"] | None = None,
        tabindex: int | None = None,
        hidden: bool | None = None,
        draggable: bool | None = None,
        contenteditable: bool | None = None,
        spellcheck: bool | None = None,
        translate: bool | None = None,
        accesskey: str | None = None,
        **kwargs: AttributeValue,
    ) -> None:
        super().__init__(
            *children,
            id_=id_,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir_=dir_,
            tabindex=tabindex,
            hidden=hidden,
            draggable=draggable,
            contenteditable=contenteditable,
            spellcheck=spellcheck,
            translate=translate,
            accesskey=accesskey,
            **kwargs,
        )

        if media is not None:
            self._attributes["media"] = media
        if nonce is not None:
            self._attributes["nonce"] = nonce
        if type_ is not None:
            self._attributes["type"] = type_


class base(Void):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        href: str | None = None,
        target: typing.Literal["_blank", "_self", "_parent", "_top"] | None = None,
        id_: str | None = None,
        class_: str | list[str] | None = None,
        style: str | None = None,
        title: str | None = None,
        lang: str | None = None,
        dir_: typing.Literal["ltr", "rtl", "auto"] | None = None,
        tabindex: int | None = None,
        hidden: bool | None = None,
        draggable: bool | None = None,
        contenteditable: bool | None = None,
        spellcheck: bool | None = None,
        translate: bool | None = None,
        accesskey: str | None = None,
        **kwargs: AttributeValue,
    ) -> None:
        super().__init__(
            id_=id_,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir_=dir_,
            tabindex=tabindex,
            hidden=hidden,
            draggable=draggable,
            contenteditable=contenteditable,
            spellcheck=spellcheck,
            translate=translate,
            accesskey=accesskey,
            **kwargs,
        )

        if href is not None:
            self._attributes["href"] = href
        if target is not None:
            self._attributes["target"] = target
