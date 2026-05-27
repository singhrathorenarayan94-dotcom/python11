def num(a):
    for i in range(2,a):
        if a%i==0:
            return True
    return False
print(num(3))
