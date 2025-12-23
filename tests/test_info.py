from subedit.info import Attachment, SubtitleTrack
from subedit.interface import IAttachmentAdapter, ITrackAdapter


class FakeAttachment(IAttachmentAdapter):

    def __init__(self, data: dict):
        super().__init__()
        self.__id = 1
        self.__uid = 8047349583708614449
        self.__file_name = "arialbd_3.ttf"
        self.__content_type = "application/x-truetype-font"

    def id(self) -> int:
        return self.__id

    def uid(self) -> int:
        return self.__uid

    def content_type(self) -> str:
        return self.__content_type

    def file_name(self) -> str:
        return self.__file_name


class FakeSubtitleTrack(ITrackAdapter):
    def __init__(self, data: dict):
        ...

    def id(self) -> int:
        return 3

    def uid(self) -> int:
        return 14539514268308361919

    def codec(self) -> str:
        return "SubStationAlpha"

    def codec_id(self) -> str:
        return "S_TEXT/ASS"

    def default_track(self) -> bool:
        return False

    def enabled_track(self) -> bool:
        return True

    def forced_track(self) -> bool:
        return False

    def language(self) -> str:
        return 'por'

    def language_ietf(self) -> str:
        return 'pt-BR'

    def number(self) -> int:
        return 4

    def track_name(self) -> str:
        return 'Brazilian_CR'

    def type(self) -> str:
        return 'subtitles'


def test_Attachment_id():
    attach = Attachment(FakeAttachment({}))
    assert attach.id() == 1


def test_Attachment_uid():
    attach = Attachment(FakeAttachment({}))
    assert attach.uid() == 8047349583708614449


def test_Attachment_file_name():
    attach = Attachment(FakeAttachment({}))
    assert attach.file_name() == 'arialbd_3.ttf'


def test_Attachment_content_type():
    attach = Attachment(FakeAttachment({}))
    assert attach.content_type() == "application/x-truetype-font"


def test_SubtitleTrack_id():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.id() == 3


def test_SubtitleTrack_uid():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.uid() == 14539514268308361919


def test_SubtitleTrack_codec():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.codec() == "SubStationAlpha"


def test_SubtitleTrack_codec_id():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.codec_id() == "S_TEXT/ASS"


def test_SubtitleTrack_default_track():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.default_track() is False


def test_SubtitleTrack_enable_track():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.enabled_track() is True


def test_SubtitleTrack_forced_track():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.forced_track() is False


def test_SubtitleTrack_language():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.language() == 'por'


def test_SubtitleTrack_language_ietf():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.language_ietf() == 'pt-BR'


def test_SubtitleTrack_number():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.number() == 4


def test_SubtitleTrack_track_name():
    track = SubtitleTrack(FakeSubtitleTrack({}))
    assert track.track_name() == 'Brazilian_CR'
