import math
s1=int(input("Enter side 1: "))
s2=int(input("Enter the side 2: "))
s3=int(input("Enter the side 3: "))
s=(s1+s2+s3)/2
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("Area of the triangle is :", area)