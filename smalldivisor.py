def smalldivisor(a):
    if a == 0 :
        return 0
    for i in range(2,a+1):
        if a%i==0:
            return i
print(smalldivisor(35))
