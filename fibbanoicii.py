def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
print("Fibonacci sequence:", fibonacci(num_terms))