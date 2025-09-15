from __future__ import annotations

import typing

from .base import Container, Void

if typing.TYPE_CHECKING:
    from .base import Tag
    from .types import AttributeValue


class a(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: Tag | str,
        href: str | None = None,
        target: typing.Literal["_self", "_blank", "_parent", "_top"] | None = None,
        download: bool | str | None = None,
        rel: str | list[str] | None = None,
        hreflang: str | None = None,
        type_: str | None = None,
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
        ping: str | list[str] | None = None,
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
        if type_ is not None:
            self._attributes["type"] = type_
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
        if ping is not None:
            self._attributes["ping"] = (
                " ".join(ping) if isinstance(ping, list) else ping
            )


class area(Void):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        alt: str | None = None,
        coords: str | None = None,
        shape: typing.Literal["rect", "circle", "poly", "default"] | None = None,
        href: str | None = None,
        target: typing.Literal["_self", "_blank", "_parent", "_top"] | None = None,
        download: bool | str | None = None,
        ping: str | list[str] | None = None,
        rel: str | list[str] | None = None,
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
