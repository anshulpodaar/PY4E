def computepay(h,r):
    x = (h - 40) * (r * 1.5)
    return x


try:
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate: "))
except:
    print("Error! Please enter numeric input.")
    quit()
pay = 0
if hours <= 40 :
    pay = hours * rate
else:
    pay = (40 * rate) + computepay(hours,rate)
print(pay)