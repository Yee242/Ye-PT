#练习1
x = 10
y = "10"
z = True

print(f"x 的类型是: {type(x)}")
print(f"y 的类型是: {type(y)}")
print(f"z 的类型是: {type(z)}")

#练习2
import math

radius = float(input("请输入圆的半径: "))
area = math.pi * (radius ** 2)

print(f"半径为 {radius} 的圆面积是: {area:.2f}")

#练习3
s = "3.14"

float_result = float(s)
int_result = int(float_result)

print(f"字符串转换为浮点数: {float_result}")
print(f"浮点数转换为整数: {int_result}")