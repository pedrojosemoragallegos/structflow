from __future__ import annotations

import typing

from .base import Container

if typing.TYPE_CHECKING:
    from .types import AttributeValue


class script(Container):
    def __init__(
        self,
        *children: typing.Union[script, noscript, template, str],
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
        src: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        async_: typing.Optional[bool] = None,
        defer: typing.Optional[bool] = None,
        crossorigin: typing.Optional[
            typing.Literal["anonymous", "use-credentials"]
        ] = None,
        integrity: typing.Optional[str] = None,
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
        nomodule: typing.Optional[bool] = None,
        fetchpriority: typing.Optional[typing.Literal["high", "low", "auto"]] = None,
        blocking: typing.Optional[str] = None,
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
        if src is not None:
            self._attributes["src"] = src
        if type is not None:
            self._attributes["type"] = type
        if async_ is not None:
            self._attributes["async"] = async_
        if defer is not None:
            self._attributes["defer"] = defer
        if crossorigin is not None:
            self._attributes["crossorigin"] = crossorigin
        if integrity is not None:
            self._attributes["integrity"] = integrity
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
        if nomodule is not None:
            self._attributes["nomodule"] = nomodule
        if fetchpriority is not None:
            self._attributes["fetchpriority"] = fetchpriority
        if blocking is not None:
            self._attributes["blocking"] = blocking

    def __repr__(self) -> str:
        return f"{self.tag_name()}({', '.join(f'{k}={repr(v)}' for k, v in self._attributes.items())}{f', children={len(self._children)}'})"


class noscript(Container):
    def __init__(
        self,
        *children: typing.Union[script, noscript, template, str],
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

    def __repr__(self) -> str:
        return f"{self.tag_name()}({', '.join(f'{k}={repr(v)}' for k, v in self._attributes.items())}{f', children={len(self._children)}'})"


class template(Container):
    def __init__(
        self,
        *children: typing.Union[script, noscript, template, str],
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

    def __repr__(self) -> str:
        return f"{self.tag_name()}({', '.join(f'{k}={repr(v)}' for k, v in self._attributes.items())}{f', children={len(self._children)}'})"


class slot(Container):
    def __init__(
        self,
        *children: typing.Union[slot, canvas, script, noscript, template, str],
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
        name: typing.Optional[str] = None,
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
        if name is not None:
            self._attributes["name"] = name

    def __repr__(self) -> str:
        return (
            f"{self.tag_name()}({', '.join(f'{k}={repr(v)}' for k, v in self._attributes.items())}"
            f", children={len(self._children)})"
        )


class canvas(Container):
    def __init__(
        self,
        *children: typing.Union[slot, canvas, script, noscript, template, str],
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
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
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
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height

    def __repr__(self) -> str:
        return (
            f"{self.tag_name()}({', '.join(f'{k}={repr(v)}' for k, v in self._attributes.items())}"
            f", children={len(self._children)})"
        )
