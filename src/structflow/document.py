from __future__ import annotations

import typing

from structflow.tags import (
    base,
    body,
    head,
    link,
    meta,
    noscript,
    script,
    style,
    template,
    title,
)
from structflow.tags.base import Container

if typing.TYPE_CHECKING:
    from typing_extensions import Self

    from structflow.tags.base import Tag
    from structflow.tags.types import AttributeValue


class html(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: head | body | Tag | str,
        lang: str | None = None,
        dir_: typing.Literal["ltr", "rtl", "auto"] | None = None,
        xmlns: str | None = None,
        manifest: str | None = None,
        id_: str | None = None,
        class_: str | list[str] | None = None,
        style: str | None = None,
        title: str | None = None,
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

        if xmlns is not None:
            self._attributes["xmlns"] = xmlns
        if manifest is not None:
            self._attributes["manifest"] = manifest


class Document:
    # for typing reasons
    _head: head
    _body: body
    _root: html

    def __init__(
        self,
        *head_elements: title
        | meta
        | link
        | script
        | style
        | base
        | noscript
        | template
        | str,
        doctype: str = "<!DOCTYPE html>",
        html_lang: str | None = None,
        html_dir: typing.Literal["ltr", "rtl", "auto"] | None = None,
        pretty: bool = True,
        xhtml: bool = False,
    ) -> None:
        self._doctype: str = doctype
        self._pretty: bool = pretty
        self._xhtml: bool = xhtml
        self._html_lang: str | None = html_lang
        self._html_dir: typing.Literal["ltr", "rtl", "auto"] | None = html_dir
        self._head_elements: list[
            title | meta | link | script | style | base | noscript | template | str
        ] = list(head_elements)
        self._pending_body: list[Tag | str] = []
        self._dirty = True

    def add(self, *tags: Tag | str) -> Self:
        self._pending_body.extend(tags)
        self._dirty = True

        return self

    def render(
        self,
        indent_level: int = 0,
        *,
        pretty: bool | None = None,
        xhtml: bool | None = None,
    ) -> str:
        self._ensure_built()

        use_pretty: bool = self._pretty if pretty is None else bool(pretty)
        use_xhtml: bool = self._xhtml if xhtml is None else bool(xhtml)

        sb: list[str] = []
        if self._doctype:
            sb.append(self._doctype)
            if use_pretty:
                sb.append("\n")

        self._root._render(  # noqa: SLF001 # type: ignore TODO: correct it
            sb=sb,
            indent_level=indent_level,
            pretty=use_pretty,
            xhtml=use_xhtml,
        )
        return "".join(sb)

    def __repr__(self) -> str:
        return (
            f"document(doctype={self._doctype!r}, "
            f"pretty={self._pretty}, xhtml={self._xhtml}, "
            f"head_elements={len(self._head_elements)}, "
            f"queued_body={len(self._pending_body)}, dirty={self._dirty})"
        )

    def _ensure_built(self) -> None:
        if not self._dirty and self._root:
            return

        self._head = head(*self._head_elements)
        self._body = body(*self._pending_body)
        self._root = html(
            self._head,
            self._body,
            lang=self._html_lang,
            dir=self._html_dir,
        )
        self._dirty = False
