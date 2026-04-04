def oddeven(num):
    if(num%2==0):
        return"EVEN"
    else:
        return'ODD'
n=int(input("Enter a number:"))
print("The given number is :",oddeven(n))
