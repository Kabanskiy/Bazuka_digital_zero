import random

def is_prime(a):
    if a == 0:
        return False
    print(a)
    for i in range(10):
        if a != 0:
            return sum(a+a[1:])
    else:
        return True
print(is_prime(random.randint(0,100)))