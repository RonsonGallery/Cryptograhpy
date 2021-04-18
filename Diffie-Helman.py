import random

alpha = 2


def miller_rabin(n, k):

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break

        else:
            return False
    return True


def genprimeBits(n):
    x = ""
    n = int(n)
    for y in range(n):
        x = x + "1"
    y = "1"
    for z in range(n - 1):
        y = y + "0"
    x = int(x, 2)
    y = int(y, 2)
    p = 0
    while True:
        p = random.randrange(y, x)
        if miller_rabin(p, 40):
            break
    return p


def generateKey(p, alpha):
    x = random.randrange(1, p - 1)
    public_key = alpha ** x % p
    values = (x, public_key)

    return values


p = genprimeBits(10)
Alice = generateKey(p, alpha)
Bob = generateKey(p, alpha)

# print(Alice[])

Alice2 = Bob[1] ** Alice[0] % p
Bob2 = Alice[1] ** Bob[0] % p

print(Alice2)
print(Bob2)














#Credit to https://www.codegrepper.com/code-examples/python/how+to+generate+prime+numbers+in+a+bit+range+python for miller rabin and Genprimebits