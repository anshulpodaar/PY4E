try:
    x = int(input('Please enter a whole number: ' ))
except:
    print('Invalid entry.')

fact = 1
num = x
while x>1:
    fact = fact*x
    x=x-1
print('Factorial of ', num, ' = ', fact)
