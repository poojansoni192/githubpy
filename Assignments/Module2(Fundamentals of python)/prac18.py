str = input("Enter the string :")

length =len(str)

if length>=3:
     
    if str[-3:] == "ing":
        str += "ly"
         
    elif length<3:
        print(str)

    else:
        str += "ing"
        
print(str)