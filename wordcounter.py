import re
from collections import Counter

def main():
    filename = input("Enter file name: ")
    infile = open(filename,'r')
    words = infile.read().lower()
    word_counter = words.split()
    most_common = Counter(word_counter).most_common(10)
    numOfChars = len(words)
    numOfWords = len(word_counter)
    numOfLines = len(words.splitlines())
    print("Characters: %i\nWords: %i\nLines: %i" % (numOfChars, numOfWords, numOfLines))
    print("The most common words are {0}".format(most_common))
               
main()
