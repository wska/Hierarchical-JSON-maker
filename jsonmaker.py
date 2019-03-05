import csv
from collections import defaultdict
import json
import sys

def ctree():
    return defaultdict(ctree)


def build_leaf(name, leaf):
    res = {"name": name}

    # add children node if the leaf actually has any children
    if len(leaf.keys()) > 0:
        item = next(iter(leaf.items())) # Fetches an arbitary item from the dict items. Used to check if we have reached the end-node.
        k,v = item
    
        if len(v.keys()) > 0: # If the leaf of the leaf has keys, continue branching children recursively.
            res["children"] = [build_leaf(k, v) for k, v in leaf.items()]
            
        else: # Else if leaf of leaf has no keys, it is an end node and thus we want to put the value into the last node.
            res = {"name" : name, "value" : k}

    return res
    

def main():
    fileName = sys.argv[1]
    tree = ctree()
    with open(str(fileName)) as csvfile:
        reader = csv.reader(csvfile)
        for rowid, row in enumerate(reader):
            # skipping first header row. Remove is the csv contains no headers.
            if rowid == 0:
                continue
            leaf = tree[row[0]]

            for columnid in range(1, len(row)):    
                leaf = leaf[row[columnid]]

   
    res = []
    for name, leaf in tree.items():
        res.append(build_leaf(name, leaf))
 
    print(json.dumps(res[0])) # [0] indexing is just to remove the outer array-brackets. Remove if you want the output as an array instead.

main()