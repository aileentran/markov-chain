"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    """Contents of your file as one long string"""

    text_file = open(file_path).read().split()

    return text_file



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

    #thoughts! 

    #input: ENTIRE string text in list 
    #output: dictionary - tuples(key): list of following word(value)

    #text_string = open_and_read_file(file_path)
    chains = {}
    #for loop - i range(len(i - 2)) <-- make sure to stay in range
    for i in range(len(text_string)-2):
    #(first word [i] and second word [i+1]) - tuple
        tuple_key = (text_string[i], text_string[i + 1])

        #dict.get(key, []) concatenate(+) following word bc .append() returns NONE
        #following word[i+2] --> appended into empty list
        chains[tuple_key] = chains.get(tuple_key,[]) + [text_string[i + 2]]
    
    #outside of loop
    #return dictionary!
    return chains

print(make_chains(open_and_read_file('green-eggs.txt')))


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
