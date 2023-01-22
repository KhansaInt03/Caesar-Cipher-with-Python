from ordo import ascii_to_ordo

dict_char = ascii_to_ordo()

def Encryption_Caesar():
    text = input('Your Plaintext\n')
    shift = int(input('Shift [must more than 3] >> '))
    conv = [ values for letter in text for key,values in dict_char.items() if letter == key ]
    print()

    conv_shift = [ (item + shift)%94 for item in conv ]

    cipher = [ key for item in conv_shift for key, values in dict_char.items() if item == values ]
    print(*cipher, sep='')

def Decryption_Caesar():
    text2 = input('Your Ciphertext\n')
    conv = [ values for letter in text2 for key,values in dict_char.items() if letter == key ]
    shift2 = int(input('Shift [must more than 3] >> '))

    conv_shift = [ (item - shift2)%94 if item-shift2 != 0 else item-shift2+94 for item in conv ]

    plain = [ key for item in conv_shift for key, values in dict_char.items() if item == values ]
    print(*plain, sep='')

Encryption_Caesar()
# Decryption_Caesar()