import json

from galgje import Galgje


def play(guesses, pattern, mistakes, letter):
    return json.loads(Galgje(guesses, pattern, mistakes).play(letter))
