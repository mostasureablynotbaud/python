import string








CHAR_SET = string.printable[:-5]
SUB_CHARS = CHAR_SET[-3:]+CHAR_SET[:-3]

ENCRYPT_dict = {}
DECRYPT_dict = {}
for i,k in enumerate(CHAR_SET):
    v = SUB_CHARS[i]
    ENCRYPT_dict[k] = v
    DECRYPT_dict[v] = k

for c in string.printable[-5:]:
    ENCRYPT_dict[c] = c
    DECRYPT_dict[c] = c


TEST_msg = 'I have yet to see Monty Python. I heard they were funny.'
INPUT_file_name = 'cryptopy_input.txt'
OUTPUT_file_name = 'cryptopy_output.txt'



def encrypt_msg(plaintext, encrypt_dict):
    ciphertext = []
    for k in plaintext:
        v = encrypt_dict[k]
        ciphertext.append(v)
    return ''.join(ciphertext)




def decrypt_msg(ciphertext, decrypt_dict):
    plaintext = []
    for k in ciphertext:
        v = decrypt_dict[k]
        plaintext.append(v)
    return ''.join(plaintext)





message = input('Type your message:\n')
ciphertext = encrypt_msg(message, ENCRYPT_dict)
plaintext = decrypt_msg(message, DECRYPT_dict)
print('The message encrypted')
print(ciphertext)
print
print('The message decrypted')
print(plaintext)




















