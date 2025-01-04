# # write a program to input 2 numbers & print their sum

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# sum = num1+num2
# print("sum of",num1,"and",num2,"is :",sum)


# # wap to input side of a square and print its area
# side = int(input("enter side of square: "))
# area = side*side
# print("area of square is :",area)


# # wap to input 2 floating point numbers & print their average
# num1 = float(input("enter first number: "))
# num2 = float(input("enter second number: "))
# avg = (num1+num2)/2
# print("average of",num1,"and",num2,"is :",avg)


# """ wap to input 2 int numbers a and b.
# print True if a is greater then or equal to b. if not print False """

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# if num1>=num2:
#     print("True")
# else:
#     print("False")


# """ Lecture : 2 practice sets """


# # 1 Strings 
# # String is data type the stores a swquence of characters

# str1 = "Hello"
# str2 = 'World'
# str3 = """Hello World"""
# print(str1)
# print(str2)
# print(str3)

# # # String Operations
# # 1 String Concatenation
# # Concatenation is the process of combining two strings

# str1 = "Hello"
# str2 = "World"
# str3 = str1+str2
# print(str3)

# # 2 String Repetition
# # Repetition is the process of repeating a string multiple times

# str1 = "Hello"
# str2 = str1*3
# print(str2)

# # 3 String Slicing
# # Slicing is the process of extracting a part of a string

# str1 = "Hello World"
# print(str1[0:5])
# print(str1[5:11])

# # 4 String Length
# # Length is the number of characters in a string

# str1 = "Hello World"
# print(len(str1))


# # 5 String Membership
# # Membership is the process of checking if a string is present in another string

# str1 = "Hello World"
# print("Hello" in str1)
# print("World" in str1)
# print("Hello" not in str1)
# print("World" not in str1)

# # 6 String Comparison
# # Comparison is the process of comparing two strings

# str1 = "Hello"
# str2 = "World"
# print(str1==str2)
# print(str1!=str2)
# print(str1>str2)
# print(str1<str2)
# print(str1>=str2)
# print(str1<=str2)

# 7 String Formatting
# Formatting is the process of formatting a string

# str1 = "Hello"
# str2 = "World"
# print("Hello %s"%str2)
# print("Hello %s"%str1)
# print("Hello %s %s"%(str1,str2))

# 8 String Methods
# Methods are functions that are associated with objects

str1 = "Hello World"
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.capitalize())
print(str1.swapcase())
print(str1.find("World"))
print(str1.replace("World","India"))
print(str1.split(" "))
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.isspace())
print(str1.startswith("Hello"))
print(str1.endswith("World"))

# 9 Escape Sequences
# Escape sequences are used to represent special characters