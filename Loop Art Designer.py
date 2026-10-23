print("Star Pyramid Pattern")
rows= int(input("Enter number of rows for star pattern:"))
for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()

print("FLOYD'S TRIANGLE")
rows= int(input("Enter the number of rows for the floyd's traingle: "))
number= 1

for i in range(1, 1+rows):
    for j in range(1, 1+i):
        print(number, end=" ")
        number+=1
    print()

print("DIAMOND NUMBER PATTERN")

row_size= int(input("Enter the number of rows for the diamond pattern: "))
if row_size%2==0:
    half_rows= row_size//2
else:
    half_rows= row_size//2+1                                    

space= half_rows - 1

for i in range(1, half_rows+1):
    for j in range(1, space+1):
        print(" ", end= "")

    space -=1
    number= 1

    for j in range(2*i-1):
        print(number, end="")
        number +=1
    print()

sapce= 1
for i in range(1,half_rows):
    for j in range(1, space+1):
        print(" ", end="")

    space += 1
    number =1

    for j in range(1,2*(half_rows-i)):
        print(number, end="")
        number +=1
   
    print()

print("LOOP ART DESIGN COMPLETE")
print("You created star, triangle and diamond patterns using nested loops.")