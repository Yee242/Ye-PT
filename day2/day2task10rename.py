import os
import re


def windows_natural_sort_key(s):
    """生成适用于Windows自然排序的键（处理数字和字母混合的文件名）"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


def rename_images_with_names(names_file, image_folder):
    """根据名字文件中的姓名批量重命名图片文件夹中的图片（Windows自然排序）"""
    # 检查文件和文件夹是否存在
    if not os.path.exists(names_file):
        print(f"错误：未找到名字文件 - {names_file}")
        return
    if not os.path.exists(image_folder):
        print(f"错误：未找到图片文件夹 - {image_folder}")
        return

    try:
        # 读取名字文件（使用utf-8编码兼容中文）
        with open(names_file, 'r', encoding='utf-8') as f:
            names = [name.strip() for name in f if name.strip()]  # 过滤空行和空白字符

        if not names:
            print("错误：名字文件中没有有效姓名")
            return

        # 获取图片文件夹中的所有文件
        image_files = [f for f in os.listdir(image_folder)
                       if os.path.isfile(os.path.join(image_folder, f))]

        if not image_files:
            print(f"错误：{image_folder} 中没有找到图片文件")
            return

        # 按Windows自然排序规则对图片文件排序
        image_files.sort(key=windows_natural_sort_key)
        print(f"已按Windows自然排序规则排列图片文件，共 {len(image_files)} 个")

        # 重命名逻辑（按排序后的顺序匹配名字和图片）
        rename_count = min(len(names), len(image_files))
        for i in range(rename_count):
            old_name = image_files[i]
            ext = os.path.splitext(old_name)[1]  # 保留原始文件扩展名
            new_name = f"{names[i]}{ext}"

            old_path = os.path.join(image_folder, old_name)
            new_path = os.path.join(image_folder, new_name)

            os.rename(old_path, new_path)
            print(f"重命名：{old_name} -> {new_name}")

        # 处理数量不匹配的情况
        if len(names) < len(image_files):
            print(f"提示：剩余 {len(image_files) - len(names)} 张图片未重命名（名字数量不足）")
        elif len(names) > len(image_files):
            print(f"提示：剩余 {len(names) - len(image_files)} 个名字未使用（图片数量不足）")

        print(f"批量重命名完成，共处理 {rename_count} 个文件")

    except Exception as e:
        print(f"操作异常：{str(e)}")


if __name__ == "__main__":
    # 指定文件和文件夹路径（根据需求修改）
    base_path = r"D:\Ye-PT"
    names_file_path = os.path.join(base_path, "student.txt")
    image_folder_path = os.path.join(base_path, "pic")

    print(f"开始执行批量重命名（Windows自然排序模式）：")
    print(f"名字文件：{names_file_path}")
    print(f"图片文件夹：{image_folder_path}")
    print("-" * 50)

    rename_images_with_names(names_file_path, image_folder_path)