def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1 

    for p in range(2, num):
        if prime[p]:
            print(p)

num = int(input("Enter the number: "))
print("Prime numbers less than or equal to", num, "are:")
SieveOfEratosthenes(num)