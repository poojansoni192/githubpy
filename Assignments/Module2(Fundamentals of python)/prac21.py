str = input("Enter the string :")
    
if len(str) % 4 == 0:
        print(''.join(reversed(str)))
else:
    print(str)
        
