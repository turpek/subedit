from pathlib3x import Path
from subedit.custom_exceptions import UnsupportedAssetError
from subedit.interface import Asset
from subedit.info import Attachment, BasicTrack


class PathBuilder:

    @staticmethod
    def builder(asset: Asset) -> Path:

        if isinstance(asset, BasicTrack):
            path = Path('tracks')
        elif isinstance(asset, Attachment):
            path = Path('fonts')
        else:
            asset_type = type(asset).__name__
            raise UnsupportedAssetError(
                f"Cannot build path for asset of type '{asset_type}'. "
                "Supported assets: Track, Attachment."
            )

        return path / asset.file_name()
