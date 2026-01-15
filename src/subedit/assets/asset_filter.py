from subedit.media_enums import (
    AudioProperty,
    SubtitleProperty,
    VideoProperty,
    TrackProperty
)
from subedit.proxy.tracks import Track
from typing import Iterable


def filter_by_id(tracks: Iterable[Track], ids: int | Iterable[int]) -> list:
    return [track for track in tracks if track.id in ids]


def filter_by_language(tracks: Iterable[Track], languages: str | Iterable[str]) -> list:
    lang = languages if not isinstance(languages, str) else [languages]
    return [track for track in tracks if track.language in lang]


def filter_by_language_ietf(tracks: Iterable[Track], languages: str | Iterable[str]) -> list:
    lang = languages if not isinstance(languages, str) else [languages]
    return [track for track in tracks if track.language in lang]


ASSET_FILTER = {

    # Filtragem usando o ID nos tipos `Track`
    AudioProperty.ID: filter_by_id,
    SubtitleProperty.ID: filter_by_id,
    VideoProperty.ID: filter_by_id,
    TrackProperty.ID: filter_by_id,

    # Filtragem usando a LANGUAGE nos tipos `Track`
    AudioProperty.LANGUAGE: filter_by_language,
    SubtitleProperty.LANGUAGE: filter_by_language,
    VideoProperty.LANGUAGE: filter_by_language,
    TrackProperty.LANGUAGE: filter_by_language,

    # Filtragem usando a LANGUAGE nos tipos `Track`
    AudioProperty.LANGUAGE_IETF: filter_by_language_ietf,
    SubtitleProperty.LANGUAGE_IETF: filter_by_language_ietf,
    VideoProperty.LANGUAGE_IETF: filter_by_language_ietf,
    TrackProperty.LANGUAGE_IETF: filter_by_language_ietf,
}
