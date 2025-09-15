from __future__ import annotations

import typing

from .base import Container, Void

if typing.TYPE_CHECKING:
    from .base import Tag
    from .types import AttributeValue


class img(Void):  # noqa: N801
    def __init__(  # noqa: C901, PLR0912, PLR0913
        self,
        *,
        alt: str | None = None,
        src: str | None = None,
        srcset: str | list[str] | None = None,
        sizes: str | None = None,
        crossorigin: typing.Literal["anonymous", "use-credentials"] | None = None,
        usemap: str | None = None,
        ismap: bool | None = None,
        width: int | None = None,
        height: int | None = None,
        referrerpolicy: str | None = None,
        decoding: typing.Literal["sync", "async", "auto"] | None = None,
        loading: typing.Literal["eager", "lazy"] | None = None,
        fetchpriority: typing.Literal["high", "low", "auto"] | None = None,
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
        if alt is not None:
            self._attributes["alt"] = alt
        if src is not None:
            self._attributes["src"] = src
        if srcset is not None:
            if isinstance(srcset, list):
                self._attributes["srcset"] = ", ".join(srcset)
            else:
                self._attributes["srcset"] = srcset
        if sizes is not None:
            self._attributes["sizes"] = sizes
        if crossorigin is not None:
            self._attributes["crossorigin"] = crossorigin
        if usemap is not None:
            self._attributes["usemap"] = usemap
        if ismap is not None:
            self._attributes["ismap"] = ismap
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
        if decoding is not None:
            self._attributes["decoding"] = decoding
        if loading is not None:
            self._attributes["loading"] = loading
        if fetchpriority is not None:
            self._attributes["fetchpriority"] = fetchpriority


class picture(Container):  # noqa: N801
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


class source(Void):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        src: str | None = None,
        type_: str | None = None,
        srcset: str | list[str] | None = None,
        sizes: str | None = None,
        media: str | None = None,
        width: int | None = None,
        height: int | None = None,
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
        if src is not None:
            self._attributes["src"] = src
        if type_ is not None:
            self._attributes["type"] = type_
        if srcset is not None:
            if isinstance(srcset, list):
                self._attributes["srcset"] = ", ".join(srcset)
            else:
                self._attributes["srcset"] = srcset
        if sizes is not None:
            self._attributes["sizes"] = sizes
        if media is not None:
            self._attributes["media"] = media
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height


class track(Void):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        kind: typing.Literal[
            "subtitles",
            "captions",
            "descriptions",
            "chapters",
            "metadata",
        ]
        | None = None,
        src: str | None = None,
        srclang: str | None = None,
        label: str | None = None,
        default: bool | None = None,
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
        if kind is not None:
            self._attributes["kind"] = kind
        if src is not None:
            self._attributes["src"] = src
        if srclang is not None:
            self._attributes["srclang"] = srclang
        if label is not None:
            self._attributes["label"] = label
        if default is not None:
            self._attributes["default"] = default


class audio(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: Tag | str,
        src: str | None = None,
        preload: typing.Literal["none", "metadata", "auto"] | None = None,
        autoplay: bool | None = None,
        loop: bool | None = None,
        muted: bool | None = None,
        controls: bool | None = None,
        controlslist: str | None = None,
        crossorigin: typing.Literal["anonymous", "use-credentials"] | None = None,
        disableremoteplayback: bool | None = None,
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
        if src is not None:
            self._attributes["src"] = src
        if preload is not None:
            self._attributes["preload"] = preload
        if autoplay is not None:
            self._attributes["autoplay"] = autoplay
        if loop is not None:
            self._attributes["loop"] = loop
        if muted is not None:
            self._attributes["muted"] = muted
        if controls is not None:
            self._attributes["controls"] = controls
        if controlslist is not None:
            self._attributes["controlslist"] = controlslist
        if crossorigin is not None:
            self._attributes["crossorigin"] = crossorigin
        if disableremoteplayback is not None:
            self._attributes["disableremoteplayback"] = disableremoteplayback


class video(Container):  # noqa: N801
    def __init__(  # noqa: C901, PLR0912, PLR0913
        self,
        *children: Tag | str,
        src: str | None = None,
        preload: typing.Literal["none", "metadata", "auto"] | None = None,
        autoplay: bool | None = None,
        loop: bool | None = None,
        muted: bool | None = None,
        controls: bool | None = None,
        controlslist: str | None = None,
        playsinline: bool | None = None,
        width: int | None = None,
        height: int | None = None,
        poster: str | None = None,
        crossorigin: typing.Literal["anonymous", "use-credentials"] | None = None,
        disablepictureinpicture: bool | None = None,
        disableremoteplayback: bool | None = None,
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
        if src is not None:
            self._attributes["src"] = src
        if preload is not None:
            self._attributes["preload"] = preload
        if autoplay is not None:
            self._attributes["autoplay"] = autoplay
        if loop is not None:
            self._attributes["loop"] = loop
        if muted is not None:
            self._attributes["muted"] = muted
        if controls is not None:
            self._attributes["controls"] = controls
        if controlslist is not None:
            self._attributes["controlslist"] = controlslist
        if playsinline is not None:
            self._attributes["playsinline"] = playsinline
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height
        if poster is not None:
            self._attributes["poster"] = poster
        if crossorigin is not None:
            self._attributes["crossorigin"] = crossorigin
        if disablepictureinpicture is not None:
            self._attributes["disablepictureinpicture"] = disablepictureinpicture
        if disableremoteplayback is not None:
            self._attributes["disableremoteplayback"] = disableremoteplayback


class audio_source(audio):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        sources: typing.Iterable[source],
        tracks: typing.Iterable[track] | None = None,
        src: str | None = None,
        preload: typing.Literal["none", "metadata", "auto"] | None = None,
        autoplay: bool | None = None,
        loop: bool | None = None,
        muted: bool | None = None,
        controls: bool | None = None,
        controlslist: str | None = None,
        crossorigin: typing.Literal["anonymous", "use-credentials"] | None = None,
        disableremoteplayback: bool | None = None,
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
    ) -> None:
        children: list[Tag] = []
        children.extend(sources)
        if tracks:
            children.extend(tracks)

        super().__init__(
            *children,
            src=src,
            preload=preload,
            autoplay=autoplay,
            loop=loop,
            muted=muted,
            controls=controls,
            controlslist=controlslist,
            crossorigin=crossorigin,
            disableremoteplayback=disableremoteplayback,
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
        )


class video_source(video):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        sources: typing.Iterable[source],
        tracks: typing.Iterable[track] | None = None,
        src: str | None = None,
        preload: typing.Literal["none", "metadata", "auto"] | None = None,
        autoplay: bool | None = None,
        loop: bool | None = None,
        muted: bool | None = None,
        controls: bool | None = None,
        controlslist: str | None = None,
        playsinline: bool | None = None,
        width: int | None = None,
        height: int | None = None,
        poster: str | None = None,
        crossorigin: typing.Literal["anonymous", "use-credentials"] | None = None,
        disablepictureinpicture: bool | None = None,
        disableremoteplayback: bool | None = None,
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
    ) -> None:
        children: list[Tag] = []
        children.extend(sources)
        if tracks:
            children.extend(tracks)

        super().__init__(
            *children,
            src=src,
            preload=preload,
            autoplay=autoplay,
            loop=loop,
            muted=muted,
            controls=controls,
            controlslist=controlslist,
            playsinline=playsinline,
            width=width,
            height=height,
            poster=poster,
            crossorigin=crossorigin,
            disablepictureinpicture=disablepictureinpicture,
            disableremoteplayback=disableremoteplayback,
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
        )


class embed(Void):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        src: str | None = None,
        type_: str | None = None,
        width: int | None = None,
        height: int | None = None,
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
        if src is not None:
            self._attributes["src"] = src
        if type_ is not None:
            self._attributes["type"] = type_
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height


class iframe(Container):  # noqa: N801
    def __init__(  # noqa: C901, PLR0913
        self,
        *children: Tag | str,
        src: str | None = None,
        name: str | None = None,
        srcdoc: str | None = None,
        width: int | None = None,
        height: int | None = None,
        allow: str | None = None,
        allowfullscreen: bool | None = None,
        sandbox: str | list[str] | None = None,
        referrerpolicy: str | None = None,
        loading: typing.Literal["eager", "lazy"] | None = None,
        csp: str | None = None,
        allowpaymentrequest: bool | None = None,
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
        if src is not None:
            self._attributes["src"] = src
        if name is not None:
            self._attributes["name"] = name
        if srcdoc is not None:
            self._attributes["srcdoc"] = srcdoc
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height
        if allow is not None:
            self._attributes["allow"] = allow
        if allowfullscreen is not None:
            self._attributes["allowfullscreen"] = allowfullscreen
        if sandbox is not None:
            self._attributes["sandbox"] = (
                " ".join(sandbox) if isinstance(sandbox, list) else sandbox
            )
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
        if loading is not None:
            self._attributes["loading"] = loading
        if csp is not None:
            self._attributes["csp"] = csp
        if allowpaymentrequest is not None:
            self._attributes["allowpaymentrequest"] = allowpaymentrequest


class object_(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: Tag | str,
        data: str | None = None,
        type_: str | None = None,
        name: str | None = None,
        form: str | None = None,
        width: int | None = None,
        height: int | None = None,
        usemap: str | None = None,
        typemustmatch: bool | None = None,
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
        if data is not None:
            self._attributes["data"] = data
        if type_ is not None:
            self._attributes["type"] = type_
        if name is not None:
            self._attributes["name"] = name
        if form is not None:
            self._attributes["form"] = form
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height
        if usemap is not None:
            self._attributes["usemap"] = usemap
        if typemustmatch is not None:
            self._attributes["typemustmatch"] = typemustmatch


class param(Void):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        name: str | None = None,
        value: str | None = None,
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
        if name is not None:
            self._attributes["name"] = name
        if value is not None:
            self._attributes["value"] = value


class canvas(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: Tag | str,
        width: int | None = None,
        height: int | None = None,
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
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height


class svg(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: Tag | str,
        width: int | str | None = None,
        height: int | str | None = None,
        viewBox: str | None = None,  # noqa: N803
        xmlns: str | None = "http://www.w3.org/2000/svg",
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
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height
        if viewBox is not None:
            self._attributes["viewBox"] = viewBox
        if xmlns is not None:
            self._attributes["xmlns"] = xmlns


class map_(Container):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *children: Tag | str,
        name: str | None = None,
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
        if name is not None:
            self._attributes["name"] = name


class area(Void):  # noqa: N801
    def __init__(  # noqa: PLR0913
        self,
        *,
        alt: str | None = None,
        coords: str | None = None,
        shape: typing.Literal["rect", "circle", "poly", "default"] | None = None,
        href: str | None = None,
        target: str | None = None,
        download: str | bool | None = None,
        ping: str | list[str] | None = None,
        rel: str | None = None,
        referrerpolicy: str | None = None,
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
        if alt is not None:
            self._attributes["alt"] = alt
        if coords is not None:
            self._attributes["coords"] = coords
        if shape is not None:
            self._attributes["shape"] = shape
        if href is not None:
            self._attributes["href"] = href
        if target is not None:
            self._attributes["target"] = target
        if download is not None:
            self._attributes["download"] = download
        if ping is not None:
            self._attributes["ping"] = (
                " ".join(ping) if isinstance(ping, list) else ping
            )
        if rel is not None:
            self._attributes["rel"] = rel
        if referrerpolicy is not None:
            self._attributes["referrerpolicy"] = referrerpolicy
