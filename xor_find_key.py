import base64
import sys

args = sys.argv
print(args[1]) # clear text
print(args[2]) # encrypted text

clear_text = args[2].encode()
encrypted_text = args[1]
encrypted_raw = base64.b64decode(encrypted_text)


find_key = []
for i in range(len(clear_text)):
    dec = encrypted_raw[i] ^ clear_text[i]
    find_key = chr(dec)
    fingd_key.append(find_key)

print("".join(find_key))
