#!/usr/bin/python3
"""
Module containing the text_indentation function
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each
    occurrence of '.', '?', and ':' characters.

    Args:
        text: String input.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence = text[:]

    for punctuation in ".?:":
        phrases = sentence.split(punctuation)
        sentence = ""
        for phrase in phrases:
            # Remove leading and trailing spaces from each phrase
            phrase = phrase.strip()
            sentence = f"{phrase}{punctuation}" if not sentence else f"{sentence}\n\n{phrase}{punctuation}"

    print(sentence[:-3], end="")
