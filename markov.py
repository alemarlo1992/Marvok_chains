"""Generate Markov text from text files."""

from random import choice



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    content = open("green-eggs.txt").read()
    # your code goes here
    # print(content)
    # return "Contents of your file as one long string"
    return content
# print(open_and_read_file("green-eggs.txt"))

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()
    # bigrams = ()
    # trailing_words = []


    for i in range(len(words)-2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        # check_existing_key = chains.get(single_pair, 0)
        # if check_existing_key == 0:
        #if key not in dictionary:
        if key not in chains:
            chains[key] = []
        #append value to the list
        chains[key].append(value)
        
    # for key, value in chains.items():
    #     print(key, value)
    # print(chains)


    return chains

input_text = open_and_read_file("green-eggs.txt")
print(make_chains(input_text))


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
