from __future__ import annotations

import html as html
import typing
from abc import ABC, abstractmethod

from .types import AttributeValue


class Tag(ABC):
    def __init__(
        self,
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
        self._attributes: dict[str, AttributeValue] = {}

        if id is not None:
            self._attributes["id"] = id
        if class_ is not None:
            if isinstance(class_, list):
                self._attributes["class"] = " ".join(class_)
            else:
                self._attributes["class"] = class_
        if style is not None:
            self._attributes["style"] = style
        if title is not None:
            self._attributes["title"] = title
        if lang is not None:
            self._attributes["lang"] = lang
        if dir is not None:
            self._attributes["dir"] = dir
        if tabindex is not None:
            self._attributes["tabindex"] = tabindex
        if hidden is not None:
            self._attributes["hidden"] = hidden
        if draggable is not None:
            self._attributes["draggable"] = draggable
        if contenteditable is not None:
            self._attributes["contenteditable"] = contenteditable
        if spellcheck is not None:
            self._attributes["spellcheck"] = spellcheck
        if translate is not None:
            self._attributes["translate"] = translate
        if accesskey is not None:
            self._attributes["accesskey"] = accesskey

        for key, value in kwargs.items():
            self._attributes[key] = value

    def _escape_text(self, text: str) -> str:
        return html.escape(str(text), quote=True)

    def __getattr__(self, name: str) -> AttributeValue:
        return self._attributes.get(name)

    def tag_name(self):
        return self.__class__.__name__

    @abstractmethod
    def _render(
        self,
        sb: list[str],
        indent_level: int,
        pretty: bool,
        xhtml: bool,
    ) -> list[str]: ...

    @abstractmethod
    def __repr__(self) -> str: ...


class Void(Tag):
    def __init__(
        self,
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

    def _format_attributes(self) -> str:
        if not self._attributes:
            return ""

        attributes: list[str] = []
        for key, value in self._attributes.items():
            if value is None:
                continue
            elif isinstance(value, bool):
                if value:
                    attributes.append(key)
            else:
                escaped_value = self._escape_text(str(value))
                attributes.append(f'{key}="{escaped_value}"')

        return " " + " ".join(attributes) if attributes else ""

    def _render(
        self,
        sb: list[str],
        indent_level: int,
        pretty: bool,
        xhtml: bool,
    ) -> list[str]:
        if pretty:
            sb.append(" " * indent_level)

        attributes: str = self._format_attributes()
        if xhtml:
            sb.append(f"<{self.tag_name()}{attributes} />")
        else:
            sb.append(f"<{self.tag_name()}{attributes}>")

        if pretty:
            sb.append("\n")

        return sb

    def __repr__(self) -> str:
        return f"{self.tag_name()}({
            ', '.join(f'{k}={repr(v)}' for k, v in self._attributes.items())
        }"


class Container(Tag):
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
        self._children: list[typing.Union[Tag, str]] = list(children)

    def _format_attributes(self) -> str:
        if not self._attributes:
            return ""

        attributes: list[str] = []
        for key, value in self._attributes.items():
            if value is None:
                continue
            elif isinstance(value, bool):
                if value:
                    attributes.append(key)
            else:
                escaped_value = self._escape_text(str(value))
                attributes.append(f'{key}="{escaped_value}"')

        return " " + " ".join(attributes) if attributes else ""

    def __len__(self) -> int:
        return len(self._children)

    def __iter__(self) -> typing.Iterator[typing.Union[Tag, str]]:
        return iter(self._children)

    def __getitem__(self, index: int) -> typing.Union[Tag, str]:
        return self._children[index]

    def _render_children(
        self, sb: list[str], indent_level: int, pretty: bool, xhtml: bool
    ) -> list[str]:
        for child in self._children:
            if isinstance(child, Tag):
                child._render(sb, indent_level + 1, pretty, xhtml)
            else:
                text: str = self._escape_text(str(child))
                if pretty:
                    sb.append(" " * (indent_level + 1))
                sb.append(text)
                if pretty:
                    sb.append("\n")
        return sb

    def _render(
        self,
        sb: list[str],
        indent_level: int,
        pretty: bool,
        xhtml: bool,
    ) -> list[str]:
        if pretty:
            sb.append(" " * indent_level)

        attributes: str = self._format_attributes()
        sb.append(f"<{self.tag_name()}{attributes}>")

        if pretty:
            sb.append("\n")

        self._render_children(sb, indent_level, pretty, xhtml)

        if pretty:
            sb.append(" " * indent_level)
        sb.append(f"</{self.tag_name()}>")

        if pretty:
            sb.append("\n")

        return sb

    def __repr__(self) -> str:
        return f"{self.tag_name()}({', '.join(f'{k}={repr(v)}' for k, v in self._attributes.items())}{f', children={len(self._children)}'})"
