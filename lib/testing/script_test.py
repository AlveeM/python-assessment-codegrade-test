import pytest
import script


class TestReadTextFile:
    def test_read_text_file(self, tmp_path):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text("Hello, World!")

        assert script.read_text_file(str(p)) == "Hello, World!"


class TestCountSpecificWord:
    @pytest.mark.parametrize(
        "text, word, expected",
        [
            ("This is a test. This is only a test.", "test", 2),
            ("apple apple banana banana banana", "banana", 3),
            ("", "test", 0),
        ],
    )
    def test_count_specific_word_parametrized(self, text, word, expected):
        assert script.count_specific_word(text, word) == expected


class TestIdentifyMostCommonWord:
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("This is a test. This is only a test.", "this"),
            ("apple apple banana banana banana", "banana"),
            ("", None),
        ],
    )
    def test_identify_most_common_word_parametrized(self, text, expected):
        assert script.identify_most_common_word(text) == expected


class TestCalculateAverageWordLength:
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("This is a test.", 2.75),
            ("apple apple banana banana banana", 5.6),
            ("", 0),  # Test with empty string
        ],
    )
    def test_calculate_average_word_length_parametrized(self, text, expected):
        assert script.calculate_average_word_length(text) == expected


class TestCountParagraphs:
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("This is a test.\n\nThis is only a test.", 2),
            ("apple apple banana\n\nbanana banana\n\nbanana", 3),
            ("", 1),  # Test with empty string
        ],
    )
    def test_count_paragraphs_parametrized(self, text, expected):
        assert script.count_paragraphs(text) == expected


class TestCountSentences:
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("This is a test. This is only a test.", 2),
            ("Hello world. How are you? I'm fine, thanks.", 3),
            ("", 0),
        ],
    )
    def test_count_sentences_parametrized(self, text, expected):
        assert script.count_sentences(text) == expected
