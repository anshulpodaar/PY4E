# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#   From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fh = open(fname)
except:
    print("Enter valid file name.")
    quit()

hour = dict()
tup = tuple()

for line in fh:
    if not line.startswith('From '):
        continue
    lx = line.split()
    if not len(lx) >= 6 :
        continue
    ls = lx[5].split(':')
    hour[ls[0]] = hour.get(ls[0],0) + 1

tup = sorted([k,v] for k,v in hour.items())

for k,v in tup:
    print(k,v)

print()

for k,v in sorted(hour.items()):
    print(k,v)