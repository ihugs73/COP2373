import re


def split_into_sentences(paragraph: str) -> list:
    """
    Splits the provided paragraph into sentences using a regex.
    Then merges any isolated numeric markers (e.g., '1.') with the following sentence.

    Args:
        paragraph (str): The input paragraph as a string.

    Returns:
        list: A list of sentences.
    """
    # Split on punctuation (.!? followed by whitespace) while keeping punctuation with sentence
    raw_sentences = re.split(r'(?<=[.!?])\s+', paragraph.strip())

    # Merge segments that are just a number with a dot with the following sentence.
    merged_sentences = []
    i = 0
    while i < len(raw_sentences):
        sentence = raw_sentences[i]
        # Check if sentence is just a number followed by a period.
        if re.fullmatch(r'\d+\.', sentence) and (i + 1) < len(raw_sentences):
            # Merge with the following sentence.
            sentence = sentence + " " + raw_sentences[i + 1]
            i += 2  # Skip the next one since it's merged.
        else:
            i += 1
        merged_sentences.append(sentence)
    return merged_sentences


def display_sentences(sentences: list):
    """
    Displays each sentence along with its index, then prints the total count.

    Args:
        sentences (list): A list of sentences.
    """
    for index, sentence in enumerate(sentences, start=1):
        print(f"Sentence {index}: {sentence}")
    print(f"\nTotal number of sentences: {len(sentences)}")


def main():
    """
    Main function to prompt the user, split the paragraph into sentences, and display them.
    """
    paragraph = input("Enter a paragraph: ")
    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)


if __name__ == "__main__":
    main()
