def mdc(a, b):
        while a != 0 and b != 0:
            if a >= b:
                a %= b
            else:
                b %= a
        return max(a,b)

def mmc(a, b):
    return int(a*b/mdc(a,b))

print(mdc(10,15))
print(mmc(10,15))