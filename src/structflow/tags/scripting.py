from __future__ import annotations

import typing

from .base import Container

if typing.TYPE_CHECKING:
    from .types import AttributeValue


class script(Container):  # noqa: N801
    def __init__(  # noqa: C901, PLR0913
        self,
        *children: script | noscript | template | str,
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
        src: str | None = None,
        type_: str | None = None,
        async_: bool | None = None,
        defer: bool | None = None,
        crossorigin: typing.Literal["anonymous", "use-credentials"] | None = None,
        integrity: str | None = None,
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
        nomodule: bool | None = None,
        fetchpriority: typing.Literal["high", "low", "auto"] | None = None,
        blocking: str | None = None,
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
        if src is not None:
            self._attributes["src"] = src
        if type_ is not None:
            self._attributes["type"] = type_
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
        return f"{self.tag_name()}({', '.join(f'{k}={v!r}' for k, v in self._attributes.items())}{f', children={len(self._children)}'})"  # noqa: E501


class noscript(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: script | noscript | template | str,
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

    def __repr__(self) -> str:
        return f"{self.tag_name()}({', '.join(f'{k}={v!r}' for k, v in self._attributes.items())}{f', children={len(self._children)}'})"  # noqa: E501


class template(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: script | noscript | template | str,
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

    def __repr__(self) -> str:
        return f"{self.tag_name()}({', '.join(f'{k}={v!r}' for k, v in self._attributes.items())}{f', children={len(self._children)}'})"  # noqa: E501


class slot(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: slot | canvas | script | noscript | template | str,
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
        name: str | None = None,
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
        if name is not None:
            self._attributes["name"] = name

    def __repr__(self) -> str:
        return (
            f"{self.tag_name()}({', '.join(f'{k}={v!r}' for k, v in self._attributes.items())}"  # noqa: E501
            f", children={len(self._children)})"
        )


class canvas(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: slot | canvas | script | noscript | template | str,
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
        width: int | None = None,
        height: int | None = None,
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
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height

    def __repr__(self) -> str:
        return (
            f"{self.tag_name()}({', '.join(f'{k}={v!r}' for k, v in self._attributes.items())}"  # noqa: E501
            f", children={len(self._children)})"
        )
