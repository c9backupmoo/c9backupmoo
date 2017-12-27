import random

number=random.randint(1,10)

print('I am thinking of a number between 1 and 10. Take a guess.')

joke_told = True
if not joke_told:
    print("Too low again, bro")

for guessesTaken in range(1,10):
    try:
        guess = int(input())

        if (guess > number) and (guess <= 10):
            print('Too high, bro. Try again.')
            continue


        if (guess < number) and (guess < 4):
            print("I wasn't asking for your penis size, Dude. Try again.")
            continue

        if guess < number:
            print('naw, man. Try again.')
            continue

        if (guess > number) and (guess > 10):
            print('Woah, man. Slow your roll.')
            continue

        if guess==number:
            print('You got it, man!')
            break

    except ValueError:
        print('Just guess a number, douche bag.')




