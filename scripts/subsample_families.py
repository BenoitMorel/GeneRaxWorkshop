#!/usr/bin/env python3
import os
import sys
import shutil
import random

def subsample(datadir, outputdir, ratio, seed):
  if (not os.path.isdir(datadir)):
    print("Error, input directory " + datadir + " does not exist")
    sys.exit(1)
  os.mkdir(outputdir)
  input_ali_dir = os.path.join(datadir, "alignments")
  input_map_dir = os.path.join(datadir, "mappings")
  output_ali_dir = os.path.join(outputdir, "alignments")
  output_map_dir = os.path.join(outputdir, "mappings")
  os.mkdir(output_ali_dir)
  os.mkdir(output_map_dir)
  families = []
  for f in os.listdir(input_ali_dir):
    families.append(f.split(".")[0])
  random.shuffle(families)
  
  to_keep_number = int(float(len(families)) * ratio)
  to_keep = set(families[0:to_keep_number])
  print("Keeping " + str(to_keep_number) + " families")

  for family in to_keep:
    ali = family + ".fasta"
    mapping = family + ".map"
    src = os.path.join(input_ali_dir, ali)
    dest = os.path.join(output_ali_dir, ali)
    shutil.copy(src, dest)
    src = os.path.join(input_map_dir, mapping)
    dest = os.path.join(output_map_dir, mapping)
    shutil.copy(src, dest)

  

if __name__ == "__main__":
  if (len(sys.argv) != 5):
    print("Syntax: ./subsample_families inputdatadir outputdatadir ratio seed")
    sys.exit(1)
  datadir = sys.argv[1]
  outputdir = sys.argv[2]
  ratio = float(sys.argv[3])
  seed = int(sys.argv[4])
  if (ratio <= 0.0 or ratio > 1.0):
    print("The ratio should be between 0 and 1")
    sys.exit(1)
  random.seed(seed)
  subsample(datadir, outputdir, ratio, seed)

