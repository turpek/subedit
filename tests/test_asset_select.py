from subedit.assets.select import AssetSelect
from pytest import fixture, raises

ASSETS = {
    'video': ['video_hd', 'video_fhd'],
    'audio': ['audio_eng', 'audio_por'],
    'subtitle': ['sub_eng', 'sub_por']
}

SUB_EXP = {'subtitle': ['sub_tur']}


@fixture
def metype(mocker):
    media_type = mocker.patch('subedit.assets.select.MediaType')
    media_type.__iter__.return_value = ['audio', 'subtitle', 'video']
    return media_type


def test_AssetSelect_get_empty():
    sub = 'subtitle'
    expect = []
    sel = AssetSelect(12, {})
    result = sel.get(sub)
    assert result == expect


def test_AssetSelect_keys_empty():
    expect = set()
    sel = AssetSelect(12, {})
    result = set(sel.keys())
    assert result == expect


def test_AssetSelect_get_subtitle():
    sub = 'subtitle'
    expect = ASSETS[sub]
    sel = AssetSelect(1, ASSETS)
    result = sel.get(sub)
    assert result == expect


def test_AssetSelect_keys():
    expect = set(ASSETS.keys())
    sel = AssetSelect(12, ASSETS)
    result = set(sel.keys())
    assert result == expect


def test_AssetSelect_filtro_de_lista_vazia_no_init():
    assets = {'sub': ['por', 'eng', 'jpn'], 'audio': [], 'video': ['video_por']}
    expect = set(('sub', 'video'))
    sel = AssetSelect(12, assets)
    result = set(sel.keys())
    assert result == expect


def test_AssetSelect_get_audio():
    sub = 'audio'
    expect = ASSETS[sub]
    sel = AssetSelect(1, ASSETS)
    result = sel.get(sub)
    assert result == expect


def test_AssetSelect_get_video():
    sub = 'video'
    expect = ASSETS[sub]
    sel = AssetSelect(1, ASSETS)
    result = sel.get(sub)
    assert result == expect


def test_AssetSelect_select():
    sub = 'subtitle'
    sel = AssetSelect(1, ASSETS)
    selector = sel.select(sub)
    assert isinstance(selector, AssetSelect)


def test_AssetSelect_select_empty():
    sub = 'subtitle'
    expect = []
    sel = AssetSelect(12, {})
    selector = sel.select(sub)
    result = selector.get(sub)
    assert result == expect


def test_AssetSelect_select_subtitle(metype):
    sub = 'subtitle'
    expect = ASSETS[sub]
    sel = AssetSelect(12, ASSETS)
    selector = sel.select(sub)
    result = selector.get(sub)
    assert result == expect


def test_AssetSelect_uniao_de_empty(metype):
    sub = 'subtitle'
    expect = []
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {})
    sel = sel1 | sel2
    result = sel.get(sub)
    assert result == expect


def test_AssetSelect_uniao_de_empty_com_id_diff(metype):
    expect = "Cannot combine objects that do not share the same origin"
    with raises(ValueError) as excinfo:
        sel1 = AssetSelect(12, {})
        sel2 = AssetSelect(13, {})
        sel1 | sel2
    result = str(excinfo.value)
    assert result == expect


def test_AssetSelect_uniao_de_mesmo_tipo(metype):
    sub = 'subtitle'
    expect = set(['sub_eng', 'sub_por', 'sub_tur'])
    sel1 = AssetSelect(12, {sub: ASSETS[sub]})
    sel2 = AssetSelect(12, SUB_EXP)
    sel = sel1 | sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_uniao_com_left_empty(metype):
    sub = 'subtitle'
    expect = set(SUB_EXP[sub])
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, SUB_EXP)
    sel = sel1 | sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_uniao_com_right_empty(metype):
    sub = 'subtitle'
    expect = set(SUB_EXP[sub])
    sel1 = AssetSelect(12, SUB_EXP)
    sel2 = AssetSelect(12, {})
    sel = sel1 | sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_uniao_com_varios_tipos(metype):
    sub = 'subtitle'
    arg2 = {
        'video': ['video_01'],
        'audio': ['audio_jpn', 'audio_por']
    }
    expect = set(SUB_EXP[sub]) | set(
        ['video_01', 'audio_jpn', 'audio_por']
    )
    sel1 = AssetSelect(12, SUB_EXP)
    sel2 = AssetSelect(12, arg2)
    sel = sel1 | sel2
    result = set(sel.get(sub)) | set(sel.get('video')) | set(sel.get('audio'))
    assert result == expect


def test_AssetSelect_uniao_composta_de_mesmo_tipo(metype):
    sub = 'subtitle'
    expect = set(['sub_eng', 'sub_por', 'sub_tur'])
    sel1 = AssetSelect(12, {sub: ASSETS[sub]})
    sel2 = AssetSelect(12, SUB_EXP)
    sel = sel1
    sel |= sel2
    result = sel1.get(sub)
    assert set(result) == expect


def test_AssetSelect_uniao_composta_empty(metype):
    sub = 'subtitle'
    expect = set()
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {})
    sel = sel1
    sel |= sel2
    result = sel1.get(sub)
    assert set(result) == expect


def test_AssetSelect_uniao_composta_com_left_empty(metype):
    sub = 'subtitle'
    expect = set(['sub_eng'])
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {sub: ['sub_eng']})
    sel = sel1
    sel |= sel2
    result = sel1.get(sub)
    assert set(result) == expect


def test_AssetSelect_uniao_composta_right_empty(metype):
    sub = 'subtitle'
    expect = set(['sub_eng'])
    sel1 = AssetSelect(12, {sub: ['sub_eng']})
    sel2 = AssetSelect(12, {})
    sel = sel1
    sel |= sel2
    result = sel1.get(sub)
    assert set(result) == expect


def test_AssetSelect_uniao_composta_empty_com_id_diff(metype):
    expect = "Cannot combine objects that do not share the same origin"
    with raises(ValueError) as excinfo:
        sel1 = AssetSelect(12, {})
        sel2 = AssetSelect(13, {})
        sel1 |= sel2
    result = str(excinfo.value)
    assert result == expect


def test_AssetSelect_uniao_composto_com_varios_tipos(metype):
    sub = 'subtitle'
    arg2 = {
        'video': ['video_01'],
        'audio': ['audio_jpn', 'audio_por']
    }
    expect = set(SUB_EXP[sub]) | set(
        ['video_01', 'audio_jpn', 'audio_por']
    )
    sel1 = AssetSelect(12, SUB_EXP)
    sel2 = AssetSelect(12, arg2)
    sel = sel1
    sel1 |= sel2
    result = set(sel.get(sub)) | set(sel.get('video')) | set(sel.get('audio'))
    assert result == expect


def test_AssetSelect_difference_empty(metype):
    sub = 'subtitle'
    expect = set()
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {})
    sel = sel1 - sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_difference(metype):
    sub = 'subtitle'
    expect = set(['sub_eng'])
    sel1 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel2 = AssetSelect(12, {sub: ['sub_por', 'sub_esp']})
    sel = sel1 - sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_difference_left_empty(metype):
    sub = 'subtitle'
    expect = set([])
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {sub: ['sub_por', 'sub_esp']})
    sel = sel1 - sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_difference_right_empty(metype):
    sub = 'subtitle'
    expect = set(['sub_por', 'sub_esp'])
    sel1 = AssetSelect(12, {sub: ['sub_por', 'sub_esp']})
    sel2 = AssetSelect(12, {})
    sel = sel1 - sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_difference_empty_com_id_diff(metype):
    expect = "Cannot combine objects that do not share the same origin"
    with raises(ValueError) as excinfo:
        sel1 = AssetSelect(12, {})
        sel2 = AssetSelect(13, {})
        sel1 - sel2
    result = str(excinfo.value)
    assert result == expect


def test_AssetSelect_difference_com_varios_tipos(metype):
    sub = 'subtitle'
    expect = set(['sub_esp', 'video_01'])
    arg1 = {
        sub: ['sub_por', 'sub_esp'],
        'video': ['video_01']
    }
    arg2 = {
        sub: ['sub_por'],
        'audio': ['audio_por']
    }
    sel1 = AssetSelect(12, arg1)
    sel2 = AssetSelect(12, arg2)
    sel = sel1 - sel2
    result = set(sel.get(sub)) | set(sel.get('video')) | set(sel.get('audio'))
    assert set(result) == expect


def test_AssetSelect_difference_composta_empty(metype):
    sub = 'subtitle'
    expect = set()
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {})
    sel = sel1
    sel1 -= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_difference_composta(metype):
    sub = 'subtitle'
    expect = set(['sub_eng'])
    sel1 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel2 = AssetSelect(12, {sub: ['sub_por', 'sub_esp']})
    sel = sel1
    sel1 -= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_difference_composta_left_empty(metype):
    sub = 'subtitle'
    expect = set()
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {sub: ['sub_por', 'sub_esp']})
    sel = sel1
    sel1 -= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_difference_composta_right_empty(metype):
    sub = 'subtitle'
    expect = set([])
    sel1 = AssetSelect(12, {sub: ['sub_por', 'sub_esp']})
    sel2 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel = sel1
    sel = sel1 - sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_difference_composta_com_varios_tipos(metype):
    sub = 'subtitle'
    expect = set(['sub_esp', 'video_01'])
    arg1 = {
        sub: ['sub_por', 'sub_esp'],
        'video': ['video_01']
    }
    arg2 = {
        sub: ['sub_por'],
        'audio': ['audio_por']
    }
    sel1 = AssetSelect(12, arg1)
    sel2 = AssetSelect(12, arg2)
    sel = sel1
    sel1 -= sel2
    result = set(sel.get(sub)) | set(sel.get('video')) | set(sel.get('audio'))
    assert set(result) == expect


def test_AssetSelect_intersection_empty(metype):
    sub = 'subtitle'
    expect = set()
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {})
    sel = sel1 & sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_intersection_empty_id_diff(metype):
    expect = "Cannot combine objects that do not share the same origin"
    with raises(ValueError) as excinfo:
        sel1 = AssetSelect(12, {})
        sel2 = AssetSelect(13, {})
        sel1 & sel2
    result = str(excinfo.value)
    assert result == expect


def test_AssetSelect_intersection(metype):
    sub = 'subtitle'
    expect = set(['sub_por', 'sub_esp'])
    sel1 = AssetSelect(12, {sub: ['sub_por', 'sub_esp', 'sub_ara']})
    sel2 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel = sel1 & sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_intersection_left_empty(metype):
    sub = 'subtitle'
    expect = set([])
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel = sel1 & sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_intersection_right_empty(metype):
    sub = 'subtitle'
    expect = set([])
    sel1 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel2 = AssetSelect(12, {})
    sel = sel1 & sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_intersection_com_varios_tipos(metype):
    sub = 'subtitle'
    expect = set(['sub_por', 'video_01'])
    arg1 = {
        sub: ['sub_eng', 'sub_por', 'sub_esp'],
        'video': ['video_01']
    }
    arg2 = {
        sub: ['sub_por'],
        'video': ['video_01', 'video_02'],
        'audio': ['audio_jpn', 'audio_eng']
    }
    sel1 = AssetSelect(12, arg1)
    sel2 = AssetSelect(12, arg2)
    sel = sel1 & sel2
    result = set(sel.get(sub)) | set(sel.get('video')) | set(sel.get('audio'))
    assert result == expect


def test_AssetSelect_intersection_composta_empty(metype):
    sub = 'subtitle'
    expect = set()
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {})
    sel = sel1
    sel1 &= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_intersection_composta_empty_id_diff(metype):
    expect = "Cannot combine objects that do not share the same origin"
    with raises(ValueError) as excinfo:
        sel1 = AssetSelect(12, {})
        sel2 = AssetSelect(13, {})
        sel1 &= sel2
    result = str(excinfo.value)
    assert result == expect


def test_AssetSelect_intersection_composta(metype):
    sub = 'subtitle'
    expect = set(['sub_por', 'sub_esp'])
    sel1 = AssetSelect(12, {sub: ['sub_por', 'sub_esp', 'sub_ara']})
    sel2 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel = sel1
    sel1 &= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_intersection_composta_left_empty(metype):
    sub = 'subtitle'
    expect = set([])
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel = sel1
    sel1 &= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_intersection_composta_right_empty(metype):
    sub = 'subtitle'
    expect = set([])
    sel1 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel2 = AssetSelect(12, {})
    sel = sel1
    sel1 &= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_intersection_composta_com_varios_tipos(metype):
    sub = 'subtitle'
    expect = set(['sub_por', 'video_01'])
    arg1 = {
        sub: ['sub_eng', 'sub_por', 'sub_esp'],
        'video': ['video_01']
    }
    arg2 = {
        sub: ['sub_por'],
        'video': ['video_01', 'video_02'],
        'audio': ['audio_jpn', 'audio_eng']
    }
    sel1 = AssetSelect(12, arg1)
    sel2 = AssetSelect(12, arg2)
    sel = sel1
    sel1 &= sel2
    result = set(sel.get(sub)) | set(sel.get('video')) | set(sel.get('audio'))
    assert result == expect


def test_AssetSelect_simmetric_difference_empty(metype):
    sub = 'subtitle'
    expect = set()
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {})
    sel = sel1
    sel = sel1 ^ sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_simmetric_difference_empty_id_diff(metype):
    expect = "Cannot combine objects that do not share the same origin"
    with raises(ValueError) as excinfo:
        sel1 = AssetSelect(12, {})
        sel2 = AssetSelect(13, {})
        sel1 ^ sel2
    result = str(excinfo.value)
    assert result == expect


def test_AssetSelect_simmetric_difference(metype):
    sub = 'subtitle'
    expect = set(['sub_ara', 'sub_eng'])
    sel1 = AssetSelect(12, {sub: ['sub_por', 'sub_esp', 'sub_ara']})
    sel2 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel = sel1 ^ sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_simmetric_difference_left_empty(metype):
    sub = 'subtitle'
    expect = set(['sub_eng', 'sub_por', 'sub_esp'])
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel = sel1 ^ sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_simmetric_difference_right_empty(metype):
    sub = 'subtitle'
    expect = set(['sub_eng', 'sub_por', 'sub_esp'])
    sel1 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel2 = AssetSelect(12, {})
    sel = sel1 ^ sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_simmetric_difference_com_varios_tipos(metype):
    sub = 'subtitle'
    expect = set(['sub_eng', 'sub_esp', 'video_02', 'audio_jpn', 'audio_eng'])
    arg1 = {
        sub: ['sub_eng', 'sub_por', 'sub_esp'],
        'video': ['video_01']
    }
    arg2 = {
        sub: ['sub_por'],
        'video': ['video_01', 'video_02'],
        'audio': ['audio_jpn', 'audio_eng']
    }
    sel1 = AssetSelect(12, arg1)
    sel2 = AssetSelect(12, arg2)
    sel = sel1 ^ sel2
    result = set(sel.get(sub)) | set(sel.get('video')) | set(sel.get('audio'))
    assert result == expect


def test_AssetSelect_simmetric_difference_composta_empty(metype):
    sub = 'subtitle'
    expect = set()
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {})
    sel = sel1
    sel1 ^= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_simmetric_difference_composta_empty_id_diff(metype):
    expect = "Cannot combine objects that do not share the same origin"
    with raises(ValueError) as excinfo:
        sel1 = AssetSelect(12, {})
        sel2 = AssetSelect(13, {})
        sel1 ^= sel2
    result = str(excinfo.value)
    assert result == expect


def test_AssetSelect_simmetric_difference_composta(metype):
    sub = 'subtitle'
    expect = set(['sub_ara', 'sub_eng'])
    sel1 = AssetSelect(12, {sub: ['sub_por', 'sub_esp', 'sub_ara']})
    sel2 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel = sel1
    sel1 ^= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_simmetric_difference_composta_left_empty(metype):
    sub = 'subtitle'
    expect = set(['sub_eng', 'sub_por', 'sub_esp'])
    sel1 = AssetSelect(12, {})
    sel2 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel = sel1
    sel1 ^= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_simmetric_difference_composta_right_empty(metype):
    sub = 'subtitle'
    expect = set(['sub_eng', 'sub_por', 'sub_esp'])
    sel1 = AssetSelect(12, {sub: ['sub_eng', 'sub_por', 'sub_esp']})
    sel2 = AssetSelect(12, {})
    sel = sel1
    sel1 ^= sel2
    result = sel.get(sub)
    assert set(result) == expect


def test_AssetSelect_simmetric_difference_composta_com_varios_tipos(metype):
    sub = 'subtitle'
    expect = set(['sub_eng', 'sub_esp', 'video_02', 'audio_jpn', 'audio_eng'])
    arg1 = {
        sub: ['sub_eng', 'sub_por', 'sub_esp'],
        'video': ['video_01']
    }
    arg2 = {
        sub: ['sub_por'],
        'video': ['video_01', 'video_02'],
        'audio': ['audio_jpn', 'audio_eng']
    }
    sel1 = AssetSelect(12, arg1)
    sel2 = AssetSelect(12, arg2)
    sel = sel1
    sel1 ^= sel2
    result = set(sel.get(sub)) | set(sel.get('video')) | set(sel.get('audio'))
    assert result == expect


def test_AssetSelect_selecionar_um_asset_especifico(metype):
    expect = set(['video'])
    sel = AssetSelect(12, ASSETS)
    result = set(sel(['video']).keys())
    assert result == expect
