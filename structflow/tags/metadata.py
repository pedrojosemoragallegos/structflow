from __future__ import annotations

import typing

from .base import Container, Void

if typing.TYPE_CHECKING:
    from .base import Tag
    from .types import AttributeValue


class title(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
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


class base(Void):
    def __init__(
        self,
        href: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        *,
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


class link(Void):
    def __init__(
        self,
        href: typing.Optional[str] = None,
        rel: typing.Optional[typing.Union[str, list[str]]] = None,
        as_: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        hreflang: typing.Optional[str] = None,
        media: typing.Optional[str] = None,
        referrerpolicy: typing.Optional[str] = None,
        crossorigin: typing.Optional[
            typing.Literal["anonymous", "use-credentials"]
        ] = None,
        integrity: typing.Optional[str] = None,
        imagesrcset: typing.Optional[str] = None,
        imagesizes: typing.Optional[str] = None,
        sizes: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        fetchpriority: typing.Optional[typing.Literal["high", "low", "auto"]] = None,
        *,
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
        if rel is not None:
            self._attributes["rel"] = " ".join(rel) if isinstance(rel, list) else rel
        if as_ is not None:
            self._attributes["as"] = as_
        if type is not None:
            self._attributes["type"] = type
        if hreflang is not None:
            self._attributes["hreflang"] = hreflang
        if media is not None:
            self._attributes["media"] = media
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
        if crossorigin is not None:
            self._attributes["crossorigin"] = crossorigin
        if integrity is not None:
            self._attributes["integrity"] = integrity
        if imagesrcset is not None:
            self._attributes["imagesrcset"] = imagesrcset
        if imagesizes is not None:
            self._attributes["imagesizes"] = imagesizes
        if sizes is not None:
            self._attributes["sizes"] = sizes
        if disabled is not None:
            self._attributes["disabled"] = disabled
        if fetchpriority is not None:
            self._attributes["fetchpriority"] = fetchpriority


class meta(Void):
    def __init__(
        self,
        charset: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        http_equiv: typing.Optional[str] = None,  # renders as "http-equiv"
        media: typing.Optional[str] = None,
        scheme: typing.Optional[str] = None,  # legacy, still seen in the wild
        property_: typing.Optional[
            str
        ] = None,  # renders as "property" (e.g., Open Graph)
        itemprop: typing.Optional[str] = None,
        *,
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
        if charset is not None:
            self._attributes["charset"] = charset
        if name is not None:
            self._attributes["name"] = name
        if content is not None:
            self._attributes["content"] = content
        if http_equiv is not None:
            self._attributes["http-equiv"] = http_equiv
        if media is not None:
            self._attributes["media"] = media
        if scheme is not None:
            self._attributes["scheme"] = scheme
        if property_ is not None:
            self._attributes["property"] = property_
        if itemprop is not None:
            self._attributes["itemprop"] = itemprop


class style(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        media: typing.Optional[str] = None,
        nonce: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        blocking: typing.Optional[typing.Literal["render"]] = None,
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
        if blocking is not None:
            self._attributes["blocking"] = blocking


class head(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        profile: typing.Optional[str] = None,
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
        if profile is not None:
            self._attributes["profile"] = profile
