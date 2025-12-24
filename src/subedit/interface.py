from abc import ABC, abstractmethod
from typing import Union, Dict


class Asset(ABC):

    @abstractmethod
    def id(self):
        ...

    @abstractmethod
    def uid(self) -> int:
        ...

    @abstractmethod
    def content_type(self) -> str:
        ...

    @abstractmethod
    def file_name(self) -> str:
        ...


class ITrack(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def id(self) -> int:
        ...

    @abstractmethod
    def uid(self) -> int:
        ...

    @abstractmethod
    def codec(self) -> str:
        ...

    @abstractmethod
    def codec_id(self) -> str:
        ...

    @abstractmethod
    def default_track(self) -> bool:
        ...

    @abstractmethod
    def enabled_track(self) -> bool:
        ...

    @abstractmethod
    def forced_track(self) -> bool:
        ...

    @abstractmethod
    def language(self) -> str:
        ...

    @abstractmethod
    def language_ietf(self) -> str:
        ...

    @abstractmethod
    def number(self) -> int:
        ...

    @abstractmethod
    def track_name(self) -> str:
        ...


class AssetAdapter(ABC):

    @abstractmethod
    def id(self):
        ...

    @abstractmethod
    def uid(self) -> int:
        ...

    @abstractmethod
    def content_type(self) -> str:
        ...

    @abstractmethod
    def file_name(self) -> str:
        ...


class TrackAdapter(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def id(self) -> int:
        ...

    @abstractmethod
    def uid(self) -> int:
        ...

    @abstractmethod
    def codec(self) -> str:
        ...

    @abstractmethod
    def codec_id(self) -> str:
        ...

    @abstractmethod
    def default_track(self) -> bool:
        ...

    @abstractmethod
    def enabled_track(self) -> bool:
        ...

    @abstractmethod
    def forced_track(self) -> bool:
        ...

    @abstractmethod
    def language(self) -> str:
        ...

    @abstractmethod
    def language_ietf(self) -> str:
        ...

    @abstractmethod
    def number(self) -> int:
        ...

    @abstractmethod
    def track_name(self) -> str:
        ...

    @abstractmethod
    def type(self) -> str:
        ...


class IDataReader(ABC):
    @abstractmethod
    def read(self, source: Union[str, bytes, Dict]):
        ...


class IDataWriter(ABC):
    @abstractmethod
    def write(self, file_path: str, data):
        ...
