spam=['apples', 'bananas', 'tofu', 'cats']

for item in spam[0:-1]:
    print(item + ', ', end='') #turns items from list into string and adds a comma


print('and ' + spam[-1]) #prints s(fisrt 3 items in list + comma) + and and the last item