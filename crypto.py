def encrypt(text=''):
    '''
    Description:
    This function is used to encrypt texts using the predefined pattern in the logic below.

    Parameters:
    - text (str): The only parameter to be entered is the text you want to encrypt.

    Returns:
    (str): This function only returns the encrypted text.
    '''
    text = input('Enter the text to be encrypted: ')  # Input of the text
    list1 = []
    list2 = []
    list3 = []

    # Performing the first treatment on the text, moving 3 positions to the right in the ASCII table.
    for char_1 in text:
        
        char_1 = ord(char_1) + 5
        char_1 = chr(char_1)
        list1.append(char_1)
        

    # Reversing the text.
    for letter in list1[::-1]:
        list2.append(letter)
    list1.clear()

    # Splitting the text into two, in order to handle each part separately.
    truncate_e = len(list2) // 2
    for truncat_1 in list2[truncate_e:]:
        list1.append(truncat_1)  # Second half.

    for truncat_2 in list2[:truncate_e]:
        list3.append(truncat_2)  # First half.
    list2.clear()

    # Performing the second treatment, moving 1 position to the left in the ASCII table for any character.
    for char_2 in list1:
        char_2 = ord(char_2) - 2
        char_2 = chr(char_2)
        list2.append(char_2)
    list1.clear()

    # Adding the two halves (already treated) to list1.
    for c in list3:
        list1.append(c)
    for d in list2:
        list1.append(d)

    # Printing the encrypted text.
    for line in list1:
        print(f'\033[33m{line}\033[m', end='')
