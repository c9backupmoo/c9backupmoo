#change to include proper cases for punctuation.
#assess the string inputs ie. the number of characters, the use of 'and'. then adjust the responses accordingly

print('Did you eat lunch today?')

response=input().lower()

yesList=['y','yes', 'yeah' , 'ya', 'yup', 'yes i did']
noList=['n', 'no', 'naw', 'nah', 'nope', "no i didn't", 'no i did not']


if response in yesList:
    print('What did you eat for lunch?')
if response in noList:
    print('What would you like to eat?')

foods=input()
suffix='s'
if foods.endswith(suffix):
    x='many'
else:
    x='much'

if response in yesList:

    print(foods + "."' that sounds good. How ' + x+ ' ' + foods + ' did you have?')

#adjust code to detect plurals and change string accordingly

if response in noList:
    print(foods.capitalize() + "."' that sounds good. How '+ x + ' ' + foods + ' will you have?')
#convert to upper case at the beginning of the string and after the periods

try:
    response=input()
    number=int(response)


    if number < 5:
        print('Are you on a diet?')

    if (number >= 5) and (number <= 19):
        print('Slow down piggy, leave some for the rest of us')

    if number > 20:
        print(str(number) + '! Are you training for an eating contest?')

except ValueError:
    print(response + '. Good job!')

# add contingencies for string responses