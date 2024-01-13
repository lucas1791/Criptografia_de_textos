# Import functions from the crypto and decrypto modules.
from decrypto import decrypt
from crypto import encrypt

# Greeting message.
print('\033[32mWelcome to the encryption program. Use this program to securely store important messages for effective description.\033[m')

print('\033[36m=\033[m'*119)

print('\033[32mOPTIONS:\033[m')

# Menu logic
while True:
    try:
        options = int(input('\n\n\033[34mEnter [1] to Encrypt a text or [2] to Decrypt. Or enter [3] to exit: \033[m'))  # Provides options for the user to choose between encryption, decryption, and exit. Ensures that the user does not input incorrect characters.

        if options == 1:
            print()
            encrypt()
        elif options == 2:
            decrypt()
        elif options == 3:
            break
        elif options != 1 or options != 2 or options != 3:
            print('\033[31mERROR, THIS OPTION DOES NOT EXIST!\033[m')
        
    except ValueError:
        print('\033[31mERROR, THIS OPTION DOES NOT EXIST!\033[m')
