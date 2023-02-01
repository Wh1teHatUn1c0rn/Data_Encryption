# Data_Encryption

This script uses the Advanced Encryption Standard (AES) algorithm to encrypt and decrypt the data.

The encrypt_data function takes two arguments, the data to be encrypted and the key to be used for encryption.

The function pads the data so that its length is a multiple of the block size (16 bytes) before encrypting it using the key.

The decrypt_data function takes the same arguments, the data to be decrypted and the key to be used for decryption.

The function decrypts the data and then removes the padding added while encryption.

It is important to keep the key in secret and the key is used for both encryption and decryption.
