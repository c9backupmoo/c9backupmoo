{"filter":false,"title":"guessing_game2.py","tooltip":"/guessing_game2.py","undoManager":{"mark":73,"position":73,"stack":[[{"start":{"row":0,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["import random","","number=random.randint(1,10)","","print('I am thinking of a number between 1 and 10. Take a guess.')","","","for guessesTaken in range(1,10):","","","        try:","            guess = int(input())","        ","            if (guess > number) and (guess <= 10):","                print('Too high, bro. Try again.')","                continue","        ","","            if (guess < number) and (guess < 4):","                print(\"I wasn't asking for your penis size, Dude. Try again.\")","                continue","","            if guess < number:","                print('naw, man. Try again.')","                continue","","            if (guess > number) and (guess > 10):","                print('Woah, man. Slow your roll.')","                continue","","        except ValueError:","            print('Just guess a number, douche bag.')","        ","","    if guess==number:","        print('You got it, man!')","        break","",""],"id":75}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":76},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"remove","lines":["    "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":77},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":8},"action":"remove","lines":["        "]}],[{"start":{"row":34,"column":3},"end":{"row":36,"column":13},"action":"remove","lines":[" if guess==number:","        print('You got it, man!')","        break"],"id":78}],[{"start":{"row":28,"column":20},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":79},{"start":{"row":29,"column":0},"end":{"row":29,"column":12},"action":"insert","lines":["            "]},{"start":{"row":29,"column":8},"end":{"row":29,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":29,"column":8},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":80},{"start":{"row":30,"column":0},"end":{"row":30,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":30,"column":8},"end":{"row":32,"column":13},"action":"insert","lines":[" if guess==number:","        print('You got it, man!')","        break"],"id":81}],[{"start":{"row":31,"column":8},"end":{"row":31,"column":12},"action":"insert","lines":["    "],"id":82}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":12},"action":"insert","lines":["    "],"id":83}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"remove","lines":["        "],"id":84},{"start":{"row":38,"column":0},"end":{"row":38,"column":3},"action":"remove","lines":["   "]}],[{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"remove","lines":[" "],"id":85}],[{"start":{"row":4,"column":66},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":86,"ignore":true},{"start":{"row":6,"column":32},"end":{"row":8,"column":0},"action":"remove","lines":["","",""]}],[{"start":{"row":5,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["","j",""],"id":87,"ignore":true}],[{"start":{"row":6,"column":1},"end":{"row":6,"column":4},"action":"insert","lines":["oke"],"id":88,"ignore":true}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":7},"action":"insert","lines":["_to"],"id":89,"ignore":true}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":10},"action":"insert","lines":["ld "],"id":90,"ignore":true}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":13},"action":"insert","lines":["= f"],"id":91,"ignore":true}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":17},"action":"insert","lines":["alse"],"id":92,"ignore":true}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":17},"action":"remove","lines":["alse"],"id":93,"ignore":true}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["f"],"id":94,"ignore":true},{"start":{"row":6,"column":12},"end":{"row":6,"column":14},"action":"insert","lines":["Fa"]}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":17},"action":"insert","lines":["lse"],"id":95,"ignore":true}],[{"start":{"row":6,"column":17},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":96,"ignore":true}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["i"],"id":97,"ignore":true}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":3},"action":"insert","lines":["f "],"id":98,"ignore":true}],[{"start":{"row":7,"column":3},"end":{"row":7,"column":6},"action":"insert","lines":["no "],"id":99,"ignore":true}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"remove","lines":[" "],"id":100,"ignore":true},{"start":{"row":7,"column":5},"end":{"row":7,"column":7},"action":"insert","lines":["y "]}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":7},"action":"remove","lines":["y "],"id":101,"ignore":true},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":9},"action":"insert","lines":[" jo"],"id":102,"ignore":true}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":11},"action":"insert","lines":["ke"],"id":103,"ignore":true}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":15},"action":"insert","lines":["_tol"],"id":104,"ignore":true}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":17},"action":"insert","lines":["d:"],"id":105,"ignore":true}],[{"start":{"row":7,"column":17},"end":{"row":8,"column":5},"action":"insert","lines":["","    p"],"id":106,"ignore":true}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":9},"action":"insert","lines":["rint"],"id":107,"ignore":true}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":11},"action":"insert","lines":["()"],"id":108,"ignore":true}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":12},"action":"insert","lines":["\"\""],"id":109,"ignore":true}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["H"],"id":110,"ignore":true}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":15},"action":"insert","lines":["e'r"],"id":111,"ignore":true}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":15},"action":"remove","lines":["'r"],"id":112,"ignore":true}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":17},"action":"insert","lines":["re's"],"id":113,"ignore":true}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":19},"action":"insert","lines":[" a"],"id":114,"ignore":true}],[{"start":{"row":8,"column":19},"end":{"row":8,"column":22},"action":"insert","lines":[" jo"],"id":115,"ignore":true}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":24},"action":"insert","lines":["ke"],"id":116,"ignore":true}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":24},"action":"remove","lines":["Here's a joke"],"id":117},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["T"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["o"],"id":118}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["o"],"id":119}],[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":[" "],"id":120}],[{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["l"],"id":121}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["o"],"id":122}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["w"],"id":123}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":[" "],"id":124}],[{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["a"],"id":125}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["g"],"id":126}],[{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["a"],"id":127}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["i"],"id":128}],[{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["n"],"id":129}],[{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":[","],"id":130}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":[" "],"id":131}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["b"],"id":132}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["r"],"id":133}],[{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["o"],"id":134}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":17},"action":"remove","lines":["False"],"id":135,"ignore":true},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["T"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["r"],"id":136,"ignore":true}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":16},"action":"insert","lines":["ue"],"id":137,"ignore":true}],[{"start":{"row":20,"column":74},"end":{"row":21,"column":12},"action":"insert","lines":["","            "],"id":138,"ignore":true}],[{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["j"],"id":139,"ignore":true}],[{"start":{"row":21,"column":13},"end":{"row":21,"column":16},"action":"insert","lines":["oke"],"id":140,"ignore":true}],[{"start":{"row":21,"column":16},"end":{"row":21,"column":20},"action":"insert","lines":["_tol"],"id":141,"ignore":true}],[{"start":{"row":21,"column":20},"end":{"row":21,"column":23},"action":"insert","lines":["d ="],"id":142,"ignore":true}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":25},"action":"insert","lines":[" f"],"id":143,"ignore":true}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":["f"],"id":144,"ignore":true},{"start":{"row":21,"column":24},"end":{"row":21,"column":26},"action":"insert","lines":["Fa"]}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":29},"action":"insert","lines":["lse"],"id":145,"ignore":true}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":16},"action":"remove","lines":["True"],"id":146,"ignore":true},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["F"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":17},"action":"insert","lines":["alse"],"id":147,"ignore":true}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":16},"action":"remove","lines":["Fals"],"id":148},{"start":{"row":6,"column":12},"end":{"row":6,"column":15},"action":"insert","lines":["Tru"]},{"start":{"row":20,"column":74},"end":{"row":21,"column":29},"action":"remove","lines":["","            joke_told = False"]}]]},"ace":{"folds":[],"scrolltop":69,"scrollleft":0,"selection":{"start":{"row":18,"column":0},"end":{"row":18,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1514408052712,"hash":"6d2db16541c32d64d77a4803ad12862561d75359"}