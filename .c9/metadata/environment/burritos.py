{"changed":true,"filter":false,"title":"burritos.py","tooltip":"/burritos.py","value":"print('Did you eat lunch today?')\n\nresponse=input()\n\nyesList=['y','yes', 'yeah' , 'ya', 'yup', 'yes i did']\nnoList=['n', 'no', 'naw', 'nah', 'nope', \"no i didn't\", 'no i did not']\n\n\nif response in yesList: #change to accept multiple versions of response\n    print('What did you eat for lunch?')\nif response in noList:\n    print('What you you like to eat?')\n\nfoods=input()\nsuffix='s'\nif foods.endswith(suffix):\n    x='many'\nelse:\n    x='much'\n\nif response in yesList:\n\n    print(foods + \".\"' that sounds good. How ' + x+ ' ' + foods + ' did you have?')\n\n#adjust code to detect plurals and change string accordingly\n\nif response in noList:\n    print(foods + \".\"' that sounds good. How '+ x + ' ' + foods + ' will you have?')\n#convert to upper case at the beginning of the string and after the periods\ntry:\n    number=int(input())\n    \n    if response > 5:\n        print('Slow down piggy, leave some for the rest of us')\n        \nexcept:ValueError\nprint(response + \"That's the way to do it.\")\n\n# add comments based on int(input)","undoManager":{"mark":54,"position":100,"stack":[[{"start":{"row":30,"column":33},"end":{"row":30,"column":35},"action":"insert","lines":["()"],"id":1623}],[{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"insert","lines":["t"],"id":1624}],[{"start":{"row":31,"column":0},"end":{"row":31,"column":21},"action":"remove","lines":["response=str(input())"],"id":1625}],[{"start":{"row":30,"column":37},"end":{"row":31,"column":0},"action":"remove","lines":["",""],"id":1626}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"remove","lines":["r"],"id":1627}],[{"start":{"row":32,"column":7},"end":{"row":32,"column":8},"action":"remove","lines":["e"],"id":1628}],[{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"remove","lines":["b"],"id":1629}],[{"start":{"row":32,"column":5},"end":{"row":32,"column":6},"action":"remove","lines":["m"],"id":1630}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":5},"action":"remove","lines":["u"],"id":1631}],[{"start":{"row":32,"column":3},"end":{"row":32,"column":4},"action":"remove","lines":["n"],"id":1632}],[{"start":{"row":32,"column":3},"end":{"row":32,"column":4},"action":"insert","lines":["r"],"id":1633}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":5},"action":"insert","lines":["e"],"id":1634}],[{"start":{"row":32,"column":5},"end":{"row":32,"column":6},"action":"insert","lines":["s"],"id":1635}],[{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"insert","lines":["p"],"id":1636}],[{"start":{"row":32,"column":7},"end":{"row":32,"column":8},"action":"insert","lines":["o"],"id":1637}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"insert","lines":["n"],"id":1638}],[{"start":{"row":32,"column":9},"end":{"row":32,"column":10},"action":"insert","lines":["s"],"id":1639}],[{"start":{"row":32,"column":10},"end":{"row":32,"column":11},"action":"insert","lines":["e"],"id":1640}],[{"start":{"row":35,"column":19},"end":{"row":35,"column":20},"action":"remove","lines":["e"],"id":1641}],[{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"remove","lines":["s"],"id":1642}],[{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"remove","lines":["n"],"id":1643}],[{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"remove","lines":["o"],"id":1644}],[{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"remove","lines":["p"],"id":1645}],[{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"remove","lines":["s"],"id":1646}],[{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"remove","lines":["e"],"id":1647}],[{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"remove","lines":["r"],"id":1648}],[{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"remove","lines":["="],"id":1649}],[{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"remove","lines":["="],"id":1650}],[{"start":{"row":35,"column":9},"end":{"row":35,"column":10},"action":"remove","lines":[")"],"id":1651}],[{"start":{"row":35,"column":8},"end":{"row":35,"column":9},"action":"remove","lines":["("],"id":1652}],[{"start":{"row":35,"column":7},"end":{"row":35,"column":8},"action":"remove","lines":["t"],"id":1653}],[{"start":{"row":35,"column":6},"end":{"row":35,"column":7},"action":"remove","lines":["u"],"id":1654}],[{"start":{"row":35,"column":5},"end":{"row":35,"column":6},"action":"remove","lines":["p"],"id":1655}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":5},"action":"remove","lines":["n"],"id":1656}],[{"start":{"row":35,"column":3},"end":{"row":35,"column":4},"action":"remove","lines":["i"],"id":1657}],[{"start":{"row":35,"column":3},"end":{"row":35,"column":4},"action":"insert","lines":["r"],"id":1658}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":5},"action":"insert","lines":["e"],"id":1659}],[{"start":{"row":35,"column":5},"end":{"row":35,"column":6},"action":"insert","lines":["s"],"id":1660}],[{"start":{"row":35,"column":6},"end":{"row":35,"column":7},"action":"insert","lines":["p"],"id":1661}],[{"start":{"row":35,"column":7},"end":{"row":35,"column":8},"action":"insert","lines":["o"],"id":1662}],[{"start":{"row":35,"column":8},"end":{"row":35,"column":9},"action":"insert","lines":["n"],"id":1663}],[{"start":{"row":35,"column":9},"end":{"row":35,"column":10},"action":"insert","lines":["s"],"id":1664}],[{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["e"],"id":1665}],[{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":["="],"id":1666}],[{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["="],"id":1667}],[{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"insert","lines":["i"],"id":1668}],[{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"insert","lines":["n"],"id":1669}],[{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"insert","lines":["t"],"id":1670}],[{"start":{"row":35,"column":16},"end":{"row":35,"column":18},"action":"insert","lines":["()"],"id":1671}],[{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["i"],"id":1672}],[{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"insert","lines":["n"],"id":1673}],[{"start":{"row":35,"column":19},"end":{"row":35,"column":20},"action":"insert","lines":["p"],"id":1674}],[{"start":{"row":35,"column":20},"end":{"row":35,"column":21},"action":"insert","lines":["u"],"id":1675}],[{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"insert","lines":["t"],"id":1676}],[{"start":{"row":35,"column":22},"end":{"row":35,"column":24},"action":"insert","lines":["()"],"id":1677}],[{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"remove","lines":["e"],"id":1678}],[{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":["s"],"id":1679}],[{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":["n"],"id":1680}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["o"],"id":1681}],[{"start":{"row":30,"column":3},"end":{"row":30,"column":4},"action":"remove","lines":["p"],"id":1682}],[{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"remove","lines":["s"],"id":1683}],[{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"remove","lines":["e"],"id":1684}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["r"],"id":1685}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"insert","lines":["n"],"id":1686}],[{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"insert","lines":["u"],"id":1687}],[{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"insert","lines":["m"],"id":1688}],[{"start":{"row":30,"column":3},"end":{"row":30,"column":4},"action":"insert","lines":["b"],"id":1689}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":["e"],"id":1690}],[{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":["r"],"id":1691}],[{"start":{"row":30,"column":20},"end":{"row":30,"column":35},"action":"remove","lines":["or str(input())"],"id":1692}],[{"start":{"row":30,"column":19},"end":{"row":30,"column":20},"action":"remove","lines":[" "],"id":1693}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":26},"action":"remove","lines":["if response==int(input()):"],"id":1694}],[{"start":{"row":34,"column":0},"end":{"row":35,"column":0},"action":"remove","lines":["",""],"id":1695}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"insert","lines":["t"],"id":1696}],[{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"insert","lines":["r"],"id":1697}],[{"start":{"row":29,"column":2},"end":{"row":29,"column":3},"action":"insert","lines":["y"],"id":1698}],[{"start":{"row":29,"column":3},"end":{"row":29,"column":4},"action":"insert","lines":[":"],"id":1699}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "],"id":1700},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":33,"column":63},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":1701},{"start":{"row":34,"column":0},"end":{"row":34,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":34,"column":8},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":1702},{"start":{"row":35,"column":0},"end":{"row":35,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":8},"action":"remove","lines":["    "],"id":1703}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"remove","lines":["    "],"id":1704}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":1},"action":"insert","lines":["e"],"id":1705}],[{"start":{"row":35,"column":1},"end":{"row":35,"column":2},"action":"insert","lines":["x"],"id":1706}],[{"start":{"row":35,"column":2},"end":{"row":35,"column":3},"action":"insert","lines":["c"],"id":1707}],[{"start":{"row":35,"column":3},"end":{"row":35,"column":4},"action":"insert","lines":["e"],"id":1708}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":5},"action":"insert","lines":["p"],"id":1709}],[{"start":{"row":35,"column":5},"end":{"row":35,"column":6},"action":"insert","lines":["t"],"id":1710}],[{"start":{"row":35,"column":6},"end":{"row":35,"column":7},"action":"insert","lines":[":"],"id":1711}],[{"start":{"row":35,"column":7},"end":{"row":35,"column":8},"action":"insert","lines":["V"],"id":1712}],[{"start":{"row":35,"column":8},"end":{"row":35,"column":9},"action":"insert","lines":["a"],"id":1713}],[{"start":{"row":35,"column":9},"end":{"row":35,"column":10},"action":"insert","lines":["l"],"id":1714}],[{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["u"],"id":1715}],[{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":["e"],"id":1716}],[{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["E"],"id":1717}],[{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"insert","lines":["r"],"id":1718}],[{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"insert","lines":["r"],"id":1719}],[{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"insert","lines":["o"],"id":1720}],[{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["r"],"id":1721}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "],"id":1722}],[{"start":{"row":36,"column":0},"end":{"row":37,"column":0},"action":"remove","lines":["",""],"id":1723}]]},"ace":{"folds":[],"scrolltop":280.5,"scrollleft":0,"selection":{"start":{"row":36,"column":0},"end":{"row":36,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":16,"state":"start","mode":"ace/mode/python"}},"timestamp":1514510539531}