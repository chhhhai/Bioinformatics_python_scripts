import sys
f = sys.argv[1]
from Bio import SeqIO
for record in SeqIO.parse(f, "fasta"):
    name = record.description.split(' ')[5][:-1]
    print(">" + name)
    print(record.seq.upper())