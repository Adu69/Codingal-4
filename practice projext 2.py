def one_iteration(a, b):
    return a * b

def n_iteration(a, b):
    s = 0
    for _ in range(b):
        s += a
    return s

a = int(input("Enter 'a' for a*b : "))
b = int(input("Enter 'b' for a*b : "))

print("\n1 iteration:", one_iteration(a, b))
print("N iteration:", n_iteration(a, b))
