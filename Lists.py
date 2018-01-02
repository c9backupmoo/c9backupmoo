print('Would you like to make a list?')

r =input().lower()
yesList=['y','yes']
noList=['n','no']

for r in yesList:
    print('What would you like to call your list?')
name=input()
newList=name
print('Input your list items for ' + newList.upper())

for r in noList:
    print('Would you like to add to an existing list?')

    #if r in yesList:

        #print('What list would you like to alter?')



