from __future__ import annotations

import typing

from .base import Container, Void

if typing.TYPE_CHECKING:
    from .base import Tag
    from .types import AttributeValue


class a(Container):  # TODO does it correspond here?
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        href: typing.Optional[str] = None,
        target: typing.Optional[
            typing.Literal["_self", "_blank", "_parent", "_top"]
        ] = None,
        download: typing.Optional[typing.Union[bool, str]] = None,
        rel: typing.Optional[typing.Union[str, list[str]]] = None,
        hreflang: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
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
        ping: typing.Optional[typing.Union[str, list[str]]] = None,
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

        if href is not None:
            self._attributes["href"] = href
        if target is not None:
            self._attributes["target"] = target
        if download is not None:
            self._attributes["download"] = download
        if rel is not None:
            self._attributes["rel"] = " ".join(rel) if isinstance(rel, list) else rel
        if hreflang is not None:
            self._attributes["hreflang"] = hreflang
        if type is not None:
            self._attributes["type"] = type
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
        if ping is not None:
            self._attributes["ping"] = (
                " ".join(ping) if isinstance(ping, list) else ping
            )


class link(Void):
    def __init__(
        self,
        rel: typing.Union[str, list[str]],
        href: typing.Optional[str] = None,
        crossorigin: typing.Optional[
            typing.Literal["anonymous", "use-credentials"]
        ] = None,
        media: typing.Optional[str] = None,
        integrity: typing.Optional[str] = None,
        hreflang: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
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
        sizes: typing.Optional[str] = None,
        imagesrcset: typing.Optional[str] = None,
        imagesizes: typing.Optional[str] = None,
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
        disabled: typing.Optional[bool] = None,
        fetchpriority: typing.Optional[typing.Literal["high", "low", "auto"]] = None,
        blocking: typing.Optional[str] = None,
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
        self._attributes["rel"] = " ".join(rel) if isinstance(rel, list) else rel

        if href is not None:
            self._attributes["href"] = href
        if crossorigin is not None:
            self._attributes["crossorigin"] = crossorigin
        if media is not None:
            self._attributes["media"] = media
        if integrity is not None:
            self._attributes["integrity"] = integrity
        if hreflang is not None:
            self._attributes["hreflang"] = hreflang
        if type is not None:
            self._attributes["type"] = type
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
        if sizes is not None:
            self._attributes["sizes"] = sizes
        if imagesrcset is not None:
            self._attributes["imagesrcset"] = imagesrcset
        if imagesizes is not None:
            self._attributes["imagesizes"] = imagesizes
        if as_ is not None:
            self._attributes["as"] = as_
        if disabled is not None:
            self._attributes["disabled"] = disabled
        if fetchpriority is not None:
            self._attributes["fetchpriority"] = fetchpriority
        if blocking is not None:
            self._attributes["blocking"] = blocking


class area(Void):  # TODO does it correspond here?
    def __init__(
        self,
        alt: typing.Optional[str] = None,
        coords: typing.Optional[str] = None,
        shape: typing.Optional[
            typing.Literal["rect", "circle", "poly", "default"]
        ] = None,
        href: typing.Optional[str] = None,
        target: typing.Optional[
            typing.Literal["_self", "_blank", "_parent", "_top"]
        ] = None,
        download: typing.Optional[typing.Union[bool, str]] = None,
        ping: typing.Optional[typing.Union[str, list[str]]] = None,
        rel: typing.Optional[typing.Union[str, list[str]]] = None,
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

        if alt is not None:
            self._attributes["alt"] = alt
        if coords is not None:
            self._attributes["coords"] = coords
        if shape is not None:
            self._attributes["shape"] = shape
        if href is not None:
            self._attributes["href"] = href
        if target is not None:
            self._attributes["target"] = target
        if download is not None:
            self._attributes["download"] = download
        if ping is not None:
            self._attributes["ping"] = (
                " ".join(ping) if isinstance(ping, list) else ping
            )
        if rel is not None:
            self._attributes["rel"] = " ".join(rel) if isinstance(rel, list) else rel
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
