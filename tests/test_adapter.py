from subedit.adapter import MKVMergeAttachmentAdapter, MKVMergeTrackAdapter, BasicTrackAdapter
from subedit.interface import TrackAdapter
from pytest import fixture
from pytest import raises


class FakeTrackAdapter(TrackAdapter):
    def __init__(self, data: dict):
        ...

    def id(self) -> int:
        return 3

    def uid(self) -> int:
        return 14539514268308361919

    def codec_id(self) -> str:
        return "S_TEXT/ASS"

    def track_name(self) -> str:
        return "Brazilian_CR"

    def language_ietf(self) -> str:
        return 'pt-BR'

    def codec(self) -> str:
        ...

    def default_track(self) -> bool:
        ...

    def enabled_track(self) -> bool:
        ...

    def forced_track(self) -> bool:
        ...

    def language(self) -> str:
        ...

    def number(self) -> int:
        ...

    def type(self) -> str:
        ...


@fixture
def attaches_data():
    return {
        "attachments": [
            {
                "content_type": "application/x-truetype-font",
                "description": "",
                "file_name": "arialbd_3.ttf",
                "id": 1,
                "properties": {
                    "uid": 8047349583708614449
                },
                "size": 286620
            },
            {
                "content_type": "application/x-truetype-font",
                "description": "",
                "file_name": "arialbi_2.ttf",
                "id": 2,
                "properties": {
                    "uid": 7732919397466994846
                },
                "size": 224692
            }
        ]
    }


@fixture
def track_data():
    return {
        "tracks": [
            {
                "codec": "AVC/H.264/MPEG-4p10",
                "id": 0,
                "properties": {
                    "codec_id": "V_MPEG4/ISO/AVC",
                    "codec_private_data": "01640028ffe1001c67640028acb280f",
                    "codec_private_length": 49,
                    "color_matrix_coefficients": 1,
                    "color_primaries": 1,
                    "color_transfer_characteristics": 1,
                    "default_duration": 41708333,
                    "default_track": True,
                    "display_dimensions": "1920x1080",
                    "display_unit": 0,
                    "enabled_track": True,
                    "forced_track": False,
                    "language": "jpn",
                    "language_ietf": "ja",
                    "minimum_timestamp": 0,
                    "num_index_entries": 710,
                    "number": 1,
                    "packetizer": "mpeg4_p10_video",
                    "pixel_dimensions": "1920x1080",
                    "tag__statistics_tags": "BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES",
                    "tag__statistics_writing_app": "mkvmerge v96.0 ('It's My Life') 64-bit",
                    "tag__statistics_writing_date_utc": "2025-12-21 17:13:24",
                    "tag_bps": "7989844",
                    "tag_duration": "00:23:39.962000000",
                    "tag_number_of_bytes": "1418159416",
                    "tag_number_of_frames": "34045",
                    "track_name": "[Erai-raws]_AVC_CR",
                    "uid": 337073230518517163
                },
                "type": "video"
            },
            {
                "codec": "AAC",
                "id": 1,
                "properties": {
                    "audio_channels": 2,
                    "audio_sampling_frequency": 48000,
                    "codec_id": "A_AAC",
                    "codec_private_data": "1190",
                    "codec_private_length": 2,
                    "default_duration": 21333333,
                    "default_track": True,
                    "enabled_track": True,
                    "forced_track": False,
                    "language": "jpn",
                    "language_ietf": "ja",
                    "minimum_timestamp": 0,
                    "num_index_entries": 0,
                    "number": 2,
                    "tag__statistics_tags": "BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES",
                    "tag__statistics_writing_app": "mkvmerge v96.0 ('It's My Life') 64-bit",
                    "tag__statistics_writing_date_utc": "2025-12-21 17:13:24",
                    "tag_bps": "191999",
                    "tag_duration": "00:23:40.011000000",
                    "tag_number_of_bytes": "34080257",
                    "tag_number_of_frames": "66563",
                    "track_name": "[Erai-raws]_AAC_CR",
                    "uid": 17826996854814350647
                },
                "type": "audio"
            },
            {
                "codec": "SubStationAlpha",
                "id": 2,
                "properties": {
                    "codec_id": "S_TEXT/ASS",
                    "codec_private_data": "5b53637269707420496e666f5d0d0a5",
                    "codec_private_length": 1431,
                    "default_track": True,
                    "enabled_track": True,
                    "encoding": "UTF-8",
                    "forced_track": False,
                    "language": "eng",
                    "language_ietf": "en",
                    "minimum_timestamp": 1010000000,
                    "num_index_entries": 484,
                    "number": 3,
                    "tag__statistics_tags": "BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES",
                    "tag__statistics_writing_app": "mkvmerge v96.0 ('It's My Life') 64-bit",
                    "tag__statistics_writing_date_utc": "2025-12-21 17:13:24",
                    "tag_bps": "226",
                    "tag_duration": "00:22:12.530000000",
                    "tag_number_of_bytes": "37761",
                    "tag_number_of_frames": "484",
                    "text_subtitles": True,
                    "track_name": "CR",
                    "uid": 15892778650616245918
                },
                "type": "subtitles"
            },
            {
                "codec": "SubStationAlpha",
                "id": 3,
                "properties": {
                    "codec_id": "S_TEXT/ASS",
                    "codec_private_data": "5b53637269707420496e666f5d0d0a5469746c653a",
                    "codec_private_length": 1207,
                    "default_track": False,
                    "enabled_track": True,
                    "encoding": "UTF-8",
                    "forced_track": False,
                    "language": "por",
                    "language_ietf": "pt-BR",
                    "minimum_timestamp": 1140000000,
                    "num_index_entries": 366,
                    "number": 4,
                    "tag__statistics_tags": "BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES",
                    "tag__statistics_writing_app": "mkvmerge v96.0 ('It's My Life') 64-bit",
                    "tag__statistics_writing_date_utc": "2025-12-21 17:13:24",
                    "tag_bps": "134",
                    "tag_duration": "00:23:38.800000000",
                    "tag_number_of_bytes": "23828",
                    "tag_number_of_frames": "366",
                    "text_subtitles": True,
                    "track_name": "Brazilian_CR",
                    "uid": 14539514268308361919
                },
                "type": "subtitles"
            }]
    }


def test_MKVMergeAttachmentAdapter_id(attaches_data):
    data = attaches_data['attachments'][0]
    attach_adapter = MKVMergeAttachmentAdapter(data)
    assert attach_adapter.id() == 1


def test_MKVMergeAttachmentAdapter_uid(attaches_data):
    data = attaches_data['attachments'][0]
    attach_adapter = MKVMergeAttachmentAdapter(data)
    assert attach_adapter.uid() == 8047349583708614449


def test_MKVMergeAttachmentAdapter_file_name(attaches_data):
    data = attaches_data['attachments'][0]
    attach_adapter = MKVMergeAttachmentAdapter(data)
    assert attach_adapter.file_name() == 'arialbd_3.ttf'


def test_MKVMergeAttachmentAdapter_content_type(attaches_data):
    data = attaches_data['attachments'][0]
    attach_adapter = MKVMergeAttachmentAdapter(data)
    assert attach_adapter.content_type() == "application/x-truetype-font"


def test_MKVMergeAttachmentAdapter_id_last(attaches_data):
    data = attaches_data['attachments'][1]
    attach_adapter = MKVMergeAttachmentAdapter(data)
    assert attach_adapter.id() == 2


def test_MKVMergeTrackAdapter_id(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.id() == 0


def test_MKVMergeTrackAdapter_uid(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.uid() == 337073230518517163


def test_MKVMergeTrackAdapter_codec(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.codec() == "AVC/H.264/MPEG-4p10"


def test_MKVMergeTrackAdapter_codec_id(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.codec_id() == "V_MPEG4/ISO/AVC"


def test_MKVMergeTrackAdapter_default_track(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.default_track() is True


def test_MKVMergeTrackAdapter_enabled_track(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.enabled_track() is True


def test_MKVMergeTrackAdapter_forced_track(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.forced_track() is False


def test_MKVMergeTrackAdapter_language(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.language() == "jpn"


def test_MKVMergeTrackAdapter_language_ietf(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.language_ietf() == "ja"


def test_MKVMergeTrackAdapter_number(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.number() == 1


def test_MKVMergeTrackAdapter_track_name(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.track_name() == "[Erai-raws]_AVC_CR"


def test_MKVMergeTrackAdapter_type(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.type() == "video"


def test_BasicTrackAdapter_id_3():
    track_adapter = FakeTrackAdapter({})
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.id() == 3


def test_BasicTrackAdapter_id_diferente_1():
    track_adapter = FakeTrackAdapter({})
    track_adapter.id = lambda: 1
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.id() == 1


def test_BasicTrackAdapter_uid():
    track_adapter = FakeTrackAdapter({})
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.uid() == 14539514268308361919


def test_BasicTrackAdapter_uid_0():
    track_adapter = FakeTrackAdapter({})
    track_adapter.uid = lambda: 0
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.uid() == 0


def test_BasicTrackAdapter_content_type_subtitle():
    track_adapter = FakeTrackAdapter({})
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.content_type() == "S_TEXT/ASS"


def test_BasicTrackAdapter_content_type_video():
    track_adapter = FakeTrackAdapter({})
    track_adapter.codec_id = lambda: "V_MPEG4/ISO/AVC"

    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.content_type() == "V_MPEG4/ISO/AVC"


def test_BasicTrackAdapter_file_name():
    expect = "3_Brazilian_CR_pt-BR.ass"
    track_adapter = FakeTrackAdapter({})
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.file_name() == expect


def test_BasicTrackAdapter_file_name_track_name_unknown():
    expect = "3_unknown_pt-BR.ass"
    track_adapter = FakeTrackAdapter({})
    track_adapter.track_name = lambda: ""
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.file_name() == expect


def test_BasicTrackAdapter_file_name_id_1():
    expect = "1_Brazilian_CR_pt-BR.ass"
    track_adapter = FakeTrackAdapter({})
    track_adapter.id = lambda: 1
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.file_name() == expect


def test_BasicTrackAdapter_language_ietf_pt_PT():
    expect = "3_Brazilian_CR_pt-PT.ass"
    track_adapter = FakeTrackAdapter({})
    track_adapter.language_ietf = lambda: "pt-PT"
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.file_name() == expect


def test_BasicTrackAdapter_language_ietf_und():
    expect = "3_Brazilian_CR_und.ass"
    track_adapter = FakeTrackAdapter({})
    track_adapter.language_ietf = lambda: ""
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.file_name() == expect


def test_BasicTrackAdapter_suffix_ass():
    expect = "3_Brazilian_CR_pt-BR.ass"
    track_adapter = FakeTrackAdapter({})
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.file_name() == expect


def test_BasicTrackAdapter_suffix_srt():
    expect = "3_Brazilian_CR_pt-BR.srt"
    track_adapter = FakeTrackAdapter({})
    track_adapter.codec_id = lambda: "S_TEXT/UTF8"
    adapter = BasicTrackAdapter(track_adapter)
    assert adapter.file_name() == expect


def test_BasicTrackAdapter_suffix_vazio():
    expect = "Faixa 3 possui codec_id ausente ou vazio."
    with raises(ValueError) as excinfo:
        track_adapter = FakeTrackAdapter({})
        track_adapter.codec_id = lambda: ""
        BasicTrackAdapter(track_adapter)
    result = str(excinfo.value)
    assert result == expect
