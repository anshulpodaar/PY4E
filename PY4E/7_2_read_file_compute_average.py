# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#   X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values 
#   and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
#   when you are testing below enter mbox-short.txt as the file name.

fn = input("Enter file name: ")
try:
    fh = open(fn)
except:
    print("Enter valid file name.")
    quit()

count = 0.0
tot = 0.0

for lx in fh:
    if not 'X-DSPAM-Confidence:' in lx:
        continue
    count = count + 1
    pos = lx.find(':')
    ls = lx[pos+1 : ]
    lf = float(ls.strip())
    tot = tot + lf

print("Average spam confidence:",(tot/count))