n=int(input("Enter number of terms: "))
a=0
b=1
temp=0
i=1
print()
print(a)

while i < n :
    print(b)
    temp=a+b
    a=b
    b=temp
    i = i+1
print("\nEnd of Sequence\n\n")