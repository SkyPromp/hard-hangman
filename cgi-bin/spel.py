from galgje import Galgje

def play(guesses, pattern, mistakes, letter):
    return Galgje(guesses, pattern, mistakes).play(letter)

print('')
print(play("", ".......", 0, "a"))
print(play("A", ".......", 1, "e"))
print(play("EA", ".....E.", 1, "o"))
print(play("EAO", ".....E.", 2, "U"))
print(play("EAOU", ".....E.", 3, "I"))
print(play("EAOUI", "..I..E.", 3, "N"))
print(play("EAOUIN", "..I..EN", 3, "K"))


