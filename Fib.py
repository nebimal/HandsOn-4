def Fib(n):
    print("Fib(",n,")")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fib(n-1) + Fib(n-2)

print("Fib(5) =",Fib(5))