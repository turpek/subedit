from subedit.media_enums import MediaType, MEDIA_EXPANSION, TrackProperty, AudioProperty
from subedit.media_enums import expand_media_type, resolve_media_type
import pytest


MT_VALUES = {'attachments', 'audio', 'video', 'subtitles', 'tracks', 'asset'}
TP_VALUES = {'id', 'language', 'language_ietf', 'track_name', 'codec', 'codec_id'}


MT_EXPANSION = {
    'attachments': ['attachments'],
    'audio': ['audio'],
    'video': ['video'],
    'subtitles': ['subtitles'],
    'tracks': ['audio', 'subtitles', 'video'],
    'asset': ['attachments', 'audio', 'subtitles', 'video']
}


def test_MediaType_members_values():
    assert MT_VALUES == {member.value for member in MediaType}


@pytest.mark.parametrize('key,value', MT_EXPANSION.items())
def test_MediaType_expansion(key, value):
    assert set(value) == set({member.value for member in MEDIA_EXPANSION[MediaType(key)]})


def test_TrackProperty_members_values():
    assert TP_VALUES == {member.value for member in TrackProperty}


def test_expand_media_type_com_audio():
    expect = [MediaType.AUDIO]
    result = expand_media_type(MediaType.AUDIO)
    assert expect == result


def test_expand_media_type_com_track():
    expect = MediaType.TRACK.expand()
    result = expand_media_type(MediaType.TRACK)
    assert expect == result


def test_expand_media_type_com_lista():
    expect = MediaType.TRACK.expand()
    expect.append(MediaType.ATTACHMENT)
    result = expand_media_type([MediaType.TRACK, MediaType.AUDIO, MediaType.ATTACHMENT])
    assert expect == result


def test_media_property_to_media_type_concrete_property():
    expect = MediaType.AUDIO
    result = resolve_media_type(AudioProperty.ID)
    assert expect == result


def test_media_property_to_media_type_abstract_property():
    expect = MediaType.TRACK
    result = resolve_media_type(TrackProperty.ID)
    assert expect == result


def test_media_property_to_media_type_com_MediaProperty_desconhecida():
    expect = "could not convert property '<class 'str'>' to 'MediaType'"
    with pytest.raises(TypeError) as excinfo:
        resolve_media_type('StrProperty')
    result = str(excinfo.value)
    assert expect == result
