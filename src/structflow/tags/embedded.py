from __future__ import annotations

import typing

from .base import Container, Void

if typing.TYPE_CHECKING:
    from .base import Tag
    from .types import AttributeValue


class img(Void):
    def __init__(  # noqa: C901
        self,
        *,
        alt: typing.Optional[str] = None,
        src: typing.Optional[str] = None,
        srcset: typing.Optional[typing.Union[str, list[str]]] = None,
        sizes: typing.Optional[str] = None,
        crossorigin: typing.Optional[
            typing.Literal["anonymous", "use-credentials"]
        ] = None,
        usemap: typing.Optional[str] = None,
        ismap: typing.Optional[bool] = None,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        referrerpolicy: typing.Optional[str] = None,
        decoding: typing.Optional[typing.Literal["sync", "async", "auto"]] = None,
        loading: typing.Optional[typing.Literal["eager", "lazy"]] = None,
        fetchpriority: typing.Optional[typing.Literal["high", "low", "auto"]] = None,
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


class picture(Container):
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


class source(Void):
    def __init__(
        self,
        *,
        src: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        srcset: typing.Optional[typing.Union[str, list[str]]] = None,
        sizes: typing.Optional[str] = None,
        media: typing.Optional[str] = None,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
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
        if src is not None:
            self._attributes["src"] = src
        if type is not None:
            self._attributes["type"] = type
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


class track(Void):
    def __init__(
        self,
        *,
        kind: typing.Optional[
            typing.Literal[
                "subtitles", "captions", "descriptions", "chapters", "metadata"
            ]
        ] = None,
        src: typing.Optional[str] = None,
        srclang: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        default: typing.Optional[bool] = None,
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


class audio(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        src: typing.Optional[str] = None,
        preload: typing.Optional[typing.Literal["none", "metadata", "auto"]] = None,
        autoplay: typing.Optional[bool] = None,
        loop: typing.Optional[bool] = None,
        muted: typing.Optional[bool] = None,
        controls: typing.Optional[bool] = None,
        controlslist: typing.Optional[str] = None,
        crossorigin: typing.Optional[
            typing.Literal["anonymous", "use-credentials"]
        ] = None,
        disableremoteplayback: typing.Optional[bool] = None,
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


class video(Container):
    def __init__(  # noqa: C901
        self,
        *children: typing.Union[Tag, str],
        src: typing.Optional[str] = None,
        preload: typing.Optional[typing.Literal["none", "metadata", "auto"]] = None,
        autoplay: typing.Optional[bool] = None,
        loop: typing.Optional[bool] = None,
        muted: typing.Optional[bool] = None,
        controls: typing.Optional[bool] = None,
        controlslist: typing.Optional[str] = None,
        playsinline: typing.Optional[bool] = None,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        poster: typing.Optional[str] = None,
        crossorigin: typing.Optional[
            typing.Literal["anonymous", "use-credentials"]
        ] = None,
        disablepictureinpicture: typing.Optional[bool] = None,
        disableremoteplayback: typing.Optional[bool] = None,
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


class audio_source(audio):
    def __init__(
        self,
        sources: typing.Iterable[source],
        tracks: typing.Optional[typing.Iterable[track]] = None,
        src: typing.Optional[str] = None,
        preload: typing.Optional[typing.Literal["none", "metadata", "auto"]] = None,
        autoplay: typing.Optional[bool] = None,
        loop: typing.Optional[bool] = None,
        muted: typing.Optional[bool] = None,
        controls: typing.Optional[bool] = None,
        controlslist: typing.Optional[str] = None,
        crossorigin: typing.Optional[
            typing.Literal["anonymous", "use-credentials"]
        ] = None,
        disableremoteplayback: typing.Optional[bool] = None,
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
    ):
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
        )


class video_source(video):
    def __init__(
        self,
        sources: typing.Iterable[source],
        tracks: typing.Optional[typing.Iterable[track]] = None,
        src: typing.Optional[str] = None,
        preload: typing.Optional[typing.Literal["none", "metadata", "auto"]] = None,
        autoplay: typing.Optional[bool] = None,
        loop: typing.Optional[bool] = None,
        muted: typing.Optional[bool] = None,
        controls: typing.Optional[bool] = None,
        controlslist: typing.Optional[str] = None,
        playsinline: typing.Optional[bool] = None,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        poster: typing.Optional[str] = None,
        crossorigin: typing.Optional[
            typing.Literal["anonymous", "use-credentials"]
        ] = None,
        disablepictureinpicture: typing.Optional[bool] = None,
        disableremoteplayback: typing.Optional[bool] = None,
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
    ):
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
        )


class embed(Void):
    def __init__(
        self,
        *,
        src: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
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
        if src is not None:
            self._attributes["src"] = src
        if type is not None:
            self._attributes["type"] = type
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height


class iframe(Container):
    def __init__(  # noqa: C901
        self,
        *children: typing.Union[Tag, str],
        src: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        srcdoc: typing.Optional[str] = None,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        allow: typing.Optional[str] = None,
        allowfullscreen: typing.Optional[bool] = None,
        sandbox: typing.Optional[typing.Union[str, list[str]]] = None,
        referrerpolicy: typing.Optional[str] = None,
        loading: typing.Optional[typing.Literal["eager", "lazy"]] = None,
        csp: typing.Optional[str] = None,
        allowpaymentrequest: typing.Optional[bool] = None,
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


class object(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        data: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        usemap: typing.Optional[str] = None,
        typemustmatch: typing.Optional[bool] = None,
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
        if data is not None:
            self._attributes["data"] = data
        if type is not None:
            self._attributes["type"] = type
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


class param(Void):
    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
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
        if name is not None:
            self._attributes["name"] = name
        if value is not None:
            self._attributes["value"] = value


class canvas(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
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
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height


class svg(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        width: typing.Optional[typing.Union[int, str]] = None,
        height: typing.Optional[typing.Union[int, str]] = None,
        viewBox: typing.Optional[str] = None,
        xmlns: typing.Optional[str] = "http://www.w3.org/2000/svg",
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
        if width is not None:
            self._attributes["width"] = width
        if height is not None:
            self._attributes["height"] = height
        if viewBox is not None:
            self._attributes["viewBox"] = viewBox
        if xmlns is not None:
            self._attributes["xmlns"] = xmlns


class map(Container):
    def __init__(
        self,
        *children: typing.Union[Tag, str],
        name: typing.Optional[str] = None,
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
        if name is not None:
            self._attributes["name"] = name


class area(Void):
    def __init__(
        self,
        *,
        alt: typing.Optional[str] = None,
        coords: typing.Optional[str] = None,
        shape: typing.Optional[
            typing.Literal["rect", "circle", "poly", "default"]
        ] = None,
        href: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        download: typing.Optional[typing.Union[str, bool]] = None,
        ping: typing.Optional[typing.Union[str, list[str]]] = None,
        rel: typing.Optional[str] = None,
        referrerpolicy: typing.Optional[str] = None,
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
