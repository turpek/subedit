from subedit.interface import AssetAdapter, ITrack as Track, TrackAdapter, Asset


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

