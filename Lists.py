def start():
    print('Would you like to make a list?')

    r =input().lower()
    yesList=['y','yes']
    noList=['n','no']
    masterList=[]

    if r in yesList:
        print('What would you like to call your list?')
        #create a 'master list' where all lists are stored and can be called
        name=input()
        print('Input your list items for ' + name.upper())
        newList=[]
        masterList.append(name)
        masterList.append(newList)
        add=input()
        newList.append(add) # is not adding to the list
        for item in newList:
            print(item)

    if r in noList:
        print('Would you like to add to an existing list?')
        answer=input()
        if answer in noList:
            print('You are out of options.')
            print('Would you like to start from the beginning?')

            option=input()
            if option in noList:

                print('Goodbye')
                exit()
            if option in yesList:
                start()
        if answer in yesList:
            print('What list would you like to alter?')
            listName=input()


start()

