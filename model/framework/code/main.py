# imports
import os
import csv
import sys
from rdkit import Chem
from rdkit.Chem.Descriptors import MolWt

from phakinpro import write_csv_file

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))


# my model
def my_model(smiles_list):
    return [MolWt(Chem.MolFromSmiles(smi)) for smi in smiles_list]


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]
#print(smiles_list)
# run model
outputs = write_csv_file(smiles_list, calculate_ad=False)
print(outputs)
#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs) - 1
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])  # header
    for o in outputs:
        writer.writerow([o])