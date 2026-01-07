from __future__ import annotations
from subedit.media_enums import MediaType


class AssetSelect:
    def __init__(self, uuid, assets):
        self.__assets = assets
        self.__uuid = uuid

    def select(self, media_type) -> AssetSelect:
        assets = {media_type: self.get(media_type)}
        return AssetSelect(self.__uuid, assets)

    def get(self, media_type: MediaType):
        return self.__assets.get(media_type, [])

    def __check_operation(self, other: AssetSelect):
        if self.__uuid != other.__uuid:
            raise ValueError("Cannot combine objects that do not share the same origin")

    def __and__(self, other: AssetSelect) -> AssetSelect:
        self.__check_operation(other)

        assets = {}
        for media_type in MediaType:
            ass = set(self.get(media_type)) & set(other.get(media_type))
            if ass:
                assets[media_type] = list(ass)
        return AssetSelect(self.__uuid, assets)

    def __iand__(self, other: AssetSelect) -> AssetSelect:
        self.__check_operation(other)

        for media_type in MediaType:
            ass = set(self.get(media_type)) & set(other.get(media_type))
            if media_type in self.__assets:
                if ass:
                    self.__assets[media_type] = list(ass)
                else:
                    del self.__assets[media_type]
        return self

    def __or__(self, other: AssetSelect) -> AssetSelect:
        self.__check_operation(other)

        assets = {}
        for media_type in MediaType:
            ass = set(other.get(media_type))
            if media_type in self.__assets:
                ass |= set(self.__assets[media_type])
            if ass:
                assets[media_type] = list(ass)
        return AssetSelect(self.__uuid, assets)

    def __ior__(self, other: AssetSelect) -> AssetSelect:
        self.__check_operation(other)

        for media_type in MediaType:
            ass = set(self.get(media_type)) | set(other.get(media_type))
            self.__assets[media_type] = list(ass)
        return self

    def __sub__(self, other: AssetSelect) -> AssetSelect:
        self.__check_operation(other)

        assets = {}
        for media_type in MediaType:
            ass = set(self.get(media_type)) - set(other.get(media_type))
            if ass:
                assets[media_type] = list(ass)
        return AssetSelect(self.__uuid, assets)

    def __isub__(self, other: AssetSelect) -> AssetSelect:
        self.__check_operation(other)

        for media_type in MediaType:
            ass = set(self.get(media_type)) - set(other.get(media_type))
            self.__assets[media_type] = list(ass)
        return self

    def __xor__(self, other: AssetSelect) -> AssetSelect:
        self.__check_operation(other)

        assets = {}
        for media_type in MediaType:
            ass = set(self.get(media_type)) ^ set(other.get(media_type))
            if ass:
                assets[media_type] = list(ass)
        return AssetSelect(self.__uuid, assets)

    def __ixor__(self, other: AssetSelect) -> AssetSelect:
        self.__check_operation(other)

        for media_type in MediaType:
            ass = set(self.get(media_type)) ^ set(other.get(media_type))
            self.__assets[media_type] = list(ass)
        return self
