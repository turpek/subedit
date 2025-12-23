from subedit.interface import IAttachmentAdapter, ITrackAdapter

class MKVMergeAttachmentAdapter(IAttachmentAdapter):
    def __init__(self, data: dict):
        super().__init__()
        self.__id = data['id']
        self.__uid = data['properties'].get('uid')
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


class MKVMergeTrackAdapter(ITrackAdapter):
    def __init__(self, data: dict):
        prop = data['properties']
        self.__id = data['id']
        self.__codec = data['codec']
        self.__uid = prop['uid']
        self.__codec_id = prop['codec_id']
        self.__default_track = prop['default_track']
        self.__enabled_track = prop['enabled_track']
        self.__forced_track = prop['forced_track']
        self.__language = prop['language']
        self.__language_ietf = prop['language_ietf']
        self.__number = prop['number']
        self.__track_name = prop['track_name']
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
