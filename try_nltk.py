from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
grammar = CFG.fromstring(demo_grammar)

print(len(list(generate(grammar, n=500))))
for sentence in generate(grammar, n=500):
        print (' '.join(sentence))