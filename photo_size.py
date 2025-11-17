import os
from PIL import Image


def convert_to_square_png(input_folder, output_folder, size=200):
    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 支持的图片格式
    supported_formats = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_formats):
            try:
                # 打开图片
                with Image.open(os.path.join(input_folder, filename)) as img:
                    img = img.convert("RGBA")
                    width, height = img.size

                    # 计算缩放比例
                    scale = min(size / width, size / height)
                    new_width = int(width * scale)
                    new_height = int(height * scale)

                    # 缩放图片
                    img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # 创建正方形画布（透明背景）
                    square_img = Image.new('RGBA', (size, size), (255, 255, 255, 0))

                    # 居中粘贴
                    x = (size - new_width) // 2
                    y = (size - new_height) // 2
                    square_img.paste(img_resized, (x, y), img_resized)

                    # 保存为PNG
                    base_name = os.path.splitext(filename)[0]
                    output_filename = f"{base_name}.png"
                    square_img.convert("RGB").save(os.path.join(output_folder, output_filename), "PNG")
                    print(f"已转换: {filename} -> {output_filename}")

            except Exception as e:
                print(f"处理 {filename} 时出错: {str(e)}")


if __name__ == "__main__":
    # 示例调用（需替换为实际路径）
    input_folder = "photo/fm_b"
    output_folder = "photo/fm"
    convert_to_square_png(input_folder, output_folder, size=200)
    print("转换完成！")