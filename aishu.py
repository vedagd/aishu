def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)
        else:
            result+=chr((ord(char)+s-97)%26+97)
    return result
text="rap"
S=1
print("Text:"+text)
print("Shift:"+str(S))
print("Cipher:"+encrypt(text,S))


