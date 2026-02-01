def OnTime(n):
    iteration = 0
    for i in range(n, n+1):
        iteration += 1
    print("When n =", n, "the loop ran", iteration, "time(s).")

print(OnTime(10))
print(OnTime(100))
print(OnTime(1000))

print("\n With any value of n, the loop runs exactly once, demonstrating O(1) time complexity.")