def setOrnot(number, n):
    if number & (1 << (n-1)):
        print("Bit is set")
    else:
        print("Bit is not set")

number = int(input("Enter a number: "))
n = int(input("Enter the bit position to check (1-based index): "))
setOrnot(number, n)