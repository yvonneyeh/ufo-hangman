# UFO: The Game

Invaders from outer space have arrived and are abducting humans using tractor beams. Earn your medal of honor by cracking the codeword to stop the abduction!

```
                 .
                 |
              .-"^"-.
             /_....._\
         .-"`         `"-.
        (  ooo  ooo  ooo  )
         '-.,_________,.-'   ,-----------.
               /   \        (  Send help! )
              /     \      / `-----------'
             /   O   \    /
            /  --|--  \
           /     |     \
          /     / \     \

```

### Gameplay

To play, run the following in your terminal:
```
python3 game.py
```

Guess one letter at a time of a codeword represented by blank placeholders for each letter. If the letter does not exist in the codeword, the person is pulled in closer to the UFO by the tractor beam. If the letter exists, the blanks that correspond to the position of those letters in the codeword are replaced by the letter. If all the letters of the codeword are revealed before the person is pulled into the UFO, you win. Otherwise, the UFO abducts the person and you lose.

### Game Rules

- All valid codewords are chosen from [this dictionary of English words](https://github.com/Codecademy/internship-code-challenge/blob/master/backend/data/nouns.txt)
- The codeword is represented by a series of dashes, one per letter in the codeword
- The codeword is chosen randomly at the start of the game
- Each game starts with the person at the bottom of the beam. Upon guessing a letter that does not exist in the codeword, the person is lifted one row.
- The distance of the person’s feet to the UFO is six rows, so unless you solve the codeword, you lose on the sixth incorrect guess.
- Every letter that was guessed but does not exist in the codeword is displayed and cannot be guessed again
- Every letter that was guessed that exists in the codeword replaces the dashes for all instances in which they exist in that word
- You win when all the dashes in the codeword have been replaced by your correct guesses


### Design

My original attempt to create this game is located in [`play.py`](https://github.com/yvonneyeh/ufo-hangman/blob/main/play.py), you can see that prior to refactoring, the code wasn't quite DRY and had some repitition in logic. I refactored the code to separate larger functions into smaller, more easily tested components.

#### Opportunities for Improvement:
- Implement hash map for quicker runtime when determining which letters have been guessed already.
- Determining difference between `word_letters` and `guessed_letters` currently in happens in O(n), to refactor this I would create a `valid_characters` set and remove letters as they are guessed to make the lookup O(1).
- Additional unittests.
