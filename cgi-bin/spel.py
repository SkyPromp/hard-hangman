import json

from galgje import Galgje


# run the game and retrieve the data from the next letter
def play(guesses, pattern, mistakes, letter):
    return json.loads(Galgje(guesses, pattern, mistakes).play(letter))
