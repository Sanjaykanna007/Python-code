n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))
if n1>n2 and n2>n3:
    print("Number 1 is the greatest")
elif n3>n2 and n1<n2:
    print("Number 3 is the greatest")
else:
    print("Number 2 is the greatest")
