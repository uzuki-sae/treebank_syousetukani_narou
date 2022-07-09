import sys
import json
from treelib import Node, Tree
from tqdm import tqdm
from build_tree import build_tree

def tree_read(n):
    with open('test.json', 'r') as corpus:
        tree_json = json.load(corpus)

    tokens = tree_json[n]
    tree = build_tree(tokens)
    tree.show(idhidden = True, key=lambda x: int(x.identifier))

    return tree

if __name__ == '__main__':
    tree_read(sys.argv[1])

