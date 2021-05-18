import os
import random
import re
import string


class Galgje:
    def __init__(self):

        # import all the words
        words = open(os.path.split(os.getcwd())[0] + "/woorden.txt").read().splitlines()

        # letters that already have been guessed
        self.guesses = set()

        # set default (empty) pattern
        self.pattern = "." * len(random.choice(words))

        # set initial wordlist to all words of the same length as the pattern
        self.words = []
        for word in words:
            if len(word) == len(self.pattern):
                self.words.append(word)

    # get all the words that match the pattern
    def getMatchingWords(self):
        wordlist = []
        for word in self.words:
            word = word.rstrip()
            if re.fullmatch(self.getPattern(), word):
                wordlist.append(word)

        return wordlist

    def mostPossibilities(self, letter):
        self.guesses.add(letter)
        pattern_count = {}
        for i in self.words:
            i = list(i)
            for j, value in enumerate(i):
                if value != letter and value not in self.guesses:
                    i[j] = "."

            if ", ".join(i).replace(", ", "") in pattern_count:
                pattern_count[", ".join(i).replace(", ", "")] += 1
            else:
                pattern_count[", ".join(i).replace(", ", "")] = 1
        if pattern_count != {}:
            # checks if the old pattern is still one of the patterns with the maximum amount of words, if so, use it
            max_value = max(pattern_count.values())
            max_patterns = [k for k, v in pattern_count.items() if v == max_value]
            if self.pattern not in max_patterns:
                # gets a random pattern with the highest number of words
                self.pattern = random.choice(max_patterns)

            self.words = self.getMatchingWords()
            return self.pattern
        return "no words left"

    def play(self, letter):
        if letter not in string.ascii_letters:
            raise AssertionError("Invalid character(s), must be 1 character in the alphabet")
        print(self.mostPossibilities(letter.upper()).replace(".", "_"))
        print(' '.join(sorted(self.guesses)))

    def getPattern(self):
        return self.pattern.replace(".", f"[^{' '.join(self.guesses)}]")


g = Galgje()
print(g.pattern.replace(".", "_"))

while True:
    g.play(input())
