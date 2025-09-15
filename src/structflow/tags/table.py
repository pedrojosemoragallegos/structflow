from __future__ import annotations

import typing

from .base import Container, Void

if typing.TYPE_CHECKING:
    from .types import AttributeValue


class table(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: caption | colgroup | thead | tbody | tfoot | tr | str,
        summary: str | None = None,
        border: int | None = None,
        cellpadding: int | str | None = None,
        cellspacing: int | str | None = None,
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
        if summary is not None:
            self._attributes["summary"] = summary
        if border is not None:
            self._attributes["border"] = border
        if cellpadding is not None:
            self._attributes["cellpadding"] = cellpadding
        if cellspacing is not None:
            self._attributes["cellspacing"] = cellspacing


class caption(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: str | table,
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


class colgroup(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: col | str,
        span: int | None = None,
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
        if span is not None:
            self._attributes["span"] = span


class col(Void):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        span: int | None = None,
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
        if span is not None:
            self._attributes["span"] = span


class thead(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: tr | str,
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


class tbody(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: tr | str,
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


class tfoot(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: tr | str,
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


class tr(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: td | th | str,
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


class th(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: str | table,
        colspan: int | None = None,
        rowspan: int | None = None,
        headers: str | None = None,
        scope: typing.Literal["row", "col", "rowgroup", "colgroup", "auto"]
        | None = None,
        abbr: str | None = None,
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
        if colspan is not None:
            self._attributes["colspan"] = colspan
        if rowspan is not None:
            self._attributes["rowspan"] = rowspan
        if headers is not None:
            self._attributes["headers"] = headers
        if scope is not None:
            self._attributes["scope"] = scope
        if abbr is not None:
            self._attributes["abbr"] = abbr


class td(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: str | table,
        colspan: int | None = None,
        rowspan: int | None = None,
        headers: str | None = None,
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
        if colspan is not None:
            self._attributes["colspan"] = colspan
        if rowspan is not None:
            self._attributes["rowspan"] = rowspan
        if headers is not None:
            self._attributes["headers"] = headers
