import pytest

from collections.abc import Callable
from pathlib import Path


TEST_PATH = Path(__file__).resolve().parent
TEST_FILES_PATH = Path(__file__).resolve().parent / "files"


@pytest.fixture
def filexture() -> Callable[[Path | str], Path]:
    def path(rel_path: Path | str) -> Path:
        return TEST_FILES_PATH / rel_path

    return path


@pytest.fixture
def filexture_content() -> Callable[[Path | str], str]:
    def path(rel_path: Path | str) -> str:
        return (TEST_FILES_PATH / rel_path).read_text()

    return path
