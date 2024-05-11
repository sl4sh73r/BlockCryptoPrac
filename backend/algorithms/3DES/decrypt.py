from Crypto.Cipher import DES3
import base64
import sys

def unpad(data):
    return data.rstrip(b'\0')

def decrypt(encrypted_data, key):
    if len(key) not in [16, 24]:
        print("Error: Key must be 16 or 24 bytes long.")
        return None

    if not encrypted_data:
        print("Error: Data to decrypt cannot be empty.")
        return None

    try:
        encrypted_data = base64.b64decode(encrypted_data)
    except Exception as e:
        print("Error: Failed to decode encrypted data.", str(e))
        return None

    iv = encrypted_data[:DES3.block_size]
    encrypted_data = encrypted_data[DES3.block_size:]

    try:
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
    except ValueError as e:
        print("Error: Invalid key or IV.", str(e))
        return None

    try:
        decrypted_data = unpad(cipher.decrypt(encrypted_data))
    except Exception as e:
        print("Error: Decryption failed.", str(e))
        return None

    return decrypted_data

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python decrypt.py <encrypted_data> <key>")
        sys.exit(1)

    try:
        encrypted_data = sys.argv[1].encode()
        key = sys.argv[2].encode()
    except UnicodeEncodeError as e:
        print("Error: Failed to encode input data or key.", str(e))
        sys.exit(1)

    result = decrypt(encrypted_data, key)
    if result:
        try:
            print(result.decode())
        except UnicodeDecodeError:
            print("Error: Result could not be decoded as UTF-8.")
    else:
        print("Decryption failed.")