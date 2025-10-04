import os

# 获取脚本所在目录的绝对路径
base_dir = os.path.dirname(os.path.abspath(__file__))

# 创建占位符文件的函数
def create_placeholder(file_path, content):
    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'已创建占位符: {file_path}')

# 创建背景图片占位符
bg_dir = os.path.join(base_dir, 'assets', 'img', 'background')
create_placeholder(os.path.join(bg_dir, 'hero1.jpg.txt'), '请将封面轮播第一张图片命名为hero1.jpg并放在此目录')
create_placeholder(os.path.join(bg_dir, 'hero2.jpg.txt'), '请将封面轮播第二张图片命名为hero2.jpg并放在此目录')
create_placeholder(os.path.join(bg_dir, 'hero3.jpg.txt'), '请将封面轮播第三张图片命名为hero3.jpg并放在此目录')
create_placeholder(os.path.join(bg_dir, 'sunset.jpg.txt'), '请将banner背景图片命名为sunset.jpg并放在此目录')

# 创建照片占位符
photos_dir = os.path.join(base_dir, 'assets', 'img', 'photos')
for i in range(1, 9):
    create_placeholder(os.path.join(photos_dir, f'g{i}.jpg.txt'), f'照片 {i} - 请将实际照片命名为g{i}.jpg并放在此目录')

# 创建祝福语图片占位符
wishes_dir = os.path.join(base_dir, 'assets', 'img', 'wishes')
for i in range(1, 4):
    create_placeholder(os.path.join(wishes_dir, f's{i}.jpg.txt'), f'祝福语卡片 {i} - 请将实际图片命名为s{i}.jpg并放在此目录')

# 创建音频文件占位符
audio_dir = os.path.join(base_dir, 'assets', 'audio')
create_placeholder(os.path.join(audio_dir, 'bgm.mp3.txt'), '请将背景音乐命名为bgm.mp3并放在此目录')
create_placeholder(os.path.join(audio_dir, 'egg.mp3.txt'), '请将彩蛋音频命名为egg.mp3并放在此目录')

print('\n所有占位符文件已创建完成!')
print('请按照占位符文件的提示，将实际文件放入对应的目录中。')