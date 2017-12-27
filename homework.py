# print('Input number. you will keep inputing numbers until your answer reaches 1')

# number=input(int())

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    if number % 2 == 1:
        print(3* number + 1)
        return 3* number + 1

x=int(input("input a number "))

while True:
  x = collatz(x)

  if x==1:
    break

print('your answer is ' + str(x) + ', input another number')