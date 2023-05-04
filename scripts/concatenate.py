#!/usr/bin/env python3
import os
import sys
import ete3
import random

"""
  Read an MSA file and return a ete3.SeqGroup object
"""
def read_msa(msa):
  return ete3.SeqGroup(msa)


"""
  Read a mapping file with the phyldog format
  and return a dictionary: d[species] = list of genes
"""
def read_mappings(mapping_file):
  d = {}
  for line in open(mapping_file).readlines():
    sp = line.replace("\n", "").split(":")
    d[sp[0]] = sp[1].split(";")
  return d

"""
  Identify mapping: d[label]=[label] for all labels of the msa
"""
def get_mapping_from_msa(msa):
  d = {}
  for entry in msa.get_entries():
    d[entry[0]] = [entry[0]]
  return d

def concatenate(msa_dir, subst_model, prefix, mapping_dir, mode):
  partition_path = prefix + ".part"
  supermatrix_path = prefix + ".fasta"

  partition_writer = open(partition_path, "w")
  offset = 0
  single = (mode == "single")
  use_all_genes = (mode == "max")
  
  family_to_mapping = {}
  supermatrix = {}
  part_number = 0
  use_mappings = mapping_dir.lower() != "none"
  if (use_mappings):
    # Fill family_to_mapping
    if (not os.path.isdir(mapping_dir)):
      print("Error, mapping dir is not a directory: " + mapping_dir)
      sys.exit(1)
    for f in os.listdir(mapping_dir):
      family = f.split(".")[0]
      d = read_mappings(os.path.join(mapping_dir, f))
      family_to_mapping[family] = d

  for f in os.listdir(msa_dir):
    family = f.split(".")[0]
    print("Concatenating msa " + os.path.join(msa_dir, f))
    gene_msa = read_msa(os.path.join(msa_dir, f))
    seq_len = len(gene_msa.get_entries()[0][1])
    species_to_genes = {}
    if (use_mappings):
      species_to_genes = family_to_mapping[family]
    else:
      species_to_genes = get_mapping_from_msa(gene_msa)
    # check if we have a new species
    for species in species_to_genes:
      if (not species in supermatrix):
        supermatrix[species] = "-" * offset
      # randomize the order of genes from the same species
      random.shuffle(species_to_genes[species])

    gene_gaps = "-" * seq_len
    
    while (len(species_to_genes) > 3):
      # we will repeat this step if we are in max mode
      for species in supermatrix:
        seq = gene_gaps
        if (species in species_to_genes):
          seq = gene_msa.get_seq(species_to_genes[species][-1])
          species_to_genes[species].pop()
          if (len(species_to_genes[species]) == 0):
            del species_to_genes[species]
        supermatrix[species] += seq
      partition_writer.write(subst_model + ", " + family + " = ")
      partition_writer.write(str(offset + 1) + "-" + str(offset + seq_len))
      partition_writer.write("\n")
      part_number += 1
      offset += seq_len
      if (not mode == "max"):
        break
  partition_writer.close()
  supermsa = ete3.SeqGroup()
  for species in supermatrix:
    supermsa.set_seq(species, supermatrix[species])
  supermsa.write("fasta", supermatrix_path)
  print("Total number of sites: " + str(offset))
  print("Total number of partitions: " + str(part_number))
  print ("Output supermatrix: " + supermatrix_path)
  print ("Output partitions: " + partition_path)
  return offset
      


if __name__ == "__main__":
  if (len(sys.argv) != 6):
    print("Syntax: ./concatenate.py msa_dir subst_model prefix mapping_dir concatenation_mode")
    sys.exit(1)
  msa_dir = sys.argv[1]
  subst_model = sys.argv[2]
  prefix = sys.argv[3]
  mapping_dir = sys.argv[4]
  mode = sys.argv[5]
  if (mode != "min" and mode != "max"):
    print("Error: concatenation_mode should be either min or max")
    sys.exit(1)
  concatenate(msa_dir, subst_model, prefix, mapping_dir, mode)

