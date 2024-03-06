inputString = input("Enter the string :")
count = 0
 
for i in inputString:
      count = count + 1
newString = inputString[:2 ] + inputString [count - 2: count ] 
 
print("Input string = " + inputString)
print("New String = "+ newString)