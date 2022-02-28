def small_num(small,x):
    if small is None:
        small = x
    elif x < small:
        small = x
    return small

def big_num(big,x):
    if big is None:
        big = x
    elif x > big:
        big = x
    return big


b = None
s = None

while True:
    num = input('Enter a number :')
    if num == 'done':
        break
    try:
        num=int(num)
    except:
        print('Invalid input')
        continue

    s = small_num(s,num)
    b = big_num(b,num)    

print('\nMaximum is',b)
print('Minimum is',s)