from __future__ import annotations

import typing

from .base import Container, Void

if typing.TYPE_CHECKING:
    from .base import AttributeValue
    from .scripting import noscript, script, template


class head(Container):
    def __init__(
        self,
        *children: typing.Union[
            title,
            meta,
            link,
            script,
            style,
            base,
            noscript,
            template,
            str,
        ],
        id: typing.Optional[str] = None,
        class_: typing.Optional[typing.Union[str, list[str]]] = None,
        style: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        dir: typing.Optional[typing.Literal["ltr", "rtl", "auto"]] = None,
        tabindex: typing.Optional[int] = None,
        hidden: typing.Optional[bool] = None,
        draggable: typing.Optional[bool] = None,
        contenteditable: typing.Optional[bool] = None,
        spellcheck: typing.Optional[bool] = None,
        translate: typing.Optional[bool] = None,
        accesskey: typing.Optional[str] = None,
        **kwargs: AttributeValue,
    ):
        super().__init__(
            *children,
            id=id,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir=dir,
            tabindex=tabindex,
            hidden=hidden,
            draggable=draggable,
            contenteditable=contenteditable,
            spellcheck=spellcheck,
            translate=translate,
            accesskey=accesskey,
            **kwargs,
        )


class title(Container):
    def __init__(
        self,
        *children: str,
        id: typing.Optional[str] = None,
        class_: typing.Optional[typing.Union[str, list[str]]] = None,
        style: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        dir: typing.Optional[typing.Literal["ltr", "rtl", "auto"]] = None,
        tabindex: typing.Optional[int] = None,
        hidden: typing.Optional[bool] = None,
        draggable: typing.Optional[bool] = None,
        contenteditable: typing.Optional[bool] = None,
        spellcheck: typing.Optional[bool] = None,
        translate: typing.Optional[bool] = None,
        accesskey: typing.Optional[str] = None,
        **kwargs: AttributeValue,
    ):
        super().__init__(
            *children,
            id=id,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir=dir,
            tabindex=tabindex,
            hidden=hidden,
            draggable=draggable,
            contenteditable=contenteditable,
            spellcheck=spellcheck,
            translate=translate,
            accesskey=accesskey,
            **kwargs,
        )


class meta(Void):
    def __init__(
        self,
        name: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        charset: typing.Optional[str] = None,
        http_equiv: typing.Optional[
            typing.Literal[
                "content-type",
                "default-style",
                "refresh",
                "x-ua-compatible",
                "content-security-policy",
                "content-language",
            ]
        ] = None,
        property: typing.Optional[str] = None,
        itemprop: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        class_: typing.Optional[typing.Union[str, list[str]]] = None,
        style: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        dir: typing.Optional[typing.Literal["ltr", "rtl", "auto"]] = None,
        tabindex: typing.Optional[int] = None,
        hidden: typing.Optional[bool] = None,
        draggable: typing.Optional[bool] = None,
        contenteditable: typing.Optional[bool] = None,
        spellcheck: typing.Optional[bool] = None,
        translate: typing.Optional[bool] = None,
        accesskey: typing.Optional[str] = None,
        **kwargs: AttributeValue,
    ):
        super().__init__(
            id=id,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir=dir,
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
        if property is not None:
            self._attributes["property"] = property
        if itemprop is not None:
            self._attributes["itemprop"] = itemprop


class link(Void):
    def __init__(  # noqa: C901
        self,
        rel: typing.Optional[
            typing.Union[
                str,
                typing.Literal[
                    "alternate",
                    "author",
                    "canonical",
                    "dns-prefetch",
                    "help",
                    "icon",
                    "license",
                    "manifest",
                    "modulepreload",
                    "next",
                    "pingback",
                    "preconnect",
                    "prefetch",
                    "preload",
                    "prerender",
                    "prev",
                    "search",
                    "shortlink",
                    "stylesheet",
                    "tag",
                ],
            ]
        ] = None,
        href: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        media: typing.Optional[str] = None,
        sizes: typing.Optional[str] = None,
        as_: typing.Optional[
            typing.Literal[
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
        ] = None,
        crossorigin: typing.Optional[
            typing.Literal["anonymous", "use-credentials"]
        ] = None,
        integrity: typing.Optional[str] = None,
        hreflang: typing.Optional[str] = None,
        referrerpolicy: typing.Optional[
            typing.Literal[
                "no-referrer",
                "no-referrer-when-downgrade",
                "origin",
                "origin-when-cross-origin",
                "same-origin",
                "strict-origin",
                "strict-origin-when-cross-origin",
                "unsafe-url",
            ]
        ] = None,
        disabled: typing.Optional[bool] = None,
        id: typing.Optional[str] = None,
        class_: typing.Optional[typing.Union[str, list[str]]] = None,
        style: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        dir: typing.Optional[typing.Literal["ltr", "rtl", "auto"]] = None,
        tabindex: typing.Optional[int] = None,
        hidden: typing.Optional[bool] = None,
        draggable: typing.Optional[bool] = None,
        contenteditable: typing.Optional[bool] = None,
        spellcheck: typing.Optional[bool] = None,
        translate: typing.Optional[bool] = None,
        accesskey: typing.Optional[str] = None,
        **kwargs: AttributeValue,
    ):
        super().__init__(
            id=id,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir=dir,
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
        if type is not None:
            self._attributes["type"] = type
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


class style(Container):
    def __init__(
        self,
        *children: str,
        media: typing.Optional[str] = None,
        nonce: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        class_: typing.Optional[typing.Union[str, list[str]]] = None,
        style: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        dir: typing.Optional[typing.Literal["ltr", "rtl", "auto"]] = None,
        tabindex: typing.Optional[int] = None,
        hidden: typing.Optional[bool] = None,
        draggable: typing.Optional[bool] = None,
        contenteditable: typing.Optional[bool] = None,
        spellcheck: typing.Optional[bool] = None,
        translate: typing.Optional[bool] = None,
        accesskey: typing.Optional[str] = None,
        **kwargs: AttributeValue,
    ):
        super().__init__(
            *children,
            id=id,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir=dir,
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
        if type is not None:
            self._attributes["type"] = type


class base(Void):
    def __init__(
        self,
        href: typing.Optional[str] = None,
        target: typing.Optional[
            typing.Literal["_blank", "_self", "_parent", "_top"]
        ] = None,
        id: typing.Optional[str] = None,
        class_: typing.Optional[typing.Union[str, list[str]]] = None,
        style: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        dir: typing.Optional[typing.Literal["ltr", "rtl", "auto"]] = None,
        tabindex: typing.Optional[int] = None,
        hidden: typing.Optional[bool] = None,
        draggable: typing.Optional[bool] = None,
        contenteditable: typing.Optional[bool] = None,
        spellcheck: typing.Optional[bool] = None,
        translate: typing.Optional[bool] = None,
        accesskey: typing.Optional[str] = None,
        **kwargs: AttributeValue,
    ):
        super().__init__(
            id=id,
            class_=class_,
            style=style,
            title=title,
            lang=lang,
            dir=dir,
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
