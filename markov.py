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

    text_string.append(None)
    #for loop - i range(len(i - 2)) <-- make sure to stay in range
    for i in range(len(text_string)-2):
    #(first word [i] and second word [i+1]) - tuple
        tuple_key = (text_string[i], text_string[i + 1])

        #dict.get(key, []) concatenate(+) following word bc .append() returns NONE
        #following word[i+2] --> appended into empty list
        chains[tuple_key] = chains.get(tuple_key,[]) + [text_string[i + 2]]
    return chains

#print(make_chains(open_and_read_file('green-eggs.txt')))


def make_text(chains):
#     """Return text from chains."""

    first_key = choice(list(chains.keys()))
    words = [first_key[0], first_key[1]]

    # tuple_key = chains.keys()
    random_word = choice(chains[first_key])
    #print(random_word)

    while random_word is not None:
        words.append(random_word)
        new_key = (words[-2], random_word)
        random_word = choice(chains[new_key])



    #for every key in the chains dictionary, grab the 1st index in that key + random word in that key's value list, then create a tuple out of the aforementioned and rebind it to a new variable 

    #while random_word is not None:
        #print(tuple_key, list_value)
        #new_key = (tuple_key[1], choice(random_word))
        #print(new_key)
        # if new_key in chains:
        #     random_word = choice(chains[new_key])
        #     words.append(random_word)
        #     tuple_key = new_key
        #break
            
    
    # for tuple_key in chains.items():
    #     if new_key == tuple_key:
    #         new_key[1], choice()

    #search for the new tuple variable in keys! 
    #REPEAT UNTIL 'sam i am?' or no longer in dictionary 

    #WANT TO RETURN!! 
    return " ".join(words)





# def make_text(chains):
#     """Return text from chains."""

#     key = choice(list(chains.keys()))
#     words = [key[0], key[1]]
#     word = choice(chains[key])

#     # Keep looping until we reach a value of None
#     # (which would mean it was the end of our original text)
#     # Note that for long texts (like a full book), this might mean
#     # it would run for a very long time.

#     while word is not None:
#         key = (key[1], word)
#         words.append(word)
#         word = choice(chains[key])

#     return " ".join(words)



#print(make_text(make_chains(open_and_read_file('green-eggs.txt'))))

import sys

print(sys.argv)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
