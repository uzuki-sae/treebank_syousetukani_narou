import json
from treelib import Node, Tree
from tqdm import tqdm
import sys

def build_tree(tokens):
    path = "/uzuki/home/treebank/test.json"

    tree = Tree()
    tree.create_node("IP-MAT", "-1")
    S = ""
    for token in tokens.keys():
        tree.create_node(tokens[token]["dep"], token, parent="-1")
        S += tokens[token]["orth"]

    tree["-1"].tag = S

    for token in tokens.keys():
        if token != str(tokens[token]["head"]):
            tree.move_node(token, str(tokens[token]["head"]))
        else:
            pass


        if not tree[token].is_leaf():
            tree.create_node(tag = tokens[token]["pos"], identifier=f'0{token}', parent = token)
            tree.create_node(tag = tokens[token]["lemma"], identifier=f'00{token}', parent=f'0{token}')

        else:

            tree[token].tag = tokens[token]["pos"]
            tree.create_node(tag=tokens[token]["lemma"], identifier=f'0{token}', parent=token)

    return tree

if __name__ == '__main__':
    sys.exit(build_tree(sys.argv[1]))
