print("Floyd Traingle")
number= 1
rows= int(input("PLease enter the number of rows: "))
for i in range(1,rows + 1):
    for j in range(1, i+1):
        print(number, end=" ")
        number= number + 1
    print()