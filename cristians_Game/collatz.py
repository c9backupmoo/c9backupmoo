def collatz(number):
    if number % 2 == 1:
        print(number // 2)
        return number // 2

x = collatz(7)
print("hi moo, collatz returned: " + str(x))