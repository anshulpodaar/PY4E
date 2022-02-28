fname = input("\nEnter file name: ")
if len(fname) < 1 :
    fname = 'mbox-short.txt'
fh = open(fname)

count = 0
print("\n")

for line in fh :
    line = line.rstrip()
    line = line.lstrip()
    line_lst = line.split()

    if len(line_lst) < 2 or line.startswith('From:') or not line.startswith('From') :
        continue
    print(line_lst[1])
    count = count+1

print("\nThere were", count, "lines in the file with From as the first word\n")