"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:

    def __init__(self, filepath):
        """ this is the class constructor it builds out the filepath, wordlist and file variables"""
        self.filepath = filepath
        self.wordlist = []

        """Opens file and reads it"""

        self.file = open(self.filepath, "r")

        """Loops through the file line by line and appends to empty list then prints an F string"""

        for line in self.file:
            self.wordlist.append(line)

        print(f"{len(self.wordlist)} words read")

    def random(self):
        """prints a random word from the wordlist"""

        print(random.choice(self.wordlist))

    ...


class SpecialWordFinder(WordFinder):

    """extends WordFinder and adds the extra functionality that removes any empty line and any
    comment lines"""

    def __init__(self, filepath):
        self.filepath = filepath
        self.wordlist = ""
        self.file = open(self.filepath, "r+")
        for line in self.file:
            if not line.isspace() and not line.startswith("#"):
                self.wordlist += line
        print(self.wordlist.strip())
