from subedit.media_enums import MediaType, MEDIA_EXPANSION, TrackProperty
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
