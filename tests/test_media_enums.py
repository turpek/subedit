from subedit.media_enums import MediaType, MEDIA_EXPANSION
import pytest


MT_VALUES = {'attachments', 'audio', 'video', 'subtitles', 'tracks', 'asset'}


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
