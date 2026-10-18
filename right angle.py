print("Making a half right triangle")
n= int(input("Please enter the number of rows: "))
for row in range(n):
    for column in range(row+1): 
        print("*", end=" ")
    print()