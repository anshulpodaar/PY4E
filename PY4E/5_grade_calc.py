try:
    score = float(input("\nPlease enter score (between 0.0 and 1.0: "))
except:
    print("\nError! Please enter valid numeric score between 0.0 and 1.0\n")
    quit()
if score > 1:
    print("\nCan't you read? \nEnter a goddamn correct score!!!!\n")
elif score >= 0.9:
    print("A")
elif score >=0.8:
    print("B")
elif score >=0.7:
    print("C")
elif score >=0.6:
    print("D")
else:
    print("F")
