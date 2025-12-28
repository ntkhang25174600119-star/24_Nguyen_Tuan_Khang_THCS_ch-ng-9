import os

# 1. Tạo thư mục temp_files
os.mkdir("temp_files")

# 2. Tạo tập tin file.txt trong thư mục temp_files
file_path = os.path.join("temp_files", "file.txt")
with open(file_path, "w") as f:
    f.write("Day la file txt")

# 3. Đổi tên file.txt thành new_file.txt
new_file_path = os.path.join("temp_files", "new_file.txt")
os.rename(file_path, new_file_path)

# 4. Di chuyển new_file.txt ra thư mục hiện tại
os.rename(new_file_path, "new_file.txt")

# 5. Xóa thư mục temp_files (sau khi đã chuyển file ra ngoài)
os.rmdir("temp_files")

print("Hoan thanh bai tap!")
