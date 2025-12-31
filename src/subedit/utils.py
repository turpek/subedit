from enum import Enum
from loguru import logger
from pathlib import Path
import logging

SRC = (Path(__file__).parent / '..' / '..').resolve()
PATH_LOG = SRC / 'log'
SUFFIX = ['.mkv']

logger.add(f"{PATH_LOG}/subedit.log", rotation="10 MB")


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        logger.log(level, record.getMessage())


def setup_logging(log_to_file: bool = True):
    logging.basicConfig(handlers=[InterceptHandler()], level=0)

    if log_to_file:
        PATH_LOG.mkdir(parents=True, exist_ok=True)
        logger.add(PATH_LOG / "subedit.log", rotation="10 MB", level="INFO")


TRACKS_SUFFIX = {
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



def check_output(path: str | Path):
    output_dir = Path(path) / 'output'
    if not output_dir.exists():
        logger.info("creating the output directory")
        output_dir.mkdir()
    return output_dir


class PrettyMsg:
    def __init__(self, index, size, digits):
        self.__index = index
        self.__size = size
        self.__digits = digits

    def __repr__(self):
        return f'PrettyMsg(index="{self.__index}", size="{self.__size}", digits="{self.__digits}")'

    def __str__(self):
        return f'[{self.__index:>{self.__digits}}/{self.__size}]'

    def __len__(self):
        return self.__size

    def index(self):
        return self.__index

    def digits(self):
        return self.__digits


class PrettyCount:
    def __init__(self, list_: list, start=1):
        self.__size = len(list_)
        self.__digits = len(str(self.__size))
        self.__list = list_
        self.__start = start

    def __iter__(self):
        for i, el in enumerate(self.__list, start=self.__start):
            yield PrettyMsg(i, self.__size, self.__digits), el


class MediaType(str, Enum):
    ATTACHMENT = 'attachments'
    AUDIO = 'audio'
    VIDEO = 'video'
    SUBTITLE = 'subtitles'
    TRACK = 'track'
