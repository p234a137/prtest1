import sys
from collections import Counter

# get file name from arguments and open file
fname = sys.argv[1]
fp = open(fname, 'r')

# create a list of words and use a counter
words = []
for line in fp:
    for word in line.split():
        words.append(word)
word_cts = Counter(words)

# calculate how many to print since we want several words with same frequency printed
ctsl = sorted(word_cts.values()) # list of sorted counts
cts = list(set(sorted(word_cts.values()))) # cast to set and back to get unique counts
ix = ctsl.index(cts[-10]) # lowest index you need to go to
how_many = len(ctsl) - ix
for word, ct in word_cts.most_common(how_many):
    print word, ct

# close file
fp.close()
