number=int(input())
print('input a number greater than 1')

def collatz():

        if number %2==0:
            print(number //2)
            return number //2

        if number %2==1:
            print(3* number + 1)
            return 3* number + 1

while True:
    collatz(number)

    if number == 1:
        print('answer is 1')
        break






