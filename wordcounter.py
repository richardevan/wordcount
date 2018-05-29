import re
from collections import Counter

def main():
    filename = "wordcount.txt"
    infile=open(filename,'r')
    words = infile.read().lower()
    word_counter = words.split()
    most_common = Counter(word_counter).most_common(5)
    numOfChars = len(words)
    numOfWords = len(words.split())
    numOfLines = len(words.splitlines())
    print("Characters: %i\nWords: %i\nLines: %i" % (numOfChars, numOfWords, numOfLines))
    print("The most common words are {0}".format(most_common))
               
main()
