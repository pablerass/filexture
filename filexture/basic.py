import pytest

from collections.abc import Callable
from pathlib import Path


_FILEXTURE_FOLDER = "filextures"


# TODO: Add a process to search folder in other parent locations or where conftest is placed
def _find_filexture_folder(test_path: Path | str, folder_name: str = _FILEXTURE_FOLDER) -> Path:
    return Path(test_path).parent / folder_name


@pytest.fixture
def filexture(request) -> Callable[[Path | str], Path]:
    test_file_path = _find_filexture_folder(request.node.fspath)

    def path(rel_path: Path | str) -> Path:
        return test_file_path / rel_path

    return path


@pytest.fixture
def filexture_content(filexture) -> Callable[[Path | str], str]:
    def path(rel_path: Path | str) -> str:
        return filexture(rel_path).read_text()

    return path
