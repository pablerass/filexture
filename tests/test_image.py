from pathlib import Path
from PIL import Image


pytest_plugins = ["filexture.image"]


def test_random_image(random_image):
    """Test that the random_image fixture returns a valid PIL image."""
    img = random_image((500, 300))

    assert isinstance(img, Image.Image)
    assert img.size == (500, 300)
    assert img.mode == "RGB"


def test_random_image_default_size(random_image):
    """Test that random_image fixture generates an image with random size."""
    img1 = random_image()
    img2 = random_image()

    assert isinstance(img1, Image.Image)
    assert isinstance(img2, Image.Image)
    assert img1 != img2


def test_random_image_file(random_image_file):
    """Test that the random_image_file fixture correctly creates a file."""
    file_path = random_image_file(size=(400, 200))

    assert file_path.exists()
    assert file_path.suffix == ".png"

    img = Image.open(file_path)

    assert img.size == (400, 200)
    assert img.mode == "RGB"


def test_random_image_file_subdirectory(random_image_file):
    """Test that random_image_file can create an image in a subdirectory."""
    subpath = Path("test_subdir")

    file_path = random_image_file(subpath=subpath, size=(300, 150))

    assert file_path.exists()

    img = Image.open(file_path)

    assert img.size == (300, 150)
    assert img.mode == "RGB"
