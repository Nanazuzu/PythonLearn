def decrypt_shift_cipher(s: str, n: int) -> str:
    ret = "" 
    for index in s:
        mid = ord(index)
        if mid - n < 97:
            dist = 97 - mid + n - 1
            ret += chr(122 - dist)
        else:
            ret += chr(mid - n)
    return ret  #It can make with module
                #chr((ord(ch) - ord('a') - n) % 26 + ord('a'))
                #Like this.

print(decrypt_shift_cipher("cde", 2))
print(decrypt_shift_cipher("zab", 2))
print(decrypt_shift_cipher("nopqrstuvwxyzabcdefghijklm", 13))