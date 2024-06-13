n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = [0, 1]
for i in range(2, n):
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
print(f"First {n} Fibonacci numbers:", fib_sequence[:n])
