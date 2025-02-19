import pytest

from pathlib import Path

pytest.register_assert_rewrite("filexture.basic")
pytest_plugins = ["filexture.basic"]
from filexture import basic     # noqa: E402


def test_filexure_returns_correct_path(filexture):
    rel_path = "dummy.txt"
    expected = basic.TEST_FILES_PATH / rel_path
    result = filexture(rel_path)
    assert isinstance(result, Path)
    assert result == expected


def test_filexture_content_reads_correctly(filexture_content):
    # Ensure the test directory exists.
    basic.TEST_FILES_PATH.mkdir(exist_ok=True)
    test_file = basic.TEST_FILES_PATH / "temp_test.txt"
    expected_content = "Sample content for testing."
    test_file.write_text(expected_content)

    try:
        # Use the fixture to read the content.
        content = filexture_content("temp_test.txt")
        assert content == expected_content
    finally:
        # Clean up the temporary file.
        if test_file.exists():
            test_file.unlink()
