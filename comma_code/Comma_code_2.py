#you are supposed to be able to use a comma (item,) keep all items on one line

spam = ['apples', 'bananas', 'tofu', 'cat']

#for i in spam[0:-1]:
   # print((str(i) +', ')+('and') + str(i)[-1])

for item in spam[0:-1]:
    print(str(item+ ', ' ) + ('and'))