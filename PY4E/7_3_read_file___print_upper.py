# Write a program to read through a file and print the contents of the file (line by line) all in upper case.

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Please enter valid file name.")
    quit()

print("\n")
for line in fh:
    print(line.strip().upper())
print("\n\n")
