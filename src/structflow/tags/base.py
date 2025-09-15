from __future__ import annotations

import html
import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:
    from .types import AttributeValue


class Tag(ABC):
    def __init__(  # noqa: C901, PLR0912, PLR0913
        self,
        id_: str | None = None,
        class_: str | list[str] | None = None,
        style: str | None = None,
        *,
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
        self._attributes: dict[str, AttributeValue] = {}

        if id_ is not None:
            self._attributes["id_"] = id_
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
        if dir_ is not None:
            self._attributes["dir"] = dir_
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

    def tag_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def _render(
        self,
        sb: list[str],
        indent_level: int,
        *,
        pretty: bool,
        xhtml: bool,
    ) -> list[str]: ...

    @abstractmethod
    def __repr__(self) -> str: ...


class Void(Tag):
    def __init__(  # noqa: PLR0913
        self,
        id_: str | None = None,
        class_: str | list[str] | None = None,
        style: str | None = None,
        *,
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

    def _format_attributes(self) -> str:
        if not self._attributes:
            return ""

        attributes: list[str] = []
        for key, value in self._attributes.items():
            if value is None:
                continue
            if isinstance(value, bool):
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
        *,
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
        return f"{self.tag_name()}({', '.join(f'{k}={v!r}' for k, v in self._attributes.items())})"  # noqa: E501


class Container(Tag):
    def __init__(  # noqa: PLR0913
        self,
        *children: Tag | str,
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
        self._children: list[Tag | str] = list(children)

    def _format_attributes(self) -> str:
        if not self._attributes:
            return ""

        attributes: list[str] = []
        for key, value in self._attributes.items():
            if value is None:
                continue
            if isinstance(value, bool):
                if value:
                    attributes.append(key)
            else:
                escaped_value = self._escape_text(str(value))
                attributes.append(f'{key}="{escaped_value}"')

        return " " + " ".join(attributes) if attributes else ""

    def __len__(self) -> int:
        return len(self._children)

    def __iter__(self) -> typing.Iterator[Tag | str]:
        return iter(self._children)

    def __getitem__(self, index: int) -> Tag | str:
        return self._children[index]

    def _render_children(
        self,
        sb: list[str],
        indent_level: int,
        *,
        pretty: bool,
        xhtml: bool,
    ) -> list[str]:
        for child in self._children:
            if isinstance(child, Tag):
                child._render(  # noqa: SLF001 TODO: correct it
                    sb=sb,
                    indent_level=indent_level + 1,
                    pretty=pretty,
                    xhtml=xhtml,
                )
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
        *,
        pretty: bool,
        xhtml: bool,
    ) -> list[str]:
        if pretty:
            sb.append(" " * indent_level)

        attributes: str = self._format_attributes()
        sb.append(f"<{self.tag_name()}{attributes}>")

        if pretty:
            sb.append("\n")

        self._render_children(
            sb=sb,
            indent_level=indent_level,
            pretty=pretty,
            xhtml=xhtml,
        )

        if pretty:
            sb.append(" " * indent_level)
        sb.append(f"</{self.tag_name()}>")

        if pretty:
            sb.append("\n")

        return sb

    def __repr__(self) -> str:
        return f"{self.tag_name()}({', '.join(f'{k}={v!r}' for k, v in self._attributes.items())}{f', children={len(self._children)}'})"  # noqa: E501
