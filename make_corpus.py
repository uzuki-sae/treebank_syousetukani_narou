import json
from tqdm import tqdm
import os
import spacy
nlp = spacy.load('ja_ginza')
#infile = os.listdir("~/narouAPI/201")
infile = "/home/uzuki/narouAPI/201/N2267BE.txt"
with open(infile, 'r') as inf:
    text = inf.readlines()
with open('word_key.json', 'w') as word_key_file:
    w_keys = {}


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
            n["lemma"] = token.lemma_
            tokeni = token.i
            tokens[tokeni] = n
            
        tree_json[i] = tokens


        
print(tree_json)


#with open('word_key.json', 'w') as word_key_file:
#    wkf =  json.dump(w_keys, word_key_file, indent = 4)
#    print(wkf)
with open('tree.json','w') as outf:
    tjf = json.dump(tree_json, outf, indent = 4)
