import sudachipy
import sys

dic = sudachipy.Dictionary()
tokenizer = dic.create()

def lemma(keys):
    morpheme = tokenizer.tokenize(keys)
    key = {m.normalized_form() for m in morpheme if m.normalized_form() != '|'}
     

    return key

if __name__ == '__main__':
    print(lemma(sys.argv[1]))
    
