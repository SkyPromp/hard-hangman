#!/usr/bin/python3
import json
import random
import re
import string


class Galgje:
    def __init__(self, guesses, pattern, mistakes):

        # import all the words
        words = open("woorden.txt").read().splitlines()

        # letters that already have been guessed
        self.guesses = set(guesses)

        # incorrect guesses
        self.mistakes = mistakes

        # set default (empty) pattern
        if pattern != "":
            self.pattern = pattern
        else:
            self.pattern = "." * len(random.choice(words))

        # set initial wordlist to all words of the same length as the pattern
        self.words = []
        for word in words:
            if len(word) == len(self.pattern):
                self.words.append(word)
        if pattern != "."*len(pattern) or guesses != "":
            self.words = self.getMatchingWords()

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
                self.pattern = random.choice(max_patterns)

            else:
                self.mistakes += 1

            self.words = self.getMatchingWords()
            return self.pattern
        raise AssertionError("No words with this pattern")

    def play(self, letter):
        if letter not in string.ascii_letters:
            raise AssertionError("Invalid character(s), must be 1 character in the alphabet")

        return json.dumps({"pattern": self.mostPossibilities(letter.upper()),
                           "guesses": ' '.join(sorted(self.guesses)).replace(" ", ""),
                           "mistakes": self.mistakes})

    def getPattern(self):
        if self.guesses != set():
            return self.pattern.replace(".", f"[^{' '.join(self.guesses)}]")
        return self.pattern
