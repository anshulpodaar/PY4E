# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers 
# at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use 
# the max() and min() functions to compute the maximum and minimum numbers after the loop completes.


#   Recieving list as input
t = list()
print('\nPlease enter list:\n(Type \'done\' to end at any time)')
while True:
    num_str = input()
    try:
        num_int = int(num_str)
    except:
        if num_str == 'done':
            break
        print('Invalid input')
        quit()
    t.append(num_int)
print('\nOriginal list: ', t)

print('Maximum value: ', max(t))
print('Minimum value: ', min(t), '\n')