str = input("Enter the string :")
n = str.split()
largest = len(n[0])

for i in n:
    if len(i)>largest:
        largest=len(i)
        
        
print("Largest string is :",largest)
