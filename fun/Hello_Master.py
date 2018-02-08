print('Hello')
print('What is your name?')

name=input()
nameList=['jack','ada lovelace']
while name in nameList:

    if name.lower()=='jack':
        print('ALL WORK AND NOT PLAY MAKES JACK A DULL BOY')#randomize cases
    elif name.lower()=='ada lovelace':
        print('Thank you, Ada, for your contributions.' +
              'You can use my computer anytime.')
        exit()

if name.lower()=='cristian': #change to include surname
    print('Hello, Sexy')

elif name.lower()=='ambernay':
    print('Hello, Master')

else:
    print('Who are you and why are you using my computer?')


age=int(input('State your age'))


if age <= 12:
    print('Get your tiny jam hands off of my keyboard')
if age > 12:
    print ('State your occupation')

if age >100:#tried to use len, didn't work
    print('Are you a vampire?')

if age==str:
    print("I don't need your life story. Just give me your age")


occ=input()

if occ=='student':
    print('school is for nerds')
elif occ=='photographer':
    print('Why would you want to do a silly thing like that?')
elif occ=='programmer' or occ=='software developer':
    print('You have chosen well for yourself')
    print('What are your doing after this? ;)')
else:
    print("That's a job now?")
