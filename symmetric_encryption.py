from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Elapsed time for {func.__name__}: {end_time - start_time} seconds.")
        return result
    return wrapper

def pad(data):
    length = 16 - (len(data) % 16)
    return data + (chr(length) * length).encode()

def unpad(data):
    return data[:-ord(data[-1:])]

@timer_decorator
def encrypt(key, plaintext):
    # Needs to be a multiple of 16 for ecb -->
    padded_plaintext = pad(plaintext)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded_plaintext)

    return ciphertext

@timer_decorator
def decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data)

    return plaintext

def main():

    key = get_random_bytes(32)
    plaintext = input("Enter the text to be encrypted: ").encode('utf-8')

    print("Here is the key:", base64.b64encode(key).decode('utf-8'))

    ciphertext = encrypt(key, plaintext)

    print("Here is the encrypted text:", base64.urlsafe_b64encode(ciphertext).decode())

    decrypted_plaintext = decrypt(key, ciphertext)

    print("Here is the plaintext after decryption:", decrypted_plaintext.decode())


    return

if __name__ == "__main__":
    main()
