from __future__ import annotations
from subedit.media_enums import MediaType, BaseMediaProperty, expand_media_type
from subedit.assets.asset_filter import ASSET_FILTER
from operator import or_, and_, sub, xor
from typing import Iterable


class AssetSelect:
    def __init__(self, uuid, assets):
        self.__assets = {key: asset for key, asset in assets.items() if asset}
        self.__uuid = uuid

    def __check_operation(self, other: AssetSelect):
        if self.__uuid != other.__uuid:
            raise ValueError("Cannot combine objects that do not share the same origin")

    def __get_media_types(self, other: AssetSelect):
        return self.keys() & other.keys()

    def __get_collection_assets(self, other: AssetSelect) -> dict:
        media_types = self.keys() - other.keys()
        collection_assets = {}
        for media_type in media_types:
            collection_assets[media_type] = self[media_type].copy()
        media_types = other.keys() - self.keys()
        for media_type in media_types:
            collection_assets[media_type] = other[media_type].copy()
        return collection_assets

    def __operator(self, other: AssetSelect, operation: callable) -> dict:
        self.__check_operation(other)

        collection_assets = self.__get_collection_assets(other)
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

    def __call__(self, media_types: list[MediaType]):
        assets = {
            media_type: asset.copy()
            for media_type, asset in self.__assets.items()
            if media_type in media_types
        }
        return AssetSelect(self.__uuid, assets)

    def __getitem__(self, media_type: MediaType):
        return self.__assets[media_type]

    def __len__(self) -> int:
        size = 0
        for asset in self.__assets.values():
            size += len(asset)
        return size

    def select(self, media_type) -> AssetSelect:
        assets = {media_type: self.get(media_type)}
        return AssetSelect(self.__uuid, assets)

    def get(self, media_type: MediaType):
        return self.__assets.get(media_type, [])

    def keys(self):
        return self.__assets.keys()

    def where(self, property: BaseMediaProperty, value: bool | str | int | Iterable[bool | str | int]):
        assets = {}
        filter = ASSET_FILTER[property]
        for media_type in expand_media_type(property):
            assets[media_type] = filter(self.get(media_type), value)
        return AssetSelect(self.__uuid, assets)
