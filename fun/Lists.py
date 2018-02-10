#for the first input - if other than yes or no, search database for input
#if input is not found - restate th question, maybe specify 'yes' or 'no'
#program will end if a space is used while inputting list items - fix this
#user should also be able to use the enter key during this process without ending the program
        #maybe use a different key (other than enter) to indicate the end of a list
#create a way for the user to also assign a quantity to the list item {apples:5, sprouts: 1 pound}
#search for a list based on a word in that list, (ex: "apples" - 'there are 2 lists that contain apples'
            #'groceries' and 'recipes' - 'please type the name of the list you would like to access'
                    #if no such word is found - ask if they would like to make a new list for 'apples'
                            #this will require a try except
#create a way for the user to go back


def start():

    #try:
        print('Would you like to make a list? Yes or no.')

        r =input().lower()
        yesList=['y','yes']
        noList=['n','no']
        masterList=[]
#NAMING LIST
        if r in yesList:
            print('What would you like to call your list?')
            #create a 'master list' where all lists are stored and can be called
            name=input()
            print('Input your list items for ' + name.upper())
            newList=[]
            masterList.append(name)
            masterList.append(newList)
            add=input()
#ADDING TO THE LIST
            newList.append(add)
            print('Your list items for ' + name.upper() +':')
            for item in newList:
                print(item)
#SAVING A LIST
            print('Would you like to save ' + name.upper() + '?')
            option = input()
            if option in yesList:
                print('Your list, ' + name.upper() + ', has been saved.')
                start()
#NOT SAVING LIST
            #not working
            if option in noList:
                print('Would you like to continue editing ' + name.upper() + '?')



#CALLING EXISTING LIST
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

    #except NameError:
        #start()


start()

#PROBLEM !!! TRY EXCEPT NOT WORKING - CAN'T FIGURE OUT WHY