# import nltk
# from nltk import CFG
# sentence = """I did not feel very well that morning."""
# tokens = nltk.word_tokenize(sentence)
# print(tokens)
# tagged = nltk.pos_tag(tokens)
# print(tagged)

# grammar = CFG.fromstring(tagged)
# print(grammar)


import nltk
from collections import defaultdict

tag_dict = defaultdict(list)

""" (Looping through sentences) """

# Tag
tagged_sent = nltk.pos_tag(tokens)

# Put tags and words into the dictionary
for word, tag in tagged_sent:
    if tag not in tag_dict:
        tag_dict[tag].append(word)
    elif word not in tag_dict.get(tag):
        tag_dict[tag].append(word)

# Printing to screen
for tag, words in tag_dict.items():
    print(tag, "->")
    first_word = True
    for word in words:
        if first_word:
            print("\"" + word + "\"")
            first_word = False
        else:
            print("| \"" + word + "\"")
    print('')