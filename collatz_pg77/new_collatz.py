number=input()

print('input a number higher than 1')

def collatz():


    if number %2 == 0:
        x = number //2
        print (x)
        return x

    if number %2==1:
        y = 3* number +1
        print (y)
        return y


while number!= 1:
    collatz()

    if number()==1:
        print('Done!')