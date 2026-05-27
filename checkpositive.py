sum = 0
while True:

    num = int(input("Enter a number: "))
    if num < 0:
        break
    sum = sum + num
print("Sum of positive numbers is:", sum)
