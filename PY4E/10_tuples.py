fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'romeo.txt'
try:
    fh = open(fname)
except:
    print("Enter valid file name.")
    quit()

counts = dict()
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

option = int(input('Select Option (1, 2, 3 or 4): '))

if option == 1:
    lst = list()
    for key, val in counts.items():
        newtup = (val, key)
        lst.append(newtup)

    lst = sorted(lst, reverse = True)
    for val,key in lst[:10]:
        print(key, val)

elif option == 2:
    print( sorted( [ (v,k) for k,v in counts.items() ] ) )

elif option == 3:
    print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )

elif option == 4:
    print( (sorted( [ (v,k) for k,v in counts.items() ], reverse=True ))[:10] )

else:
    print('Please input correct option')

