# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Enter valid file name")
    quit()

sender = dict()

for line in fh:
    if not line.startswith('From '):
        continue
    words = line.split()
    sender[words[1]] = sender.get(words[1],0) + 1

maxkey = None
maxval = None
for key,val in sender.items():
    if maxval == None or val > maxval :
        maxkey = key
        maxval = val

print(maxkey, maxval)