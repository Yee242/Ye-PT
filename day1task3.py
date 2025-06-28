#练习1
numbers = [n for n in range(1, 101)]
evens = [n for n in numbers if n % 2 == 0]
print("1-100中的偶数：", evens)

#练习2
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# 测试示例
original = [3, 1, 2, 1, 4, 3]
unique = remove_duplicates(original)
print("去重后的列表：", unique)

#练习3
keys = ["a", "b", "c"]
values = [1, 2, 3]
merged_dict = dict(zip(keys, values))
print("合并后的字典：", merged_dict)

#练习4
student = ("张三", 20, 90)
name, age, score = student
print(f"姓名：{name}，年龄：{age}，成绩：{score}")