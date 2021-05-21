#!/usr/bin/env python3
import json
import cgi
from spel import play

# Lees data verstuurd door JavaScript
parameters = cgi.FieldStorage(keep_blank_values=1)

guesses = parameters.getvalue('guesses')
pattern = parameters.getvalue('pattern')
mistakes = int(parameters.getvalue('mistakes'))
letter = parameters.getvalue('letter')


# Bereken te verzenden data
new_data = play(guesses, pattern, mistakes, letter)

# Stuur antwoord terug
print("Content-Type: application/json")
print()
print(json.dumps(new_data))
