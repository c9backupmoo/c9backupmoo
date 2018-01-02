print('Would you like to make a list?')

r =input().lower()
yesList=['y','yes']
noList=['n','no']

if r in yesList:
    print('What would you like to call your list?')
if r in noList:
    print('Would you like to add to an existing list?')
name=input()
newList=name
print('Input your list items for ' + newList.upper())

