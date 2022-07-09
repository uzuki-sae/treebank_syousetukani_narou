import json
from tqdm import tqdm
import os
import spacy
nlp = spacy.load('ja_ginza')
infile = "your text path"
with open(infile, 'r') as inf:
    text = inf.readlines()
with open('word_key.json', 'w') as word_key_file:
    w_keys = {}


def make_wk(words, i, w_keys):
    for word in words:

        if word in w_keys.keys():
            if i in w_keys[word]:
                pass
            else:
                w_keys[word].append(i)

        
        else:
            w_keys[word] = [i, ]
    
    return w_keys

i = 0
tree_json = {}

for line in tqdm(text):
    doc = nlp(line[:-1])

    for sent in doc.sents:
        i = i + 1
        tokens = {}
        words = []

        for token in sent:
            n = {}
            n["head"] = token.head.i
            n["dep"] = token.dep_
            n["pos"] = token.pos_
            n["orth"] = token.orth_
            tokeni = token.i
            tokens[tokeni] = n
            words.append(token.lemma_)
            
        tree_json[i] = tokens
#        w_keys = make_wk(words, i, w_keys)


#print(w_keys)
        
print(tree_json)


#with open('word_key.json', 'w') as word_key_file:
#    wkf =  json.dump(w_keys, word_key_file, indent = 4)
#    print(wkf)
with open('tree.json','a') as outf:
    tjf = json.dump(tree_json, outf, indent = 4)
