from decrypto import decrypt
from crypto import encrypt

print('Bem vindo ao programa de criptografia, use esse programa para salvar mensagens importantes a fim de descrição eficaz.')

print('='*119)

print('OPTIONS:')

while True:
    options = int(input('\n\n Digite [1] para Criptografar um texto ou [2] para Descriptografar. Ou digite [3] para sair: '))
    if options == 1:
        print()
        encrypt()
    elif options == 2:
        decrypt()
    elif options == 3:
        break

