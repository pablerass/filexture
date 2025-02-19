import pytest
import random
import shutil
import tempfile
import uuid

from collections.abc import Callable, Generator
from pathlib import Path
from PIL import Image


Size = tuple[int | float, int | float] | list[int | float]


@pytest.fixture
def random_image() -> Callable[[Size], Image.Image]:
    def create_image(size: Size | None = None) -> Image.Image:
        aspect_ratio = random.choice([(3, 2), (4, 3)])
        if size is None:
            width = random.randint(300, 1000)
            height = int(width * aspect_ratio[1] / aspect_ratio[0])
        else:
            width = int(size[0])
            height = int(size[1])

        return Image.new('RGB', (width, height), color=(255, 0, 0))

    return create_image


@pytest.fixture
def random_image_file(random_image) -> Generator[Callable[[Path, Size], Path], None, None]:
    temp_dir = Path(tempfile.mkdtemp())

    def create_temp_file(subpath: Path | None = None, size: Size | None = None) -> Path:
        file_name = f"{uuid.uuid4()}.png"
        if subpath:
            full_subpath = temp_dir / subpath
            full_subpath.mkdir(parents=True, exist_ok=True)
            temp_file = full_subpath / file_name
        else:
            temp_file = temp_dir / file_name

        random_image(size).save(temp_file)

        return temp_file

    yield create_temp_file

    if temp_dir.exists():
        shutil.rmtree(temp_dir)
