email = input("请输入您的邮箱地址：")
at_index = email.index('@')  # 会在没有@时抛出异常
username = email[:at_index]
print(f"提取的用户名是：{username}")#gthythyty