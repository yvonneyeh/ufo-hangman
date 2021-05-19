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


### About the Developer

[**Yvonne Yeh**](http://yvonneyeh.com/) is a software engineer from the Silicon Valley who has never seen the show. Curiosity, creativity, and a love of learning are at the root of everything Yvonne does. She loves that coding because it's an art form, it tickles her brain in the same spot as designing does. Before she learned how to code, she worked in K-12 education, design, and mental/physical fitness. Her personal coding journey began when she was learning alongside her 3rd grade students; she helped introduce **Hour of Code** and **Computer Science Week** into her school’s permanent curriculum. From there she dove into self-study with Scratch, CS50x, Python 4 Everybody, YouTube videos, and Codecademy. She is currently the **Chapter Leader** of [Codecademy's Silicon Valley Chapter](https://community.codecademy.com/silicon-valley/).