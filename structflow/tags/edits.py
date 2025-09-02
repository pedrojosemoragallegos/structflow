from __future__ import annotations

import typing

from .base import Container

if typing.TYPE_CHECKING:
    from .base import Tag
    from .types import AttributeValue


class ins(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        cite: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
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
        if cite is not None:
            self._attributes["cite"] = cite
        if datetime is not None:
            self._attributes["datetime"] = datetime


class del_(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        cite: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
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
        if cite is not None:
            self._attributes["cite"] = cite
        if datetime is not None:
            self._attributes["datetime"] = datetime

    def tag_name(self):
        return "del"
