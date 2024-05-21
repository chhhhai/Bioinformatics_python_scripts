import sys
my_file = sys.argv[1]
f=open(my_file,'rt')
lines = f.readlines()
unique_ids = {}
output_lines = []
for line in lines:
    unique_id = line.split()[0]
    if unique_id not in unique_ids:
        output_lines.append(line)
        unique_ids[unique_id] = True
for line in output_lines:
    print(line.rstrip())
