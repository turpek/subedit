from subedit.asset_builder import MKVMergeAssetBuilder
from pytest import raises


class FakeAttachmentAdapter:
    def __init__(self, data: dict):
        ...


class FakeAttachment:
    def __init__(self, data: dict):
        ...


class FakeTrackAdapter:
    def __init__(self, data: dict):
        ...


class FakeTrack:
    def __init__(self, data: dict):
        ...


def test_MKVMergeAssetBuilder_get_audio_data_empty():
    expect = 0
    data = {}
    asset = MKVMergeAssetBuilder(data)
    asset.register_type(FakeTrackAdapter, FakeTrack, 'audio')
    asset.build()
    result = len(asset.get('audio'))
    assert result == expect


def test_MKVMergeAssetBuilder_get_audio_track():
    expect = 1
    data = {'tracks': [{'type': 'audio'}]}
    asset = MKVMergeAssetBuilder(data)
    asset.register_type(FakeTrackAdapter, FakeTrack, 'audio')
    asset.build()
    result = len(asset.get('audio'))
    assert result == expect


def test_MKVMergeAssetBuilder_get_audio_tracks():
    expect = 2
    data = {'tracks': [{'type': 'audio'}, {'type': 'audio'}]}
    asset = MKVMergeAssetBuilder(data)
    asset.register_type(FakeTrackAdapter, FakeTrack, 'audio')
    asset.build()
    result = len(asset.get('audio'))
    assert result == expect


def test_MKVMergeAssetBuilder_get_audio_track_empty():
    expect = 0
    data = {'tracks': [{'type': 'video'}]}
    asset = MKVMergeAssetBuilder(data)
    asset.register_type(FakeTrackAdapter, FakeTrack, 'audio')
    asset.build()
    result = len(asset.get('audio'))
    assert result == expect


def test_MKVMergeAssetBuilder_get_audio_track_no_register():
    expect = 0
    data = {'tracks': [{'type': 'video'}]}
    asset = MKVMergeAssetBuilder(data)
    asset.build()
    result = len(asset.get('audio'))
    assert result == expect


def test_MKVMergeAssetBuilder_get_attachment():
    expect = 1
    data = {'attachments': [{"content_type": "application/x-truetype-font"}]}
    asset = MKVMergeAssetBuilder(data)
    asset.register_type(FakeAttachmentAdapter, FakeAttachment, 'attachments')
    asset.build()
    result = len(asset.get('attachments'))
    assert result == expect


def test_MKVMergeAssetBuilder_build_called_twice_raises():
    expect = "AssetBuilder.build() called more than once"
    with raises(RuntimeError) as excinfo:
        data = {'attachments': [{"content_type": "application/x-truetype-font"}]}
        asset = MKVMergeAssetBuilder(data)
        asset.register_type(FakeAttachmentAdapter, FakeAttachment, 'attachments')
        asset.build()
        asset.build()
    result = str(excinfo.value)
    assert result == expect


def test_MKVMergeAssetBuilder_AttachmentAdapter_called(mocker):
    data = {'attachments': [{"content_type": "application/x-truetype-font"}]}
    FakeAdapter = mocker.MagicMock()
    asset = MKVMergeAssetBuilder(data)
    asset.register_type(FakeAdapter, FakeAttachment, 'attachments')
    asset.build()
    assert FakeAdapter.called is True


def test_MKVMergeAssetBuilder_Attachment_called(mocker):
    data = {'attachments': [{"content_type": "application/x-truetype-font"}]}
    FakeAttachment = mocker.MagicMock()
    asset = MKVMergeAssetBuilder(data)
    asset.register_type(FakeAttachmentAdapter, FakeAttachment, 'attachments')
    asset.build()
    assert FakeAttachment.called is True


def test_MKVMergeAssetBuilder_Attachment_not_called(mocker):
    data = {}
    FakeAttachment = mocker.MagicMock()
    asset = MKVMergeAssetBuilder(data)
    asset.register_type(FakeAttachmentAdapter, FakeAttachment, 'attachments')
    asset.build()
    assert FakeAttachment.called is False
