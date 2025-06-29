nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# (1) 使用切片反转列表
reversed_nums = nums[::-1]
print("反转后的列表:", reversed_nums)  # 输出: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# (2) 提取索引为0、2、4的元素
selected_elements = [reversed_nums[i] for i in [0, 2, 4]]
print("提取的元素:", selected_elements)  # 输出: [9, 7, 5]