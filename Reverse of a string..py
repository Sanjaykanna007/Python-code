def reverse(word):
    str2=' '
    for i in word:
        str2=i + str2
    return str2   
str1=str(input("\n Enter a string:"))
print("\n The reverse of given string is:",reverse(str1))
