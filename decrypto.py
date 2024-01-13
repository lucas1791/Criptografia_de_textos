def decrypt(text=''):
    text = input('Enter the text to be decrypted: ')
    list1 = []
    list2 = []
    list3 = []

    trunk = len(text) // 2
    for trk1 in text[trunk:]: #segunda metade
        list1.append(trk1)

    for trk2 in text[:trunk]: #primeira metade
        list2.append(trk2)

    #tratar a segunda metade
    for char_2 in list1:
        char_2 = ord(char_2)+1
        char_2 = chr(char_2)
        list3.append(char_2) # segunda metade tratada lista 3
    list1.clear()

    for letter2 in list2:
        list1.append(letter2) #adicionando a primeira metade
    list2.clear()

    for letter3 in list3:
        list1.append(letter3) #adicionando a seunda metade (1° tratada)
    list3.clear()

    #desinverter list 1
    for letter in list1[::-1]:
        list2.append(letter)
    list1.clear()

    #lista 2 esta com todos os caracteres e desinvertido

    for char_1 in list2:
        if char_1.isalpha():
            char_1 = ord(char_1)-3
            char_1 = chr(char_1)
            list1.append(char_1)
        else:
            list1.append(char_1)

    #printando o que ja foi totalmente tratado
    for line_ in list1:
        print(f'{line_}', end='')
