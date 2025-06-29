Python 基础知识学习笔记



一、Python 简介



Python 是一种高级、解释型、面向对象的编程语言，由 Guido van Rossum 于 1989 年开发。它以简洁、易读的语法著称，广泛应用于 Web 开发、数据分析、人工智能、自动化脚本等领域。Python 的设计哲学强调代码的可读性和简洁性，使用缩进来表示代码块，而非传统的大括号。


二、安装与环境配置



### 2.1 安装 Python&#xA;



*   **官网下载**：访问 Python 官方网站（[https://www.python.org/downloads/](https://www.python.org/downloads/)），根据操作系统下载对应的安装包。


*   **安装过程**：运行安装包，勾选 “Add Python to PATH” 选项，方便在命令行中直接调用 Python 命令，然后按照提示完成安装。


### 2.2 环境配置&#xA;



*   **命令行检查**：打开命令提示符（Windows）或终端（Linux/macOS），输入 `python` 或 `python3` ，若出现 Python 解释器的交互界面，则安装成功。


*   **虚拟环境**：使用 `venv` 模块创建虚拟环境，避免不同项目间依赖冲突。




```
\# 创建虚拟环境


python -m venv myenv


\# 激活虚拟环境（Windows）


myenv\Scripts\activate


\# 激活虚拟环境（Linux/macOS）


source myenv/bin/activate
```

三、基础语法



### 3.1 注释&#xA;



*   **单行注释**：使用 `#` 开头，用于解释单行代码。




```
\# 这是一个单行注释


print("Hello, World!")
```



*   **多行注释**：使用三个连续的单引号 `'''` 或双引号 `"""` 包裹注释内容。




```
'''


这是一个


多行注释


'''
```

### 3.2 变量与数据类型&#xA;



*   **变量命名规则**：由字母、数字、下划线组成，不能以数字开头，区分大小写，且不能使用 Python 关键字（如 `if`、`for`、`while` 等）。


*   **常见数据类型**：



    *   **整数（int）**：表示没有小数部分的数字，例如 `10`、`-5`。


    *   **浮点数（float）**：表示带有小数部分的数字，例如 `3.14`、`-2.5`。


    *   **字符串（str）**：用单引号、双引号或三引号包裹的文本，例如 `'Hello'`、`"World"`、`'''Python'''`。


    *   **布尔值（bool）**：只有两个取值 `True` 和 `False`，常用于逻辑判断。


    *   **列表（list）**：有序、可变的数据集合，用方括号 `[]` 表示，例如 `[1, 2, 3, 'a', 'b']`。


    *   **元组（tuple）**：有序、不可变的数据集合，用圆括号 `()` 表示，例如 `(1, 2, 3)`。


    *   **集合（set）**：无序、不重复的数据集合，用花括号 `{}` 表示，例如 `{1, 2, 3}`。


    *   **字典（dict）**：以键值对形式存储数据的集合，用花括号 `{}` 表示，例如 `{'name': 'Alice', 'age': 25}`。


### 3.3 运算符&#xA;



*   **算术运算符**：`+`（加）、`-`（减）、`*`（乘）、`/`（除）、`//`（整除）、`%`（取余）、`**`（幂运算）。




```
print(10 + 5)  # 输出 15


print(10 / 3)  # 输出 3.3333333333333335


print(10 // 3)  # 输出 3


print(10 % 3)  # 输出 1


print(2 \*\* 3)  # 输出 8
```



*   **比较运算符**：`==`（等于）、`!=`（不等于）、`<`（小于）、`>`（大于）、`<=`（小于等于）、`>=`（大于等于），返回布尔值。




```
print(10 > 5)  # 输出 True


print(10 == 5)  # 输出 False
```



*   **逻辑运算符**：`and`（逻辑与）、`or`（逻辑或）、`not`（逻辑非），返回布尔值。




```
print(True and False)  # 输出 False


print(True or False)  # 输出 True


print(not True)  # 输出 False
```



*   **赋值运算符**：`=`（赋值）、`+=`（加等于）、`-=`（减等于）等。




```
x = 10


x += 5  # 等价于 x = x + 5，此时 x 的值为 15
```

四、控制结构



### 4.1 条件语句（if-elif-else）&#xA;

用于根据条件执行不同的代码块。




```
age = 18


if age < 18:


&#x20;   print("未成年人")


elif age == 18:


&#x20;   print("刚成年")


else:


&#x20;   print("成年人")
```

### 4.2 循环语句&#xA;



*   **for 循环**：常用于遍历可迭代对象（如列表、字符串等）。




```
fruits = \["apple", "banana", "cherry"]


for fruit in fruits:


&#x20;   print(fruit)
```



*   **while 循环**：在条件为真时重复执行代码块。




```
count = 0


while count < 5:


&#x20;   print(count)


&#x20;   count += 1
```



*   **break 和 continue**：`break` 用于跳出循环，`continue` 用于跳过当前循环的剩余代码，继续下一次循环。




```
for i in range(10):


&#x20;   if i == 5:


&#x20;       break  # 当 i 等于 5 时，跳出循环


&#x20;   print(i)


for j in range(10):


&#x20;   if j % 2 == 0:


&#x20;       continue  # 当 j 是偶数时，跳过本次循环


&#x20;   print(j)
```

五、函数



### 5.1 定义函数&#xA;

使用 `def` 关键字定义函数，可以有参数和返回值。




```
def add(a, b):


&#x20;   return a + b


result = add(3, 5)


print(result)  # 输出 8
```

### 5.2 函数参数&#xA;



*   **位置参数**：按照参数定义的顺序传递参数。




```
def greet(name, age):


&#x20;   print(f"Hello, {name}. You are {age} years old.")


greet("Alice", 25)
```



*   **默认参数**：为参数设置默认值，调用函数时若不传递该参数，则使用默认值。




```
def greet(name, age=18):


&#x20;   print(f"Hello, {name}. You are {age} years old.")


greet("Bob")  # 输出 Hello, Bob. You are 18 years old.
```



*   **可变参数**：`*args` 用于接收任意数量的位置参数，`**kwargs` 用于接收任意数量的关键字参数。




```
def sum\_numbers(\*args):


&#x20;   total = 0

&#x20;   for num in args:


&#x20;       total += num


&#x20;   return total


print(sum\_numbers(1, 2, 3, 4, 5))  # 输出 15

def print\_info(\*\*kwargs):


&#x20;   for key, value in kwargs.items():


&#x20;       print(f"{key}: {value}")


print\_info(name="Alice", age=25, city="New York")
```

六、模块与包



### 6.1 模块&#xA;

模块是包含 Python 定义和语句的文件，可以导入其他 Python 程序中使用。




*   **创建模块**：在 `.py` 文件中编写代码，例如 `my_module.py`。




```
\# my\_module.py

def hello():


&#x20;   print("Hello from my module!")
```



*   **导入模块**：




```
import my\_module


my\_module.hello()  # 输出 Hello from my module!


from my\_module import hello


hello()  # 输出 Hello from my module!


from my\_module import \*


hello()  # 输出 Hello from my module!
```

### 6.2 包&#xA;

包是一个包含 `__init__.py` 文件的目录，用于组织多个模块。`__init__.py` 文件可以为空，也可以包含初始化代码。




```
my\_package/


&#x20;   \_\_init\_\_.py

&#x20;   module1.py

&#x20;   module2.py
```

在其他文件中导入包内的模块：




```
from my\_package import module1


module1.some\_function()
```

以上便是 Python 基础知识的相关内容。

