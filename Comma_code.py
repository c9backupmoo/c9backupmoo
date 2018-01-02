spam=['apples', 'bananas', 'tofu', 'cats']
#print(', '.join(spam)[0:-1])


print(', '.join(spam[0:-1]) + ' and ' + spam[-1] )

s = ""
for item in spam[0:-1]:
    s = s + item

print(s)