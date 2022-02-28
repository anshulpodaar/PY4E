#   Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program.
#   Modify the program that prompts the user for the file name so that it prints a funny message when the user types in
#   the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist.

fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    if fname == 'na na boo boo':
        print('Coochie Coochie Coo!!!')
        quit()
    else :
        print('Invalid file name: ', fname)
        quit()

count = 0
for line in fh:
    count = count + 1
print('There were',count,'lines in the file, \'',fname,'\'.')
