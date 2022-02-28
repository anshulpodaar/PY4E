# Input file name and create file handle
try:
    fname = input("\nEnter file name: ")
    fh = open(fname)
except:
    print("Invalid file name:",fname)
    quit()

count = 0
add = 0

# Read the data in the file
for lx in fh:
    ly = lx.rstrip() #Removing new line character from end of every line
    print(ly)
    count = count + 1
print("\nNumber of lines in file:",count)

# Reopen file handle (it acts as pointer/count)
fh = open(fname)

count = 0

# Search for data required, extract data required, convert to float from string, add and then average it
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    sp = line.find(":")
    str_d = line[sp+1:]
    flt_d = float(str_d)
    add = add + flt_d

# Print the values as required
print("\nCount:",count,"\t\tSum:",add)
fname_avg = add/count
print("\nAverage spam confidence:",fname_avg,"\n\n")

