myList  = list(map(str,input('Enter products separated by a space: ').split()))
# print(myList)
for item in enumerate(myList):
    # enumerate создает объект, который генерирует кортежи, состоящие из двух элементов - индекса элемента и самого элемента
    word = item[1]
    print(item[0]+1,word[:10])
    # print(type(word))
    # print(len(word))
