# hard-hangman
Just a game of hangman, but the odds are stacked against you

(only works with bash)

In this verion of hangman, the word is variable. This means that when the player chooses a letter, the pattern of the word will change to a pattern with the most possibilities.
e.g. image that you have a 3 letter word.
_ _ _

and lets immagine that the list of possible words is:
-sag
-bag
-alt
-egg
-sip

and now lets imagine that the player chooses the letter "a".

the words with the letter "a" are:
-sag
-bag
-alt
and the words without the letter "a" are:
-egg
-sip

So now there are 3 possible patterns:
_ a _ 2x
a _ _ 1x
_ _ _ 2x

The first and last pattern both occur twice, so the algorithm will choose one of those two at random, but since in the last pattern the a does not occur, the algoritm will prioritize the pattern "_ _ _".
This will happen until the pattern only matches a single word and if the player guesses that word the player wins.

If the player wins, the player gets sent to a winning screen and the player can choose to play another game.
If the player looses, the player gets sent to a losing screen and the player can choose to play another game.


The wordlist of the game is included, this list is in dutch, but you could easily add another wordlist of any other language that uses the roman alphabet with 26 letters.
