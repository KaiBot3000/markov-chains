#import sys
import random

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    bigrams = {}
    word_list = corpus.split(" ")
    word_count = len(word_list)
    i = 0 # word_list index counter for bigrams
    j = 3 # word_list counter for values

    # Makes bigram keys for dictionary, from word_list
    while i < (word_count - 1):
        bigram_tuple = (word_list[i], word_list[(i + 1)])
        bigrams[bigram_tuple] = []
        i += 1

    # adds values to bigram keys in dictionary
    while j < word_count:
        bigrams[(word_list[j - 2], word_list[j - 1])].append(word_list[j])
        j += 1

    return bigrams


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    # select random key to start
    text = ""
    start_bigram = random.choice(chains.keys()) # choose random tuple key

    while start_bigram in chains:
        #append key to return string
        text += start_bigram[1] + " " + start_bigram[2] + " "
        #select random value from list based on previous bigram
        #new bigram, select random value from list based on previous bigram
            # loop until bigram not found




    return "Here's some random text."




# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# open and process text into single string
input_text = open("green-eggs.txt")
input_string = ""
for line in input_text:
    input_string += line.replace("\n", " ")

# Get a Markov chain
chain_dict = make_chains(input_string)


# Produce random text
random_text = make_text(chain_dict)

# print random_text
