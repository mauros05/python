import base64
import hashlib

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


HASH_NAME       = "SHA512"
IV_LENGHT       = 12 # initial vector lenght
ITERATION_COUNT = 65535
KEY_LENGHT      = 32 # 256-bit key
SALT_LENGHT     = 16
TAG_LENGHT      = 16

def encrypt(password ,plain_text):

    iv = get_random_bytes(IV_LENGHT)
    salt = get_random_bytes(SALT_LENGHT)

    secret = get_secret_key(password, salt)

    cipher = AES.new(secret, AES.MODE_GCM, iv)

    encrypted_message_byte, tag = cipher.encrypt_and_digest(plain_text.encode("utf-8"))

    cipher_byte = salt + iv + encrypted_message_byte + tag

    print(cipher_byte)

    encode_cipher_byte = base64.b64encode(cipher_byte)
    return bytes.decode(encode_cipher_byte)


def decrypt(password, cipher_message):
    decode_cipher_byte = base64.b64decode(cipher_message)

    iv = decode_cipher_byte[SALT_LENGHT : (SALT_LENGHT + IV_LENGHT)]
    salt = decode_cipher_byte[:SALT_LENGHT]
    encrypted_message_byte = decode_cipher_byte[(IV_LENGHT + SALT_LENGHT) : -TAG_LENGHT]

    tag = decode_cipher_byte[-TAG_LENGHT:]
    secret = get_secret_key(password, salt)
    cipher = AES.new(secret, AES.MODE_GCM, iv)

    decrypt_message_byte = cipher.decrypt_and_verify(encrypted_message_byte, tag)
    return decrypt_message_byte.decode("utf-8")


def get_secret_key(password, salt):
    return hashlib.pbkdf2_hmac(HASH_NAME, password.encode(), salt, ITERATION_COUNT, KEY_LENGHT)


secret_key = "banana"
plain_text = "Hola Mundo"

cipher_text = encrypt(secret_key, plain_text)
print(f'Ciphertext: {cipher_text}')
print(f'Decrypted text: {decrypt(secret_key, cipher_text)}')