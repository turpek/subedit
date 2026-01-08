from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TrackSnapshot:
    id: int
    codec: str
    uid: Optional[int] = None
    codec_id: str = ""
    default_track: bool = True    # Padrão True [1]
    enabled_track: bool = True    # Padrão True [1]
    forced_track: bool = False    # Padrão False [1]
    language: str = "eng"         # Padrão 'eng' [1]
    language_ietf: Optional[str] = None
    number: int = 0
    track_name: str = ""
    default_duration: Optional[int] = None
    flag_hearing_impaired: bool = False
    flag_visual_impaired: bool = False
    flag_text_descriptions: bool = False
    flag_original: bool = False
    flag_commentary: bool = False


@dataclass(frozen=True)
class AudioTrackSnapshot(TrackSnapshot):
    audio_channels: Optional[int] = None
    aac_is_sbr: Optional[bool] = None
    audio_emphasis: Optional[int] = None


@dataclass(frozen=True)
class SubtitleTrackSnapshot(TrackSnapshot):
    encoding: str = ''
    text_subtitles: Optional[bool] = None


@dataclass(frozen=True)
class VideoTrackSnapshot(TrackSnapshot):
    display_dimensions: Optional[str] = None
    stereo_mode: Optional[int] = None
    field_order: Optional[int] = None
    color_range: Optional[int] = None
    color_primaries: Optional[int] = None
    color_transfer_characteristics: Optional[int] = None
    color_matrix_coefficients: Optional[int] = None
