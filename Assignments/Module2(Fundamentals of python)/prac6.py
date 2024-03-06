## With the use of temp variable
x = 10
y = 20

temp = x
x = y
y = temp

print("Enter value of x :",x)
print("Enter value of y :",y)

## Without using temp variable

x = 10
y = 20

x,y = y,x

print("After Swapping")
print("Value of x :",x,"Value of :",y)
