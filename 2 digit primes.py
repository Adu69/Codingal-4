# Find all 2-digit prime numbers

for num in range(10, 100):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num)