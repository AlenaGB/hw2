myList = [2, 'list', 45.3, None, [], {}, True, None, range(11)]
for i, item in enumerate(myList,1):
    print (f"{i} {item} - {type(item)}")