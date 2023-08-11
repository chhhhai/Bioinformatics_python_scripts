import sys
print("getsnpanno bed_file gff3_file out_file")
bedfile_in = sys.argv[1]
gfffile_in = sys.argv[2]
outfile_in = sys.argv[3]

gfffile = open(gfffile_in, 'r')
outfile = open(outfile_in, 'w')
gff = gfffile.readlines()
for line in gff:
    line_std = line.split("\t")
    if line_std[2] == 'mRNA':
        bedfile = open(bedfile_in, "r")
        bed = bedfile.readlines()
        bedfile.close()
        for i in bed:
            a = i.split()
            if a[1] == line_std[0] and int(a[2]) >= int(line_std[3]) and int(a[3]) <= int(line_std[4]):
                gene = f"{a[0]}\t{line_std[8]}"
                outfile.write(gene)
    else:
        pass
outfile.close()