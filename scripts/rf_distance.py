#!/usr/bin/env python3
import sys
import os
from ete3 import Tree
import dendropy



def str_4(ll):
  return "{0:.4f}".format(ll)

def ete3_rf(tree1, tree2, unrooted = True):
  if (len(tree2.children) == 3):
    tree2.set_outgroup(tree2.children[0])
  if (len(tree1.children) == 3):
    tree1.set_outgroup(tree1.children[0])
  return tree1.robinson_foulds(tree2, unrooted_trees=unrooted, skip_large_polytomies = True, correct_by_polytomy_size = True)

def get_relative_rf(tree1, tree2, unrooted = True):
  rf = ete3_rf(tree1, tree2, unrooted)
  return float(rf[0]) / float(rf[1])

if (__name__ == "__main__"):
  if (len(sys.argv) < 3):
    print("Syntax python " + os.path.basename(__file__) + " tree1 tree2")
    sys.exit(1)
  tree1 = Tree(sys.argv[1], format=1)
  tree2 = Tree(sys.argv[2], format=1)
  print("Relative RF: " + str_4(get_relative_rf(tree1, tree2)))

