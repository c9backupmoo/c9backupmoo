print('input a number greater than 1')

def collatz(number):

        if number %2==0:
            print(number //2)
            return number //2

        if number %2==1:
            print(3* number + 1)
            return 3* number + 1

x=int(input())


while True:
    try:
        collatz(x)

        x=collatz(x)

        if x == 1:
            print('answer is ' + str(x))
            break

    except ValueError:
        print('please type a number')

#can't except without breaking program



