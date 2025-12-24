from subedit.path_builder import PathBuilder
from subedit.custom_exceptions import UnsupportedAssetError
from subedit.info import Attachment, BasicTrack
from pytest import raises


class FakeSubtitleTrack(BasicTrack):
    def __init__(self):
        ...

    def id(self) -> int:
        return 3

    def uid(self) -> int:
        return 14539514268308361919

    def content_type(self) -> str:
        return "S_TEXT/ASS"

    def file_name(self) -> str:
        return "2_Brazilian_CR_pt-BR.ass"


class FakeAttachment(Attachment):
    def __init__(self):
        ...

    def id(self) -> int:
        return 1

    def uid(self) -> int:
        return 8047349583708614449

    def content_type(self) -> str:
        return "application/x-truetype-font"

    def file_name(self) -> str:
        return "arialbd_3.ttf"


def test_PathBuilder_com_SubtitleTrack():
    expect = 'tracks/2_Brazilian_CR_pt-BR.ass'

    sub = FakeSubtitleTrack()
    path = PathBuilder.builder(sub)
    assert str(path) == expect


def test_PathBuilder_com_Attachmente():
    expect = 'fonts/arialbd_3.ttf'

    sub = FakeAttachment()
    path = PathBuilder.builder(sub)
    assert str(path) == expect


def test_PathBuilder_com_Asset_nao_suportado():
    expect = "Cannot build path for asset of type 'dict'. "\
        "Supported assets: Track, Attachment."
    with raises(UnsupportedAssetError) as excinfo:
        sub = dict()
        PathBuilder.builder(sub)
    result = str(excinfo.value)
    assert result == expect
