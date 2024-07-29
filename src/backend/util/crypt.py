# coding: utf-8
import base64
import hashlib
import json
from Crypto.Cipher import AES
from Crypto import Random


def encrypt(decrypted_data, token):
    private_key = hashlib.sha256(token.encode()).digest()
    rem = len(decrypted_data) % 16
    padded = str.encode(decrypted_data) + (b'\0' * (16 - rem)) if rem > 0 else str.encode(decrypted_data)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CFB, iv, segment_size=128)
    enc = cipher.encrypt(padded)[:len(decrypted_data)]
    return base64.b64encode(iv + enc).decode()


def decrypt(encrypted_data, token):
    private_key = hashlib.sha256(token.encode()).digest()
    encrypted_data = base64.b64decode(encrypted_data)
    iv, value = encrypted_data[:16], encrypted_data[16:]
    rem = len(value) % 16
    padded = value + (b'\0' * (16 - rem)) if rem > 0 else value
    cipher = AES.new(private_key, AES.MODE_CFB, iv, segment_size=128)
    return (cipher.decrypt(padded)[:len(value)]).decode()


def main():
    key = 'YmrQCPJCUzbhNrnDMRoY26Y7XChcw8F+I2mD05eh6yM='
    data = json.dumps({"test": "test", "test2": "あああ"})
    encrypted = encrypt(data, key)
    print(encrypted)
    # encrypted = "d4OOIyv9grrlUuvbuPg5S+Wfmt+nlW9o4G46s+X7A7gTFPZzri…5CuS52lmUYJBTbsfHrYqHkD1DCncUDjLh+mMc8y3QOkkEcyg="
    dec = decrypt(encrypted, key)
    print(dec)


if __name__== '__main__':
    main()

