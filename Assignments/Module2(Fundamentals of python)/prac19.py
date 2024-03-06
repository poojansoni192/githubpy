str = input("Enter the sentence :")

snot = str.find("not")

spoor = str.find("poor")

if spoor>snot and snot>0 and spoor>0:
    str = str.replace(str[snot:(spoor+4)],"good")
    print(str)
    
else:
    print(str)