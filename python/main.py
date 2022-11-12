from base64 import b64encode, b64decode
from Crypto.Cipher import AES

iv = "1234567890abcdef"
key = "@ABCDEFGHI12345!"

pad = (lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16).encode())
unpad = (lambda s: s[:-ord(s[len(s)-1:])])
def AES_128_CBC_Encrypt(text: str, key: str, iv: str):
    key = key.encode()
    iv = iv.encode()
    text = text.encode()
    raw = pad(text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    crypted = cipher.encrypt(raw)
    return b64encode(crypted).decode("utf-8")
def AES_128_CBC_Decrypt(crypted: str, key: str, iv: str):
    key = key.encode()
    iv = iv.encode()
    crypted = b64decode(crypted)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(crypted)
    return unpad(decrypted).decode("utf-8")

if __name__ == "__main__":
    # Encrypt  -  Result : wP3XthWbuBMvNsDab2RHZQ==
    print(AES_128_CBC_Encrypt("encrypt text", key, iv))

    # Decrypt  -  Result : encrypt text
    print(AES_128_CBC_Decrypt("wP3XthWbuBMvNsDab2RHZQ==", key, iv))
