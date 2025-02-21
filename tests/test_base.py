from pathlib import Path

pytest_plugins = ["filexture"]


def test_filexure_returns_correct_path(filexture):
    rel_path = "content.txt"
    result = filexture(rel_path)

    print(result)
    assert isinstance(result, Path)
    assert result.name == "content.txt"


def test_filexture_content_reads_correctly(filexture_content):
    # Ensure the test directory exists.
    expected_content = "content"

    content = filexture_content("content.txt")
    assert content == expected_content
