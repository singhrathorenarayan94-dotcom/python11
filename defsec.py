def odd_even(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


def divisible_by_3(num):
    if num % 3 == 0:
        print("Divisible by 3")
    else:
        print("Not divisible by 3")


number = int(input("Enter a number: "))

odd_even(number)
divisible_by_3(number)
