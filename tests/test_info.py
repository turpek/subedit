from subedit.info import Attachment, SubtitleTrack, VideoTrack
from subedit.interface import IAttachmentAdapter, ITrackAdapter
from pytest import fixture
from tests.data import MKVMERGE_DATA


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


class FakeTrackAdapter(ITrackAdapter):
    def __init__(self, data: dict):
        prop = data['properties']
        self.__id = data['id']
        self.__codec = data['codec']
        self.__uid = prop['uid']
        self.__codec_id = prop['codec_id']
        self.__default_track = prop['default_track']
        self.__enabled_track = prop['enabled_track']
        self.__forced_track = prop['forced_track']
        self.__language = prop['language']
        self.__language_ietf = prop['language_ietf']
        self.__number = prop['number']
        self.__track_name = prop['track_name']
        self.__type = data['type']

    def id(self) -> int:
        return self.__id

    def uid(self) -> int:
        return self.__uid

    def codec(self) -> str:
        return self.__codec

    def codec_id(self) -> str:
        return self.__codec_id

    def default_track(self) -> bool:
        return self.__default_track

    def enabled_track(self) -> bool:
        return self.__enabled_track

    def forced_track(self) -> bool:
        return self.__forced_track

    def language(self) -> str:
        return self.__language

    def language_ietf(self) -> str:
        return self.__language_ietf

    def number(self) -> int:
        return self.__number

    def track_name(self) -> str:
        return self.__track_name

    def type(self) -> str:
        return self.__type


@fixture
def sub_track():
    data = MKVMERGE_DATA['tracks'][3]
    yield FakeTrackAdapter(data)


@fixture
def video_track():
    data = MKVMERGE_DATA['tracks'][0]
    yield FakeTrackAdapter(data)


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


def test_SubtitleTrack_id(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.id() == 3


def test_SubtitleTrack_uid(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.uid() == 14539514268308361919


def test_SubtitleTrack_codec(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.codec() == "SubStationAlpha"


def test_SubtitleTrack_codec_id(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.codec_id() == "S_TEXT/ASS"


def test_SubtitleTrack_default_track(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.default_track() is False


def test_SubtitleTrack_enable_track(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.enabled_track() is True


def test_SubtitleTrack_forced_track(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.forced_track() is False


def test_SubtitleTrack_language(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.language() == 'por'


def test_SubtitleTrack_language_ietf(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.language_ietf() == 'pt-BR'


def test_SubtitleTrack_number(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.number() == 4


def test_SubtitleTrack_track_name(sub_track):
    track = SubtitleTrack(sub_track)
    assert track.track_name() == 'Brazilian_CR'


def test_VideoTrack_id(video_track):
    track = VideoTrack(video_track)
    assert track.id() == 0


def test_VideoTrack_uid(video_track):
    track = VideoTrack(video_track)
    assert track.uid() == 337073230518517163


def test_VideoTrack_codec(video_track):
    track = VideoTrack(video_track)
    assert track.codec() == "AVC/H.264/MPEG-4p10"


def test_VideoTrack_codec_id(video_track):
    track = VideoTrack(video_track)
    assert track.codec_id() == "V_MPEG4/ISO/AVC"


def test_VideoTrack_default_track(video_track):
    track = VideoTrack(video_track)
    assert track.default_track() is True


def test_VideoTrack_enable_track(video_track):
    track = VideoTrack(video_track)
    assert track.enabled_track() is True


def test_VideoTrack_forced_track(video_track):
    track = VideoTrack(video_track)
    assert track.forced_track() is False


def test_VideoTrack_language(video_track):
    track = VideoTrack(video_track)
    assert track.language() == 'jpn'


def test_VideoTrack_language_ietf(video_track):
    track = VideoTrack(video_track)
    assert track.language_ietf() == 'ja'


def test_VideoTrack_number(video_track):
    track = VideoTrack(video_track)
    assert track.number() == 1


def test_VideoTrack_track_name(video_track):
    track = VideoTrack(video_track)
    assert track.track_name() == '[Erai-raws]_AVC_CR'
