a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"0","1","2","3","4","5","6","7","8","9"]

b = str(input("คำที่ต้องการถอด: "))

key = int(input("key: "))

def caesar_cipher_decrypt(text, key):
    result = ""
    for char in text:
        if char in a:
            index = a.index(char)
            new_index = (index - key) % len(a)
            result += a[new_index]
        else:
            result += char  # กรณีที่ตัวอักษรไม่อยู่ใน `a`
    return result

decoded_word = caesar_cipher_decrypt(b, key)
print(f"คำที่ถอดรหัส: {decoded_word}")
