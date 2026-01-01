from enum import Enum


class MediaType(str, Enum):
    ATTACHMENT = 'attachments'
    AUDIO = 'audio'
    VIDEO = 'video'
    SUBTITLE = 'subtitles'
    TRACK = 'tracks'
    ASSET = 'asset'

    def expand(self) -> set["MediaType"]:
        return MEDIA_EXPANSION[self]


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
