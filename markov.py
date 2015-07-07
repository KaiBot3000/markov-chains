#import sys


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    # loop through words
    # make tuple bigrams
    bigrams = {}
    word_list = corpus.split(" ")
    word_count = len(word_list)
    print word_count
    # i = 0 # corpus index
    # for words in corpus:
    #     word_count += 1

    # while i < word_count:
    #     bigram_tuple = (corpus[i], corpus[(i + 1)])
    #     bigrams[bigram_tuple] = []
    #     i += 1

    # print bigrams

    # if loop to generate values list
        # loops over words starting at thrid word
        # append word to list of tuple matching previous two words

    return {}


# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# # Change this to read input_text from a file, deciding which file should
# # be used by examining the `sys.argv` arguments (if neccessary, see the
# # Python docs for sys.argv)

# open and process text into single string
input_text = open("green-eggs.txt")
input_string = ""
for line in input_text:
    input_string += line.replace("\n", " ")
print type(input_string)
# Get a Markov chain
chain_dict = make_chains(input_string)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
