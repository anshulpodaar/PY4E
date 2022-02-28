# Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

#   Defining the functions
def chop(t):
    x = len(t)-1
    del t[x]
    del t[0]
    return None

def middle(t):
    x = len(t)-1
    t2 = t[1:x]
    return t2

#   Recieving list as input
t = list()
print('Please enter list:\n(Press # to end at any time)\n')
while True:
    num_str = input()
    try:
        num_int = int(num_str)
    except:
        if num_str == '#':
            break
        print('Invalid input')
        quit()
    t.append(num_int)
print('\nOriginal list: ', t)

#   Invoking the functions created
t_duplicate = t[:]
chop(t_duplicate)
print('Chop function on list: ', t_duplicate)
t_duplicate = t[:]
print('Middle function on list: ', middle(t_duplicate), '\n')
