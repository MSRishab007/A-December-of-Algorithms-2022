#Problem 2
x=input("Input: ")
y=len(x)
if x[y-2:]=="ae":
    z=x[y-4:y-2]
    for i in range(0,y-4):
        z=z+x[i]
    print("Output:",z)
else:
    print("Output: Invalid Input")