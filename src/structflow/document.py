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
from structflow.tags.base import AttributeValue, Container

if typing.TYPE_CHECKING:
    from structflow.tags.base import Tag


class html(Container):
    def __init__(
        self,
        *children: typing.Union[head, body, Tag, str],
        lang: typing.Optional[str] = None,
        dir: typing.Optional[typing.Literal["ltr", "rtl", "auto"]] = None,
        xmlns: typing.Optional[str] = None,
        manifest: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        class_: typing.Optional[typing.Union[str, list[str]]] = None,
        style: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
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
        *head_elements: typing.Union[
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
        doctype: str = "<!DOCTYPE html>",
        html_lang: typing.Optional[str] = None,
        html_dir: typing.Optional[typing.Literal["ltr", "rtl", "auto"]] = None,
        pretty: bool = True,
        xhtml: bool = False,
    ):
        self._doctype: str = doctype
        self._pretty: bool = pretty
        self._xhtml: bool = xhtml
        self._html_lang: typing.Optional[str] = html_lang
        self._html_dir: typing.Optional[typing.Literal["ltr", "rtl", "auto"]] = html_dir
        self._head_elements: list[
            typing.Union[
                title,
                meta,
                link,
                script,
                style,
                base,
                noscript,
                template,
                str,
            ]
        ] = list(head_elements)
        self._pending_body: list[typing.Union[Tag, str]] = []
        self._dirty = True

    def add(self, *tags: typing.Union[Tag, str]):
        self._pending_body.extend(tags)
        self._dirty = True

    def render(
        self,
        pretty: typing.Optional[bool] = None,
        xhtml: typing.Optional[bool] = None,
        indent_level: int = 0,
    ) -> str:
        self._ensure_built()

        use_pretty: bool = self._pretty if pretty is None else bool(pretty)
        use_xhtml: bool = self._xhtml if xhtml is None else bool(xhtml)

        sb: list[str] = []
        if self._doctype:
            sb.append(self._doctype)
            if use_pretty:
                sb.append("\n")

        self._root._render(sb, indent_level, use_pretty, use_xhtml)
        return "".join(sb)

    def __repr__(self) -> str:
        return (
            f"document(doctype={repr(self._doctype)}, "
            f"pretty={self._pretty}, xhtml={self._xhtml}, "
            f"head_elements={len(self._head_elements)}, "
            f"queued_body={len(self._pending_body)}, dirty={self._dirty})"
        )

    def _ensure_built(self):
        if not self._dirty and self._root:
            return

        self._head = head(*self._head_elements)
        self._body = body(*self._pending_body)
        self._root = html(
            self._head, self._body, lang=self._html_lang, dir=self._html_dir
        )
        self._dirty = False
