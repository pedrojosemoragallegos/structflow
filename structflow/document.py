from __future__ import annotations

import typing

from .tags.base import Container

if typing.TYPE_CHECKING:
    from .tags.base import Tag


class html(Container): ...


class body(Container): ...


class head(Container): ...


class Document:
    def __init__(
        self,
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
        self._pending_head: list[typing.Union[Tag, str]] = []
        self._pending_body: list[typing.Union[Tag, str]] = []
        self._head: typing.Optional[head] = None
        self._body: typing.Optional[body] = None
        self._root: typing.Optional[html] = None
        self._dirty = True

    def add_head(self, *tags: typing.Union[Tag, str]):
        self._pending_head.extend(tags)
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

        self._root._render(
            sb, indent_level, use_pretty, use_xhtml
        )  # TODO add a public function in the Tag class
        return "".join(sb)

    def __repr__(self) -> str:
        return (
            f"document(doctype={repr(self._doctype)}, "
            f"pretty={self._pretty}, xhtml={self._xhtml}, "
            f"queued_head={len(self._pending_head)}, "
            f"queued_body={len(self._pending_body)}, dirty={self._dirty})"
        )

    def _ensure_built(self):
        if not self._dirty and self._root is not None:
            return

        self._head: head = head(*self._pending_head)
        self._body: body = body(*self._pending_body)
        self._root: html = html(
            self._head, self._body, lang=self._html_lang, dir=self._html_dir
        )
        self._dirty = False
