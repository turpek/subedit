from loguru import logger
from subedit.adapter import AssetAdapter
from subedit.assets import Asset


class MKVMergeAssetBuilder:
    def __init__(self, data: dict):
        self._factories = {}
        self._assets = {}
        self._data = data
        self._build_called = False

    def build(self):

        if self._build_called:
            raise RuntimeError('AssetBuilder.build() called more than once')

        for track_item in self._data.get('tracks', []):
            type_ = track_item['type']
            factory = self._factories.get(type_)
            if not factory:
                logger.warning(f"Track type '{type_}' not registered")
                continue
            asset = factory(track_item)
            self._assets.get(type_).append(asset)

        for attach_item in self._data.get('attachments', []):
            factory = self._factories.get('attachments')
            if not factory:
                logger.warning("Attachment type 'attachments' not registered")
                break
            attach = factory(attach_item)
            self._assets.get('attachments').append(attach)

        self._build_called = True

    def register_type(self, adapter_cls: AssetAdapter, asset_cls: Asset, type_: str) -> None:
        self._factories[type_] = lambda data: asset_cls(adapter_cls(data))
        self._assets.setdefault(type_, [])

    def get(self, type_: str):
        return self._assets.get(type_, [])
