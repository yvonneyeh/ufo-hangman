import random 
from ufo import ufo

# NOUN LIST
noun_file = open("nouns.txt", "r")
content = noun_file.read()
noun_list = content.split("\n")
noun_file.close()

# MESSAGE LIST
msg_file = open("messages.txt", "r")
content = msg_file.read()
msg_list = content.split("\n")
msg_file.close()

# print(noun_list)
# print(msg_list)
# print(ufo[0])

def get_word():
    """ Randomly selects playable word from noun list. """

    word = random.choice(noun_list)
    while '-' in word or ' ' in word or word == '':
        word = random.choice(noun_list)
    # print(word.upper())
    return word.upper()
    
def play_ufo():
    pass

if __name__ == '__main__':
    get_word()
    # play_ufo()