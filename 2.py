print('game cryptography'.upper())
# заглавные буквы

myList = list(map(str,input("let's play! You need to send a message to your friend. No one should understand it.\nEnter your messege and i will encrypt this word... ").split()))
# print(myList)
# map(int, input().split())
# input() возвращает строку (например: "1 2 3")
# split() преобразует строку в list по разделителю - по умолчанию пробел
# map преобразует список в соответствие с функцией

for el in myList:
    elList = list(el)
    # print(elList)
    # print(len(elList))
    elList[::2], elList[1::2] = elList[1::2], elList[::2]
    print(' '.join(elList))

    # проблема с нечетным комличеством элементов в elList