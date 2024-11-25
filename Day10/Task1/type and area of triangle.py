

import math
print("Enter the lengths of the triangle sides:")
side_1=int(input("Side 1:"))
side_2=int(input("Side 2:"))
side_3=int(input("Side 3:"))
if side_1==side_2==side_3:
    print("Triangle Type:Equilatral")
elif side_1==side_2 or side_2==side_3 or side_3==side_1:
    print("Triangle Type:Isosceles")
else:
    print("Triangle Type:Scalene")

s=(side_1+side_2+side_3)/2
area=math.sqrt(s*(s-side_1)*(s-side_2)*(s-side_3))
print("Area of the Triangle:",area,"square units.")