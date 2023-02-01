from Crypto.Cipher import AES
import os


def encrypt_data(data: bytes, key: bytes):
    BLOCK_SIZE = 16
    PADDING = '{'

    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data))


def decrypt_data(data: bytes, key: bytes):
    PADDING = '{'

    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = cipher.decrypt(data)
    return padded_data.rstrip(PADDING)


key = os.urandom(16)  # create a random key of 16 bytes
data = b'example data'

encrypted_data = encrypt_data(data, key)
decrypted_data = decrypt_data(encrypted_data, key)

print(f'Encrypted data: {encrypted_data}')
print(f'Decrypted data: {decrypted_data}')