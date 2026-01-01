from loguru import logger
from subedit.adapter import AssetAdapter
from subedit.assets import Asset
from subedit.media_enums import MediaType


class MKVMergeAssetBuilder:
    def __init__(self, data: dict):
        self._factories = {}
        self._assets = {}
        self._data = data
        self._build_called = False

    def __build(self, item: dict, media_type: MediaType) -> None:
        factory = self._factories.get(media_type)
        if not factory:
            logger.warning(f"Media type '{media_type}' not registered")
        else:
            asset = factory(item)
            self._assets.get(media_type).append(asset)

    def __build_tracks(self):
        for track_item in self._data.get('tracks', []):
            try:
                media_type = MediaType(track_item['type'])
                self.__build(track_item, media_type)
            except ValueError:
                logger.warning(f"Unknown track type '{track_item["type"]}'")

    def __build_attachments(self):
        for attach_item in self._data.get('attachments', []):
            media_type = MediaType.ATTACHMENT
            self.__build(attach_item, media_type)

    def build(self):
        if self._build_called:
            raise RuntimeError('AssetBuilder.build() called more than once')

        self.__build_tracks()
        self.__build_attachments()
        self._build_called = True

    def register_type(self, adapter_cls: AssetAdapter, asset_cls: Asset, media_type: MediaType) -> None:
        self._factories[media_type] = lambda data: asset_cls(adapter_cls(data))
        self._assets.setdefault(media_type, [])

    def get(self, media_type: MediaType):
        return self._assets.get(media_type, [])
