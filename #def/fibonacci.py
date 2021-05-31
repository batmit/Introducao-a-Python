n = int((input("Número para ser calculado a sequência fibonacci: ")))
fib = [0, 1]
lele = 0
while lele <= n:
        print(fib)
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
        lele += 1
# o jeito de realizar a sequência fibonacci com função recursiva está na recursivas.py