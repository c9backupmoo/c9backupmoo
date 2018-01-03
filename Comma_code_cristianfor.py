spam=['apples', 'bananas', 'tofu', 'cats']

#s = "" #assigns s as a string?

for item in spam[0:-1]:
    s = s + item + ', ' #turns items from list into string and adds a comma

print(s + 'and ' + spam[-1]) #prints s(fisrt 3 items in list + comma) + and and the last item
