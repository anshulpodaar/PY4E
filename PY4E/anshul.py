# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#   From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fn = input("Enter file name: ")
try:
    fh = open(fn)
except:
    print("Invalid file name")
    quit()

words = dict()
l = list()

for line in fh:
    x = line.split()
    for w in x:
        words[w] = words.get(w,0) + 1

for k,v in words.items():
    l.append((v,k))

#l.sort(reverse=True)
for v,k in l[:]:
    print(v,k)