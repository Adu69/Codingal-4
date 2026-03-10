binary_no = int(input("Enter a binary number: "))

if binary_no == 0:
    print("Decimal equivalent: 0")
else:
    decimal_number = 0
    power = 0
    while binary_no != 0:
        digit = binary_no % 10
        decimal_number += digit * (2 ** power)
        power += 1
        binary_no //= 10
    print("Decimal equivalent: ", decimal_number)