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


def build_track_property(name: str, **kwargs):
    props = COMMON_TRACK_PROPS.copy()
    props.update(kwargs)
    return Enum(name, props, type=BaseMediaProperty)


AudioProperty = build_track_property("AudioProperty")
VideoProperty = build_track_property("VideoProperty")
SubtitleProperty = build_track_property("SubtitleProperty")
TrackProperty = build_track_property("TrackProperty")


def expand_media_type(media_type: MediaType | list[MediaType]) -> list[MediaType]:
    if isinstance(media_type, MediaType):
        return media_type.expand()
    expand_media = []
    for type_ in media_type:
        if type_ not in expand_media:
            expand_media.extend(type_.expand())
    return expand_media


MEDIA_PROP_TO_TYPE = {
    TrackProperty: MediaType.TRACK,
    AudioProperty: MediaType.AUDIO,
    SubtitleProperty: MediaType.SUBTITLE,
    VideoProperty: MediaType.VIDEO,
}


def resolve_media_type(prop: BaseMediaProperty) -> MediaType:
    try:
        return MEDIA_PROP_TO_TYPE[type(prop)]
    except KeyError:
        raise TypeError(f"could not convert property '{type(prop)}' to 'MediaType'")
