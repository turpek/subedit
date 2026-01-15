from subedit.asset_builder import MKVMergeAssetBuilder
from subedit.factory import AssetBuilderFactory
from subedit.media_enums import Provider
from pathlib3x import Path
from pytest import fixture
from tests.data import MKVMERGE_DATA


@fixture
def mkvmerge_deps(mocker):
    return {
        'run': mocker.patch('subedit.factory.run'),
        'JSONReader': mocker.patch('subedit.factory.JSONReader'),
    }


def test_integration_AssetBuilderFactory(mkvmerge_deps):
    reader = mkvmerge_deps['JSONReader']
    reader.read.return_value = MKVMERGE_DATA
    asset_builder = AssetBuilderFactory.from_path(Path('video.mkv'), Provider.MKVMERGE)
    assert isinstance(asset_builder, MKVMergeAssetBuilder)
