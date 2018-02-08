import random

number=random.randint(1,10)

print('I am thinking of a number between 1 and 10. Take a guess.')


while True:

    guess = int(input())


    if guess > number:
        print('Too high, bro. Try again.')
        continue


    elif (guess < number) and (guess < 4):
        print("I wasn't asking for your penis size, Dude. Try again.")
        continue

    elif guess < number:
        print('naw, man. Try again.')
        continue


    elif guess==number:
        print('You got it, man!')
        break
