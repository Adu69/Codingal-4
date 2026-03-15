largestnum = int(input("Enter the Larger number: "))
smallestnum = int(input("Enter the Smaller number: "))

a = smallestnum
b = largestnum
while smallestnum > 0:
    store = smallestnum
    smallestnum = largestnum % smallestnum
    largestnum = store
    print("The GCD is: ", largestnum)

GCD = largestnum
LCM = (a*b) // GCD
print("The LCM is: ", LCM)