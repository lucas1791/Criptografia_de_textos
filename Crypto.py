text_in = input('Digite o texo: ')
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []

for char_1 in text_in:
    if char_1.isalpha():
        char_1 = ord(char_1)+3
        char_1 = chr(char_1)
        list1.append(char_1)
    else:
        list1.append(char_1)

for letter in list1[::-1]:
    list3.append(letter)

trunk = len(list3) // 2

for trk1 in list3[trunk:]:
    list2.append(trk1)

for trk2 in list3[:trunk]:
    list4.append(trk2)


for char_2 in list2:
    char_2 = ord(char_2)-1
    char_2 = chr(char_2)
    list5.append(char_2)

for c in list4:
    list6.append(c)
for d in list5:
    list6.append(d)

for crip in list6:
    print(f'{crip}',end='')