from ufo import ufo

noun_file = open("nouns.txt", "r")
content = noun_file.read()
noun_list = content.split("\n")
noun_file.close()

msg_file = open("messages.txt", "r")
content = msg_file.read()
msg_list = content.split("\n")
msg_file.close()

print(noun_list)
# print(msg_list)