def fibo(n):
    if n > 0:
        if n <= 1:
            return 1
        else:
            return fibo(n-1) + fibo(n-2)
    else:
        return 0


fibbonacci = [fibo(fib) for fib in range(1, 31)]
print(fibbonacci)

fibbonacci = []
fibbonacci.append(1)
fibbonacci.append(1)
for i in range(2, 30):
    fibbonacci.append(fibbonacci[i-1] + fibbonacci[i-2])
print(fibbonacci)