from Crypto.Cipher import AES


def print_matrix(block):
    for i in range(4):
        row = [f"{block[4 * i + j]:02X}" for j in range(4)]
        print(" ".join(row))


key = b"ThisIsA16ByteKey"  # 16 bytes = 128 bits
plaintext = b"ABCDEFGHIJKLMNOP"  # 16 bytes, exactly one AES block

cipher = AES.new(key, AES.MODE_ECB)

# Encryption
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext (hex):", ciphertext.hex())

# Decryption
decipher = AES.new(key, AES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
print_matrix(ciphertext)
