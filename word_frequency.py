import string
import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def normalize_text(text):
    """
    Given a text, lowercases it, removes all punctuation, 
    and replaces all whitespace with normal spaces. Multiple whitespace will
    be compressed into a single space.
    """
    text = text.casefold()
    # valid_chars = re.sub(r"[^a-zA-Z]"," ",text)
    valid_chars = string.ascii_letters + string.whitespace + string.digits

    # Remove all punctuation
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char

    text = new_text
    text = text.replace("\n", " ")
    return text


def print_word_freq(filename):
    """Read in `filename` and print out the frequency of words in that file."""
    with open(filename) as file:
        text = file.read()

    text = normalize_text(text)
    words = []
    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS:
            words.append(word)

    ind_words = []
    for word in words:
        if word not in ind_words:
            ind_words.append(word)

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else: 
            word_freq[word] = 1

    # print(word_freq)

    # print(sorted(word_freq.values(), reverse=True))

    # for value in word_freq.items():\

    # for value in word_freq.values():
    #     sorted(value, reverse=True)

    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_word_freq)

    sorted_dict = dict(sorted_word_freq)
    # print(sorted_dict)

        
    # for key, value in word_freq.items():
    #     print(value, key)

    for key, value in sorted_dict.items():
        # sorted(word_freq.items(), key=lambda x: x[1])
        # value = sorted(value, reverse = True)
        print(key, "|", value, "*" * value)


    
    # sorted_words = sorted(word_freq.values(), reverse=True)

    # for sortedkey in sorted_words:
    #     for key, value in word_freq.items():
    #         if value == sortedkey:
    #            sorted_word_freq[key]



    # for sorted_word_freq in sorted(word_freq.values(), reverse=True):
    #     print(sorted_word_freq)
            



            ## What now?
    # Get a dictionary of word frequencies and print it out




if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)