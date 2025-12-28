import os

# 1. Tạo thư mục gốc
os.mkdir("my_project")

# 2. Tạo các thư mục con
os.mkdir("my_project/src")
os.mkdir("my_project/docs")
os.mkdir("my_project/data")

# 3. Tạo các tập tin rỗng
open("my_project/src/main.py", "w").close()
open("my_project/docs/README.md", "w").close()
open("my_project/data/input.txt", "w").close()

# 4. In ra cấu trúc thư mục
print("my_project/")
for folder in os.listdir("my_project"):
    print(folder)
    for file in os.listdir("my_project/" + folder):
        print("  ", file)

