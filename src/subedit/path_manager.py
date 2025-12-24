from pathlib3x import Path
from typing import Union
from subedit.interface import IAttachment, ITrack


_SUFFIX = {
    # --- VÍDEO ---
    "V_MPEG1": ".m1v",             # MPEG-1 elementary stream
    "V_MPEG2": ".m2v",             # MPEG-2 elementary stream
    "V_MPEG4/ISO/AVC": ".h264",    # H.264 / AVC elementary stream
    "V_MPEG4/ISO/HEVC": ".h265",   # H.265 / HEVC elementary stream
    "V_MS/VFW/FOURCC": ".avi",     # Fixed FPS AVI
    "V_REAL/RV10": ".rm",          # RealVideo
    "V_REAL/RV20": ".rm",          # RealVideo
    "V_REAL/RV30": ".rm",          # RealVideo
    "V_REAL/RV40": ".rm",          # RealVideo
    "V_THEORA": ".ogg",            # Theora em container Ogg
    "V_VP8": ".ivf",               # VP8 em formato IVF
    "V_VP9": ".ivf",               # VP9 em formato IVF

    # --- ÁUDIO ---
    "A_AAC": ".aac",               # AAC com cabeçalhos ADTS
    "A_AAC/MPEG2/MAIN": ".aac",    # AAC MPEG-2
    "A_AAC/MPEG4/MAIN": ".aac",    # AAC MPEG-4
    "A_AAC/MPEG4/LC": ".aac",      # AAC Low Complexity
    "A_AAC/MPEG4/LC/SBR": ".aac",  # HE-AAC
    "A_AC3": ".ac3",               # AC-3 bruto
    "A_EAC3": ".ac3",              # Enhanced AC-3
    "A_ALAC": ".caf",              # Apple Lossless em Core Audio Format
    "A_DTS": ".dts",               # DTS bruto
    "A_FLAC": ".flac",             # FLAC bruto
    "A_MPEG/L2": ".mp2",           # MPEG-1 Audio Layer II
    "A_MPEG/L3": ".mp3",           # MPEG-1 Audio Layer III
    "A_OPUS": ".opus",             # OggOpus
    "A_PCM/INT/LIT": ".wav",       # PCM Little-endian
    "A_PCM/INT/BIG": ".wav",       # PCM Big-endian (convertido para Little)
    "A_REAL/28_8": ".rm",          # RealAudio
    "A_REAL/COOK": ".rm",          # RealAudio
    "A_REAL/SIPR": ".rm",          # RealAudio
    "A_REAL/RALF": ".rm",          # RealAudio
    "A_REAL/ATRC": ".rm",          # RealAudio
    "A_TRUEHD": ".truehd",         # TrueHD bruto
    "A_MLP": ".mlp",               # MLP bruto
    "A_TTA1": ".tta",              # TrueAudio
    "A_VORBIS": ".ogg",            # Vorbis em container Ogg
    "A_WAVPACK4": ".wv",           # WavPack

    # --- LEGENDAS ---
    "S_HDMV/PGS": ".sup",          # PGS (Blu-ray)
    "S_HDMV/TEXTST": ".txt",       # TextST (formato especial)
    "S_KATE": ".ogg",              # Kate em container Ogg
    "S_TEXT/SSA": ".ssa",          # SubStation Alpha
    "S_TEXT/ASS": ".ass",          # Advanced SubStation Alpha
    "S_SSA": ".ssa",               # SSA legado
    "S_ASS": ".ass",               # ASS legado
    "S_TEXT/UTF8": ".srt",         # SRT (UTF-8)
    "S_TEXT/ASCII": ".srt",        # SRT (ASCII)
    "S_VOBSUB": ".idx",            # VobSub (gera também um .sub)
    "S_TEXT/USF": ".usf",          # Universal Subtitle Format
    "S_TEXT/WEBVTT": ".vtt",       # WebVTT

    # --- OUTROS ELEMENTOS ---
    "Tags": ".xml",                # Metadados em XML
    "Chapters": ".xml",            # Capítulos em XML
    "Chapters_Simple": ".txt",     # Capítulos em formato OGM
    "Timestamps": ".txt",          # Timestamps v2
}


class PathManager:
    def __init__(self, file: Path):
        self.__file = file

    def __get_track_lang(self, item: ITrack):
        return lang if (lang := item.language_ietf()) != 'und' else item.language()

    def __from_track(self, item: ITrack):
        suffix = _SUFFIX[item.codec_id()]
        file = self.__file.stem
        item_id = item.id()
        name = item.track_name()
        lang = self.__get_track_lang(item)
        return Path(f'{item_id}_{file}_{name}({lang}){suffix}')

    def __from_attachment(self, item: IAttachment):
        return Path('fonts') / item.file_name()

    def path_from(self, item: Union[IAttachment, ITrack]):
        if isinstance(item, ITrack):
            return self.__from_track(item)
        elif isinstance(item, IAttachment):
            return self.__from_attachment(item)

        type_name = type(item).__name__
        raise TypeError(
            f"Tipo inesperado '{type_name}' para geração de caminho. "
            f"Esperado 'ITrack' ou 'IAttachment'."
        )
