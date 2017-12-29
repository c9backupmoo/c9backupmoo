print('Did you eat lunch today?')

response=input()

yesList=['y','yes', 'yeah' , 'ya', 'yup', 'yes i did']
noList=['n', 'no', 'naw', 'nah', 'nope', "no i didn't", 'no i did not']


if response in yesList: #change to accept multiple versions of response
    print('What did you eat for lunch?')
if response in noList:
    print('What you you like to eat?')

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
    print(foods + "."' that sounds good. How '+ x + ' ' + foods + ' will you have?')
#convert to upper case at the beginning of the string and after the periods

response=int(input()) or str(input())

if response > 5:
    print('Slow down piggy, leave some for the rest of us')

if response==int(input()):
    print(response + "That's the way to do it.")

# add comments based on int(input)