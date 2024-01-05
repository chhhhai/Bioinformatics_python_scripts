import sys
f = sys.argv[1]
from Bio import SeqIO
for record in SeqIO.parse(f, "fasta"):
    if record.seq[0:3]=="ATG":
        print(">" + record.description)
        print(record.seq.upper())