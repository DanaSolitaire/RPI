def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1

def power(m,n):
    if n == 1:
        return m
    else:
        return multi(power(m, n-1),m)
def multi(m,n):
    if n == 1:
        return m
    else:
        return add(multi(m,n-1), m)
print(add(5,3))
print(multi(4,4))
print(power(6,70))