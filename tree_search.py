import sys
import json
from treelib import Node, Tree
from tqdm import tqdm
from build_tree import build_tree
from lemma import lemma
from time import time


st = time()
with open('tree.json', 'r') as corpus:
    tree_json = json.load(corpus)
ft = time()
print(f'read time:{ft - st}s')


def get(number):
    if not number:
        print("No such a sentence, sorry.")
    else:
        for n in number:
            tokens = tree_json[n]
            tree = build_tree(tokens)
            print(f'ID={n}')
            tree.show(idhidden = True, key=lambda x: int(x.identifier))
def string(string):
    key = lemma(string)
    print("wordkey")
    print(key)
    number = {}
    number = set(tree_json.keys())
        
    for k in key:
        single = set()
        for n in tree_json:
            for token in tree_json[n]:
                if k == tree_json[n][token]["lemma"]:
                    single.add(n)
                else:
                    pass

        number = number & single

    get(number)

def exist(arg1, arg2):
    number = set()
    for n in tree_json:
        for token in tree_json[n]:
            if [arg1 in tree_json[n][token].values()] and [arg2 in tree_json[n][token].values()]:
                number.add(n)
            else:
                pass
    return number

def dominate(arg1,arg2,reverse=False):
    number = set()
    for n in exist(arg1, arg2):
        tokens = tree_json[n]
        tree = build_tree(tokens)
        for i in tree.expand_tree():
            if tree[i].tag == arg1:
                for j in tree.expand_tree():
                    if tree[j].tag == arg2:
                        if reverse == False:
                            if tree.is_ancestor(i,j):
                                number.add(n)
                            else:
                                pass
                        else:
                            if tree.is_ancestor(j, i):
                                number.add(n)
                            else:
                                pass
                    else:
                        pass
            else:
                pass

         

    return number


def depend(arg1, arg2, reverse = False):
    number = set()
    for n in tree_json:
        for i in tree_json[n]:
            if arg1 in tree_json[n][i].values():
                for j in tree_json[n]:
                    if arg2 in tree_json[n][j].values():
                        if reverse == False:
                            if str(tree_json[n][i]["head"]) == j:
                                number.add(n)
                            else:
                                pass
                        else:
                            if str(tree_json[n][j]["head"]) == i:
                                number.add(n)
                            else:
                                pass
                    else:
                        pass
            else:
                pass

                
    return number


def syster(arg1, arg2):
    number = set()
    for n in exist(arg1, arg2):
        tokens = tree_json[n]
        tree = build_tree(tokens)
        for i in tree.expand_tree():
            if tree[i].tag == arg1:
                for j in tree.expand_tree():
                    if tree[j].tag == arg2:
                        if tree.parent(i) == tree.parent(j):
                            number.add(n)
                        else:
                            pass
                    else:
                        pass
            else:
                pass

    return number


def onetwo(arg1, arg2, reverse=False):
    number = set()
    for n in exist(arg1, arg2):
        for i in tree_json[n]:
            if arg1 in tree_json[n][i].values():
                for j in tree_json[n]:
                    if arg2 in tree_json[n][j].values():
                        if reverse==True:
                            if int(i) > int(j):
                                number.add(n)
                            else:
                                pass
                        else:
                            if int(i) < int(j):
                                number.add(n)
                            else:
                                pass
                    else:
                        pass

            else:
                pass

    return number








if __name__ == '__main__':

    st = time()
    string(sys.argv[1])
#    get(depend("ADP","NOUN"))
    ft = time()
    print(f'operate time:{ft - st}s')


