import random

number=random.randint(1,10)
print('I am thinking of a number between 1 and 10. Take a guess.')

joke_told=False

for guessesTaken in range(1,10):
    try:
        guess = int(input())

        if (guess > number) and (guess <= 10):
            print('Too high, bro. Try again.')
            continue

        if (guess < number) and (guess < 4):
            if joke_told == False:
                print("I wasn't asking for your penis size.")
                joke_told = True
            else:
                print("Still too low, bro. Guess again.")
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




