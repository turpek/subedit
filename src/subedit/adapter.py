from subedit.interface import AssetAdapter, TrackAdapter
from subedit.utils import TRACKS_SUFFIX


class MKVMergeAttachmentAdapter(AssetAdapter):
    def __init__(self, data: dict):
        super().__init__()
        self.__id = data['id']
        self.__uid = data['properties'].get('uid', 0)
        self.__content_type = data['content_type']
        self.__file_name = data['file_name']

    def id(self) -> int:
        return self.__id

    def uid(self) -> int:
        return self.__uid

    def content_type(self) -> str:
        return self.__content_type

    def file_name(self) -> str:
        return self.__file_name


class MKVMergeTrackAdapter(TrackAdapter):
    def __init__(self, data: dict):
        prop = data.get('properties', {})
        self.__id = data['id']
        self.__codec = data['codec']
        self.__uid = prop.get('uid', 0)
        self.__codec_id = prop.get('codec_id', "")
        self.__default_track = prop.get('default_track', False)
        self.__enabled_track = prop.get('enabled_track', True)
        self.__forced_track = prop.get('forced_track')
        self.__language = prop.get('language', 'und')
        self.__language_ietf = prop.get('language_ietf', 'und')
        self.__number = prop.get('number', 0)
        self.__track_name = prop.get('track_name', "")
        self.__type = data['type']

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

    def type(self) -> str:
        return self.__type


class BasicTrackAdapter(AssetAdapter):
    def __init__(self, track_adapter: TrackAdapter):
        self.__id = track_adapter.id()
        self.__uid = track_adapter.uid()
        self.__content_type = track_adapter.codec_id()

        lang = self.__get_lang(track_adapter)
        suffix = self.__get_suffix(track_adapter)
        track_name = self.__get_track_name(track_adapter)
        self.__file_name = f"{self.id()}_{track_name}_{lang}{suffix}"

    def __get_track_name(self, track_adapter: TrackAdapter):
        return track_adapter.track_name() or "unknown"

    def __get_lang(self, track_adapter: TrackAdapter):
        return track_adapter.language_ietf() or "und"

    def __get_suffix(self, track_adapter: TrackAdapter):
        suffix = TRACKS_SUFFIX.get(track_adapter.codec_id(), "")
        if not suffix:
            raise ValueError(f"Faixa {track_adapter.id()} possui codec_id ausente ou vazio.")
        return suffix

    def id(self):
        return self.__id

    def uid(self):
        return self.__uid

    def content_type(self):
        return self.__content_type

    def file_name(self):
        return self.__file_name
