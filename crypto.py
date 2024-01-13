def encrypt(text=''):
    text = input('Enter the text to be encrypted: ')
    list1 = []
    list2 = []
    list3 = []

    for char_1 in text:
        if char_1.isalpha():
            char_1 = ord(char_1)+3
            char_1 = chr(char_1)
            list1.append(char_1)
        else:
            list1.append(char_1)

    for letter in list1[::-1]:
        list2.append(letter)
    list1.clear()

    trunk = len(list2) // 2
    for trk1 in list2[trunk:]:
        list1.append(trk1)

    for trk2 in list2[:trunk]:
        list3.append(trk2)
    list2.clear()

    for char_2 in list1:
        char_2 = ord(char_2)-1
        char_2 = chr(char_2)
        list2.append(char_2)
    list1.clear()

    for c in list3:
        list1.append(c)
    for d in list2:
        list1.append(d)

    for line in list1:
        print(f'{line}',end='')



