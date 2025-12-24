from subedit.path_manager import PathManager
from subedit.info import Attachment, SubtitleTrack
from pathlib3x import Path
from pytest import fixture, raises


class FakeSubtitleTrack(SubtitleTrack):
    def __init__(self):
        ...

    def id(self):
        return 2

    def codec_id(self):
        return "S_TEXT/ASS"

    def track_name(self):
        return "Brazilian_CR"

    def language(self):
        return "por"

    def language_ietf(self):
        return "pt-BR"


class FakeAttachment(Attachment):
    def __init__(self):
        ...

    def id(self) -> int:
        return 1

    def uid(self) -> int:
        return 8047349583708614449

    def content_type(self) -> str:
        return "application/x-truetype-font"

    def file_name(self) -> str:
        return "arialbd_3.ttf"


@fixture
def file():
    yield Path('Animes') / 'One Punch Man' / 'One Punch Man 01.mkv'


@fixture
def file2():
    yield Path('Animes') / 'One Punch Man' / 'One Punch Man 02.mkv'


def test_PathManager_com_SubtitleTrack(file):
    expect = '2_One Punch Man 01_Brazilian_CR(pt-BR).ass'

    sub = FakeSubtitleTrack()

    patman = PathManager(file)
    path = patman.path_from(sub)
    assert str(path) == expect


def test_PathManager_com_SubtitleTrack_sem_track_name(file):
    expect = '2_One Punch Man 01_(pt-BR).ass'

    sub = FakeSubtitleTrack()
    sub.track_name = lambda: ''

    patman = PathManager(file)
    path = patman.path_from(sub)
    assert str(path) == expect


def test_PathManager_com_SubtitleTrack_com_id_diferente(file):
    expect = '3_One Punch Man 01_Brazilian_CR(pt-BR).ass'

    sub = FakeSubtitleTrack()
    sub.id = lambda: 3

    patman = PathManager(file)
    path = patman.path_from(sub)
    assert str(path) == expect


def test_PathManager_com_SubtitleTrack_sem_language_ietf(file):
    expect = '2_One Punch Man 01_Brazilian_CR(por).ass'

    sub = FakeSubtitleTrack()
    sub.language_ietf = lambda: 'und'

    patman = PathManager(file)
    path = patman.path_from(sub)
    assert str(path) == expect


def test_PathManager_com_SubtitleTrack_sem_language_ietf_e_sem_language(file):
    expect = '2_One Punch Man 01_Brazilian_CR(und).ass'

    sub = FakeSubtitleTrack()
    sub.language = lambda: 'und'
    sub.language_ietf = lambda: 'und'

    patman = PathManager(file)
    path = patman.path_from(sub)
    assert str(path) == expect


def test_PathManager_com_SubtitleTrack_sem_track_name_sem_language_ietf_e_sem_language(file):
    expect = '2_One Punch Man 01_(und).ass'

    sub = FakeSubtitleTrack()
    sub.track_name = lambda: ''
    sub.language = lambda: 'und'
    sub.language_ietf = lambda: 'und'

    patman = PathManager(file)
    path = patman.path_from(sub)
    assert str(path) == expect


def test_PathManager_com_SubtitleTrack_episode2(file2):
    expect = '2_One Punch Man 02_Brazilian_CR(pt-BR).ass'

    sub = FakeSubtitleTrack()

    patman = PathManager(file2)
    path = patman.path_from(sub)
    assert str(path) == expect


def test_PathManager_com_SubtitleTrack_str(file):
    expect = '2_One Punch Man 01_Brazilian_CR(pt-BR).srt'

    sub = FakeSubtitleTrack()
    sub.codec_id = lambda: 'S_TEXT/UTF8'

    patman = PathManager(file)
    path = patman.path_from(sub)
    assert str(path) == expect


def test_PathManager_com_AttachmentTrack(file):
    expect = 'fonts/arialbd_3.ttf'

    attach = FakeAttachment()

    patman = PathManager(file)
    path = patman.path_from(attach)
    assert str(path) == expect


def test_PathManager_com_valor_desconhecido(file):
    expect = "Tipo inesperado 'dict' para geração de caminho. Esperado 'ITrack' ou 'IAttachment'."

    with raises(TypeError) as excinfo:
        patman = PathManager(file)
        patman.path_from({})

    result = str(excinfo.value)
    assert expect == result
