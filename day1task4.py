#练习1
#(1) 提取单词 "language"
s1 = "Python is a powerful programming language"
words = s1.split()
print(f"提取的单词是: {words[-1]}")

# (2) 连接字符串并重复输出3次
s2 = " Let's learn together"
combined = s1 + s2
print(f"重复3次的结果: {combined * 3}")

# (3) 输出所有以 p 或 P 开头的单词
p_words = [word for word in words if word.lower().startswith('p')]
print(f"以p或P开头的单词: {p_words}")

#练习2
s3 = " Hello, World! This is a test string. "

# (1) 去除字符串前后的空格
trimmed = s3.strip()
print("去除空格后的字符串：", trimmed)

# (2) 将所有字符转换为大写
upper_case = trimmed.upper()
print("转换为大写后的字符串：", upper_case)

# (3) 查找子串 "test" 的起始下标
index = trimmed.find("test")
print("子串 'test' 的起始下标：", index)

# (4) 将 "test" 替换为 "practice"
replaced = trimmed.replace("test", "practice")
print("替换后的字符串：", replaced)

# (5) 以空格为分隔符分割字符串，并用 "-" 连接
split_list = trimmed.split()
joined = "-".join(split_list)
print("连接后的字符串：", joined)