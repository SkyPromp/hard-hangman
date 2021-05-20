#!/usr/bin/env python3
import json
import cgi
from spel import play

# Lees data verstuurd door JavaScript
parameters = cgi.FieldStorage();
data = json.loads(parameters.getvalue('data'));
letter = parameters.getvalue('letter');

# Bereken te verzenden data
#nieuwe_lijst = voeg_toe(data["lijst"], waarde);

                # pattern, guesses, mistakes
nieuwe_data = play(data[0], data[1], data[2], letter)

# Stuur antwoord terug
print("Content-Type: application/json")
print() # Lege lijn na headers
print(json.dumps(nieuwe_data))