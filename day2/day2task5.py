#1.回文数判断
def is_palindrome(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    return num_str == reversed_str

# 测试示例
print("121是否为回文数：", is_palindrome(121))
print("123是否为回文数：", is_palindrome(123))

#2.任意参数平均值计算
def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

# 测试示例
print("平均值：", calculate_average(1, 2, 3, 4, 5))

#3.最长字符串查找
def find_longest_string(*strings):
    if not strings:
        return ""
    return max(strings, key=len)

# 测试示例
print("最长的字符串是：", find_longest_string("apple", "banana", "cherry"))

#4.矩形计算
# geometry.py (模块文件)
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

length = 5
width = 3
print(f"矩形面积：{rectangle_area(length, width)}")
print(f"矩形周长：{rectangle_perimeter(length, width)}")