from subedit.interface import AssetAdapter, Track, TrackAdapter, Asset


class Attachment(Asset):
    def __init__(self, data: AssetAdapter):
        self.__id = data.id()
        self.__uid = data.uid()
        self.__content_type = data.content_type()
        self.__file_name = data.file_name()

    def id(self) -> int:
        return self.__id

    def uid(self) -> int:
        return self.__uid

    def content_type(self) -> str:
        return self.__content_type

    def file_name(self) -> str:
        return self.__file_name


class BasicTrack(Asset):
    def __init__(self, data: TrackAdapter):
        self.__id = data.id()
        self.__uid = data.uid()
        self.__content_type = data.codec_id()
        self.__file_name = data.file_name()

    def id(self) -> int:
        return self.__id

    def uid(self) -> int:
        return self.__uid

    def content_type(self) -> str:
        return self.__content_type

    def file_name(self) -> str:
        return self.__file_name


class AudioTrack(Track):
    def __init__(self, data: TrackAdapter):
        self.__id = data.id()
        self.__uid = data.uid()
        self.__codec = data.codec()
        self.__codec_id = data.codec_id()
        self.__default_track = data.default_track()
        self.__enabled_track = data.enabled_track()
        self.__forced_track = data.forced_track()
        self.__language = data.language()
        self.__language_ietf = data.language_ietf()
        self.__number = data.number()
        self.__track_name = data.track_name()

    def id(self) -> int:
        return self.__id

    def uid(self) -> int:
        return self.__uid

    def codec(self) -> str:
        return self.__codec

    def codec_id(self) -> str:
        return self.__codec_id

    def default_track(self) -> bool:
        return self.__default_track

    def enabled_track(self) -> bool:
        return self.__enabled_track

    def forced_track(self) -> bool:
        return self.__forced_track

    def language(self) -> str:
        return self.__language

    def language_ietf(self) -> str:
        return self.__language_ietf

    def number(self) -> int:
        return self.__number

    def track_name(self) -> str:
        return self.__track_name


class SubtitleTrack(Track):
    def __init__(self, data: TrackAdapter):
        self.__id = data.id()
        self.__uid = data.uid()
        self.__codec = data.codec()
        self.__codec_id = data.codec_id()
        self.__default_track = data.default_track()
        self.__enabled_track = data.enabled_track()
        self.__forced_track = data.forced_track()
        self.__language = data.language()
        self.__language_ietf = data.language_ietf()
        self.__number = data.number()
        self.__track_name = data.track_name()

    def id(self) -> int:
        return self.__id

    def uid(self) -> int:
        return self.__uid

    def codec(self) -> str:
        return self.__codec

    def codec_id(self) -> str:
        return self.__codec_id

    def default_track(self) -> bool:
        return self.__default_track

    def enabled_track(self) -> bool:
        return self.__enabled_track

    def forced_track(self) -> bool:
        return self.__forced_track

    def language(self) -> str:
        return self.__language

    def language_ietf(self) -> str:
        return self.__language_ietf

    def number(self) -> int:
        return self.__number

    def track_name(self) -> str:
        return self.__track_name


class VideoTrack(Track):
    def __init__(self, data: TrackAdapter):
        self.__id = data.id()
        self.__uid = data.uid()
        self.__codec = data.codec()
        self.__codec_id = data.codec_id()
        self.__default_track = data.default_track()
        self.__enabled_track = data.enabled_track()
        self.__forced_track = data.forced_track()
        self.__language = data.language()
        self.__language_ietf = data.language_ietf()
        self.__number = data.number()
        self.__track_name = data.track_name()

    def id(self) -> int:
        return self.__id

    def uid(self) -> int:
        return self.__uid

    def codec(self) -> str:
        return self.__codec

    def codec_id(self) -> str:
        return self.__codec_id

    def default_track(self) -> bool:
        return self.__default_track

    def enabled_track(self) -> bool:
        return self.__enabled_track

    def forced_track(self) -> bool:
        return self.__forced_track

    def language(self) -> str:
        return self.__language

    def language_ietf(self) -> str:
        return self.__language_ietf

    def number(self) -> int:
        return self.__number

    def track_name(self) -> str:
        return self.__track_name
