from pathlib3x import Path
from pytest import fixture
from subedit.factory import Factory, MKVMergeFactory
from subedit.media_enums import MediaType, Provider
from subprocess import PIPE


@fixture
def mkvmerge_deps(mocker):
    return {
        'AttachmentAdapter': mocker.patch('subedit.factory.MKVMergeAttachmentAdapter'),
        'TrackAdapter': mocker.patch('subedit.factory.MKVMergeTrackAdapter'),
        'Attachment': mocker.patch('subedit.factory.Attachment'),
        'Audio': mocker.patch('subedit.factory.AudioTrack'),
        'Video': mocker.patch('subedit.factory.VideoTrack'),
        'Subtitle': mocker.patch('subedit.factory.SubtitleTrack'),
        'run': mocker.patch('subedit.factory.run'),
        'JSONReader': mocker.patch('subedit.factory.JSONReader'),
    }


@fixture
def mkvmerge_builder(mocker):
    return mocker.patch('subedit.factory.MKVMergeAssetBuilder')
def test_Factory_build_mkvmerge_parse(mocker):
    FakeFactory = mocker.MagicMock()
    mocker.patch.dict(Factory._provider, {Provider.MKVMERGE: FakeFactory})
    Factory.build_parse(Path('video.mkv'), Provider.MKVMERGE)


def test_Factory_build_mkvmerge_parse_build(mocker):
    FakeFactory = mocker.MagicMock()
    fake_factory = mocker.MagicMock()
    FakeFactory.return_value = fake_factory
    mocker.patch.dict(Factory._provider, {Provider.MKVMERGE: FakeFactory})
    Factory.build_parse(Path('video.mkv'), Provider.MKVMERGE)
    fake_factory.build.assert_called()


def test_Factory_build_return(mocker):
    expect = 'asset_builder'
    FakeFactory = mocker.MagicMock()
    fake_factory = mocker.MagicMock()
    fake_factory.build.return_value = expect
    FakeFactory.return_value = fake_factory
    mocker.patch.dict(Factory._provider, {Provider.MKVMERGE: FakeFactory})
    result = Factory.build_parse(Path('video.mkv'), Provider.MKVMERGE)
    assert result == expect


def test_MKVMergeFactory_run_called(mkvmerge_deps, mkvmerge_builder):
    expect_args = ['mkvmerge', '-J', 'video.mkv']
    mkvmerge_factory = MKVMergeFactory(Path('video.mkv'))
    mkvmerge_factory.build()
    args, kwargs = mkvmerge_deps['run'].call_args

    assert args[0] == expect_args
    assert kwargs["stdout"] is PIPE


def test_MKVMergeFactory_register_attachment(mkvmerge_deps, mkvmerge_builder):
    mkvmerge_factory = MKVMergeFactory(Path('video.mkv'))
    asset = mkvmerge_factory.build()
    asset.register_type.assert_any_call(
        mkvmerge_deps['AttachmentAdapter'],
        mkvmerge_deps['Attachment'],
        MediaType.ATTACHMENT
    )


def test_MKVMergeFactory_register_audio(mkvmerge_deps, mkvmerge_builder):
    mkvmerge_factory = MKVMergeFactory(Path('video.mkv'))
    asset = mkvmerge_factory.build()
    asset.register_type.assert_any_call(
        mkvmerge_deps['TrackAdapter'],
        mkvmerge_deps['Audio'],
        MediaType.AUDIO
    )


def test_MKVMergeFactory_register_video(mkvmerge_deps, mkvmerge_builder):
    mkvmerge_factory = MKVMergeFactory(Path('video.mkv'))
    asset = mkvmerge_factory.build()
    asset.register_type.assert_any_call(
        mkvmerge_deps['TrackAdapter'],
        mkvmerge_deps['Video'],
        MediaType.VIDEO
    )


def test_MKVMergeFactory_register_subtitle(mkvmerge_deps, mkvmerge_builder):
    mkvmerge_factory = MKVMergeFactory(Path('video.mkv'))
    asset = mkvmerge_factory.build()
    asset.register_type.assert_any_call(
        mkvmerge_deps['TrackAdapter'],
        mkvmerge_deps['Subtitle'],
        MediaType.SUBTITLE
    )
