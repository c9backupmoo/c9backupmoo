# Given a string, returns that string with strikethrough
def strike(text):
    # https://stackoverflow.com/questions/19457227/how-to-print-like-printf-in-python3
    result = ''
    for c in text:
        result = result + '\u0336' + c
    return result



def main():
    print("hello {0} moo".format(strike("world")))

    fortunes = [
        "You will get very hangry",
        "A man in pink underwear will wrap himself in your blankets",
        "(This fortune intentionally left blank)",
        "I ran out of fortunes",
        "I ran out of fortunes",
        "I ran out of fortunes",
        "I ran out of fortunes",
        "I ran out of fortunes",
        "I ran out of fortunes",
    ]

    while True:
        response = input("Pick a fortune (1-9) or exit: ")
        if 'exit' in response.lower():
            print("Exiting")
            break;

        try:
            number = int(response)
            if 9 >= number >= 1:
                print(fortunes[number-1])
            else:
                print(f"{response} is not between 1 and 9")
        except ValueError:
            print(f"{response} is not a number")
