
def fib(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >2:
        for i in range(n-1):
            c = a+b
            a = b
            b = c
        return c
            
if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
