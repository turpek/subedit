from subedit.adapter import MKVMergeAttachmentAdapter, BasicTrackAdapter
from subedit.adapters.mkvmerge import MKVMergeTrackAdapter, MKVMergeAudioAdapter, MKVMergeSubtitleAdapter, MKVMergeVideoAdapter
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
            # --- TRILHA 0: VÍDEO (MKVMergeVideoAdapter) ---
            {
                "codec": "AVC/H.264/MPEG-4p10",
                "id": 0,
                "type": "video",
                "properties": {
                    # Dados Originais
                    "codec_id": "V_MPEG4/ISO/AVC",
                    "codec_private_data": "01640028ffe1001c67640028acb280f",
                    "codec_private_length": 49,
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
                    "track_name": "[Erai-raws]_AVC_CR",
                    "uid": 337073230518517163,

                    # --- NOVOS CAMPOS FICTÍCIOS (Classe Video) ---
                    "stereo_mode": 0,             # 0 = Mono/2D (Falta no original)
                    "field_order": 0,             # 0 = Progressivo (Falta no original)
                    "color_range": 1,             # 1 = Broadcast Range (Falta no original)
                    "color_primaries": 1,         # 1 = BT.709
                    "color_transfer_characteristics": 1,  # 1 = BT.709 (Nota: Adapter tinha typo na chave)
                    "color_matrix_coefficients": 1,       # 1 = BT.709

                    # --- FLAGS DE TRACK (Classe Track) ---
                    "flag_hearing_impaired": False,
                    "flag_visual_impaired": False,
                    "flag_text_descriptions": False,
                    "flag_original": True,        # Vídeo Original
                    "flag_commentary": False
                }
            },
            # --- TRILHA 1: ÁUDIO (MKVMergeAudioAdapter) ---
            {
                "codec": "AAC",
                "id": 1,
                "type": "audio",
                "properties": {
                    # Dados Originais
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
                    "track_name": "[Erai-raws]_AAC_CR",
                    "uid": 17826996854814350647,

                    # --- NOVOS CAMPOS FICTÍCIOS (Classe Audio) ---
                    "aac_is_sbr": "false",        # String 'false'/'true' conforme schema JSON
                    "audio_emphasis": 0,          # 0 = Sem ênfase
                    "audio_bits_per_sample": 16,  # Frequentemente omitido em AAC, adicionado ficticiamente

                    # --- FLAGS DE TRACK (Classe Track) ---
                    "flag_hearing_impaired": False,
                    "flag_visual_impaired": False,
                    "flag_text_descriptions": False,
                    "flag_original": True,        # Áudio Original
                    "flag_commentary": False
                }
            },

            # --- TRILHA 2: LEGENDA (MKVMergeSubtitleAdapter) ---
            {
                "codec": "SubStationAlpha",
                "id": 2,
                "type": "subtitles",
                "properties": {
                    # Dados Originais
                    "codec_id": "S_TEXT/ASS",
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
                    "text_subtitles": True,
                    "track_name": "CR",
                    "uid": 15892778650616245918,

                    # --- FLAGS DE TRACK (Classe Track) ---
                    "flag_hearing_impaired": True,  # Exemplo: Legenda para surdos (SDH)
                    "flag_visual_impaired": False,
                    "flag_text_descriptions": False,
                    "flag_original": False,
                    "flag_commentary": False
                }
            },

            # --- TRILHA 3: LEGENDA PT-BR (MKVMergeSubtitleAdapter) ---
            {
                "codec": "SubStationAlpha",
                "id": 3,
                "type": "subtitles",
                "properties": {
                    # Dados Originais
                    "codec_id": "S_TEXT/ASS",
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
                    "text_subtitles": True,
                    "track_name": "Brazilian_CR",
                    "uid": 14539514268308361919,

                    # --- FLAGS DE TRACK (Classe Track) ---
                    "flag_hearing_impaired": False,
                    "flag_visual_impaired": False,
                    "flag_text_descriptions": False,
                    "flag_original": False,       # Tradução
                    "flag_commentary": False
                }
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
    assert adapter.id == 0


def test_MKVMergeTrackAdapter_uid(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.uid == 337073230518517163


def test_MKVMergeTrackAdapter_codec(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.codec == "AVC/H.264/MPEG-4p10"


def test_MKVMergeTrackAdapter_codec_id(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.codec_id == "V_MPEG4/ISO/AVC"


def test_MKVMergeTrackAdapter_default_track(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.default_track is True


def test_MKVMergeTrackAdapter_enabled_track(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.enabled_track is True


def test_MKVMergeTrackAdapter_forced_track(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.forced_track is False


def test_MKVMergeTrackAdapter_language(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.language == "jpn"


def test_MKVMergeTrackAdapter_language_ietf(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.language_ietf == "ja"


def test_MKVMergeTrackAdapter_number(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.number == 1


def test_MKVMergeTrackAdapter_track_name(track_data):
    data = track_data['tracks'][0]
    adapter = MKVMergeTrackAdapter(data)
    assert adapter.track_name == "[Erai-raws]_AVC_CR"


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


def test_MKVMergeAudioAdapter_padrao(track_data):
    expect = {
        'id': 0,
        'codec': 'AAC',
        'uid': None,
        'number': 0,
        'codec_id': '',
        'track_name': '',
        'default_track': True,
        'enabled_track': True,
        'forced_track': False,
        'language': 'eng',
        'language_ietf': None,
        'default_duration': None,
        'flag_hearing_impaired': False,
        'flag_visual_impaired': False,
        'flag_text_descriptions': False,
        'flag_original': False,
        'flag_commentary': False,
        'audio_channels': None,
        'audio_emphasis': None,
        'aac_is_sbr': None
    }

    data = expect
    result = vars(MKVMergeAudioAdapter(data))
    assert result == expect


def test_MKVMergeAudioAdapter_geral(track_data):
    data = track_data['tracks'][1]
    result = vars(MKVMergeAudioAdapter(data))
    assert result == {
        'id': 1,
        'uid': 17826996854814350647,
        'number': 2,
        'codec': 'AAC',
        'codec_id': 'A_AAC',
        'default_track': True,
        'enabled_track': True,
        'forced_track': False,
        'track_name': '[Erai-raws]_AAC_CR',
        'language': 'jpn',
        'language_ietf': 'ja',
        'default_duration': 21333333,
        'flag_hearing_impaired': False,
        'flag_visual_impaired': False,
        'flag_text_descriptions': False,
        'flag_original': True,
        'flag_commentary': False,
        'audio_channels': 2,
        'aac_is_sbr': False,
        'audio_emphasis': 0
    }


def test_MKVMergeVideoAdapter_padrao(track_data):
    expect = {
        'id': 0,
        'uid': None,
        'codec': 'AVC/H.264/MPEG-4p10',
        'codec_id': '',
        'default_track': True,
        'enabled_track': True,
        'forced_track': False,
        'language': 'eng',
        'language_ietf': None,
        'number': 0,
        'track_name': '',
        'default_duration': None,
        'flag_hearing_impaired': False,
        'flag_visual_impaired': False,
        'flag_text_descriptions': False,
        'flag_original': False,
        'flag_commentary': False,
        'display_dimensions': None,
        'stereo_mode': None,
        'field_order': None,
        'color_range': None,
        'color_primaries': None,
        'color_transfer_characteristics': None,
        'color_matrix_coefficients': None
    }
    data = expect
    result = vars(MKVMergeVideoAdapter(data))
    assert result == expect


def test_MKVMergeVideoAdapter_geral(track_data):
    data = track_data['tracks'][0]
    result = vars(MKVMergeVideoAdapter(data))
    assert result == {
        'id': 0,
        'uid': 337073230518517163,
        'codec': 'AVC/H.264/MPEG-4p10',
        'codec_id': 'V_MPEG4/ISO/AVC',
        'default_track': True,
        'enabled_track': True,
        'forced_track': False,
        'language': 'jpn',
        'language_ietf': 'ja',
        'number': 1,
        'track_name': '[Erai-raws]_AVC_CR',
        'default_duration': 41708333,
        'flag_hearing_impaired': False,
        'flag_visual_impaired': False,
        'flag_text_descriptions': False,
        'flag_original': True,
        'flag_commentary': False,
        'display_dimensions': '1920x1080',
        'stereo_mode': 0,
        'field_order': 0,
        'color_range': 1,
        'color_primaries': 1,
        'color_transfer_characteristics': 1,
        'color_matrix_coefficients': 1
    }


def test_MKVMergeSubtitleAdapter_padrao(track_data):
    expect = {
        'id': 0,
        'codec': 'SubStationAlpha',
        'uid': None,
        'number': 0,
        'codec_id': '',
        'track_name': '',
        'default_track': True,
        'enabled_track': True,
        'forced_track': False,
        'language': 'eng',
        'language_ietf': None,
        'default_duration': None,
        'flag_hearing_impaired': False,
        'flag_visual_impaired': False,
        'flag_text_descriptions': False,
        'flag_original': False,
        'flag_commentary': False,
        'encoding': '',
        'text_subtitles': None
    }

    data = expect

    result = vars(MKVMergeSubtitleAdapter(data))
    assert result == expect


def test_MKVMergeSubtitleAdapter_geral(track_data):
    data = track_data['tracks'][3]
    result = vars(MKVMergeSubtitleAdapter(data))
    assert result == {
        'id': 3,
        'uid': 14539514268308361919,
        'codec': 'SubStationAlpha',
        'codec_id': 'S_TEXT/ASS',
        'default_track': False,
        'enabled_track': True,
        'forced_track': False,
        'language': 'por',
        'language_ietf': 'pt-BR',
        'number': 4,
        'track_name': 'Brazilian_CR',
        'default_duration': None,
        'flag_hearing_impaired': False,
        'flag_visual_impaired': False,
        'flag_text_descriptions': False,
        'flag_original': False,
        'flag_commentary': False,
        'encoding': 'UTF-8',
        'text_subtitles': True
    }
