from __future__ import annotations
from subedit.media_enums import MediaType
from operator import or_, and_, sub, xor


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

    def __get_media_types(self, other: AssetSelect):
        return set(self.__assets.keys()) | set(other.__assets.keys())

    def __operator(self, other: AssetSelect, operation: callable) -> dict:
        self.__check_operation(other)

        collection_assets = {}
        media_types = self.__get_media_types(other)
        for media_type in media_types:
            assets = operation(set(self.get(media_type)), set(other.get(media_type)))
            collection_assets[media_type] = list(assets)
        return collection_assets

    def __and__(self, other: AssetSelect) -> AssetSelect:
        return AssetSelect(self.__uuid, self.__operator(other, and_))

    def __iand__(self, other: AssetSelect) -> AssetSelect:
        self.__assets = self.__operator(other, and_)
        return self

    def __or__(self, other: AssetSelect) -> AssetSelect:
        return AssetSelect(self.__uuid, self.__operator(other, or_))

    def __ior__(self, other: AssetSelect) -> AssetSelect:
        self.__assets = self.__operator(other, or_)
        return self

    def __sub__(self, other: AssetSelect) -> AssetSelect:
        return AssetSelect(self.__uuid, self.__operator(other, sub))

    def __isub__(self, other: AssetSelect) -> AssetSelect:
        self.__assets = self.__operator(other, sub)
        return self

    def __xor__(self, other: AssetSelect) -> AssetSelect:
        return AssetSelect(self.__uuid, self.__operator(other, xor))

    def __ixor__(self, other: AssetSelect) -> AssetSelect:
        self.__assets = self.__operator(other, xor)
        return self
