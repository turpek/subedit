from pytest_mock import mocker
from subedit.subedit import main, subtitle_remove
from pathlib import Path
from pytest import fixture
import pytest


@fixture
def subrem(mocker, output_dir: str):
    dir_mock = mocker.patch('subedit.subedit.check_output')
    remove_mock = mocker.patch('subedit.subedit.subtitle_remove')
    remove_mock.return_value = Path(output_dir)
    arg = mocker.Mock()
    yield arg, remove_mock


@fixture
def subrem_task(mocker, output_dir: str):
    mocker.patch('subedit.subedit.check_output')
    remove_task_mock = mocker.patch('subedit.subedit.subtitle_remove_task')
    remove_task_mock.return_value = Path(output_dir)
    arg = mocker.Mock()
    arg.file = ''
    arg.files = []
    arg.directory = False
    yield arg, remove_task_mock


@pytest.mark.parametrize("output_dir", ["output"])
def test_subtitle_remove_not_call(subrem):
    arg, remove_mock = subrem
    arg.subtitle_remove = False
    main(arg)
    assert not remove_mock.called


@pytest.mark.parametrize("output_dir", ["output"])
def test_subtitle_remove_call(subrem):
    arg, remove_mock = subrem
    arg.subtitle_remove = True
    main(arg)
    assert remove_mock.called


@pytest.mark.parametrize("output_dir", ["output"])
def test_subtitle_remove_not_call(subrem):
    arg, remove_mock = subrem
    arg.subtitle_remove = False
    main(arg)
    assert not remove_mock.called


@pytest.mark.parametrize("output_dir", ["output"])
def test_subtitle_file_worker(subrem_task):
    arg, remove_task_mock = subrem_task
    arg.file = 'anime_title 02.mkv'
    subtitle_remove(arg)
    assert remove_task_mock.called


@pytest.mark.parametrize("output_dir", ["output"])
def test_subtitle_file_worker_not_call(subrem_task):
    arg, remove_task_mock = subrem_task
    subtitle_remove(arg)
    assert not remove_task_mock.called
