from enum import Enum


class MediaType(Enum):
    ATTACHMENT = 'attachments'
    AUDIO = 'audio'
    VIDEO = 'video'
    SUBTITLE = 'subtitles'
    TRACK = 'tracks'
    ASSET = 'asset'

    def expand(self) -> set["MediaType"]:
        return MEDIA_EXPANSION[self].copy()


class Provider(Enum):
    MKVMERGE = 'mkvmerge'


MEDIA_EXPANSION = {
    MediaType.ATTACHMENT: [MediaType.ATTACHMENT],
    MediaType.AUDIO: [MediaType.AUDIO],
    MediaType.VIDEO: [MediaType.VIDEO],
    MediaType.SUBTITLE: [MediaType.SUBTITLE],
    MediaType.TRACK: [
        MediaType.AUDIO,
        MediaType.VIDEO,
        MediaType.SUBTITLE,
    ],
    MediaType.ASSET: [
        MediaType.ATTACHMENT,
        MediaType.AUDIO,
        MediaType.VIDEO,
        MediaType.SUBTITLE,
    ],
}

COMMON_TRACK_PROPS = {
    "ID": "id",
    "LANGUAGE": "language",
    "LANGUAGE_IETF": "language_ietf",
    "TRACK_NAME": "track_name",
    "CODEC": "codec",
    "CODEC_ID": "codec_id"
}


class BaseMediaProperty(Enum):
    ...


def build_track_property(name: str):
    return Enum(name, COMMON_TRACK_PROPS, type=BaseMediaProperty)


AudioProperty = build_track_property("AudioProperty")
VideoProperty = build_track_property("VideoProperty")
SubtitleProperty = build_track_property("SubtitleProperty")
TrackProperty = build_track_property("TrackProperty")
