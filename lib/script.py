import re
from collections import Counter
from pathlib import Path


def read_text_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def count_specific_word(text, word):
    word_count = text.lower().count(word.lower())
    return word_count


def identify_most_common_word(text):
    if text == "":
        return None

    words = re.findall(r"\b\w+\b", text.lower())
    common_word = Counter(words).most_common(1)[0][0]
    return common_word


def calculate_average_word_length(text):
    words = re.findall(r"\b\w+\b", text)
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length


def count_paragraphs(text):
    paragraphs = text.split("\n\n")
    return len(paragraphs)


def count_sentences(text):
    sentences = re.split(r"(?<=[.!?]) +", text)
    return len(sentences)


def main():
    file_path = input("Enter the file path: ")
    # Convert the file path string to a Path object
    file_path = Path(file_path)

    # Check if the file exists
    if not file_path.exists():
        print("File not found.")
        return

    text = read_text_file(file_path)

    print("1. Count the number of times a specific word is used in the text.")
    specific_word = input("Enter the word to count: ")
    word_count = count_specific_word(text, specific_word)
    print(f"'{specific_word}' appears {word_count} times in the text.")

    print("\n2. Identify the most common word in the text.")
    most_common_word = identify_most_common_word(text)
    print(f"The most common word in the text is '{most_common_word}'.")

    print("\n3. Calculate the average length of words in the text.")
    average_word_length = calculate_average_word_length(text)
    print(
        f"The average word length in the text is {average_word_length:.2f} characters."
    )

    print("\n4. Count the number of paragraphs in the text.")
    paragraph_count = count_paragraphs(text)
    print(f"There are {paragraph_count} paragraphs in the text.")

    print("\n5. Count the number of sentences in the text.")
    sentence_count = count_sentences(text)
    print(f"There are {sentence_count} sentences in the text.")


if __name__ == "__main__":
    main()
