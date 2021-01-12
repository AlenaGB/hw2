print('game cryptography'.upper())
# заглавные буквы

myList = input("let's play! You need to send a message to your friend. No one should understand it.\nEnter your messege and i will encrypt this word... ").split()
# print(myList)
for el in myList:
    elList = list(el)
    # print(elList)
    # print(len(elList))
    for i in range(1, len(elList), 2):
        elList.insert(i - 1, elList.pop(i))
    print(' '.join(elList))