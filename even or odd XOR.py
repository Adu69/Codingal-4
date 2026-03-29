def isEvenOdd(n):
    if(n ^ 1 == n + 1):
        return True;
    else:
        return False;

number = int(input("Enter a number: "))

if isEvenOdd(number):
    print("The number", number, "is even.")
else:
    print("The number", number, "is odd.")