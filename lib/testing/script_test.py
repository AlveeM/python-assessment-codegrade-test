import pytest
from script import read_text_file, count_specific_word, identify_most_common_word


def test_read_text_file(tmp_path):
    # Create a temporary text file
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("Hello, World!")

    # Test the read_text_file function
    assert read_text_file(str(p)) == "Hello, World!"


def test_count_specific_word():
    text = "This is a test. This is only a test."
    word = "test"
    assert count_specific_word(text, word) == 2


def test_identify_most_common_word():
    text = "This is a test. This is only a test."
    assert identify_most_common_word(text) == "this"


@pytest.mark.parametrize(
    "text, expected",
    [
        ("This is a test. This is only a test.", "this"),
        ("apple apple banana banana banana", "banana"),
        ("", None),
    ],
)
def test_identify_most_common_word(text, expected):
    assert identify_most_common_word(text) == expected
