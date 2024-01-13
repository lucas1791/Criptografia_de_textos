from decrypto import decrypt
from crypto import encrypt

print('\033[32mBem vindo ao programa de criptografia, use esse programa para salvar mensagens importantes a fim de descrição eficaz.\033[m')

print('\033[36m=\033[m'*119)

print('\033[32mOPTIONS:\033[m')

while True:
    try:
        options = int(input('\n\n\033[34mDigite [1] para Criptografar um texto ou [2] para Descriptografar. Ou digite [3] para sair: \033[m'))

        if options == 1:
            print()
            encrypt()
        elif options == 2:
            decrypt()
        elif options == 3:
            break
        elif options != 1 or options != 2 or options != 3:
            print('\033[31mERRO, ESSA OPÇÃO NÃO EXISTE!\033[m')
        
    except ValueError:
        print('\033[31mERRO, ESSA OPÇÃO NÃO EXISTE!\033[m')

