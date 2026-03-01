number = int(input("Enter a number: "))

digits = len(str(number))

resultnumber = 0

temp = number
while temp > 0:
    digit = temp % 10
    resultnumber += digit ** digits
    temp //= 10

if number == resultnumber:
    print(f"{number} is an Armstrong number.")
else:    
    print(f"{number} is not an Armstrong number.")