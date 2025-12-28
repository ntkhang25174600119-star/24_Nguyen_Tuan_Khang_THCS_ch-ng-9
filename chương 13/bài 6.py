import csv

# 1. Tạo và ghi dữ liệu vào file nhan_vien.csv
with open("nhan_vien.csv", mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["ID", "Ten", "Luong"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"ID": 1, "Ten": "Nguyen Van A", "Luong": 45000})
    writer.writerow({"ID": 2, "Ten": "Tran Thi B", "Luong": 55000})
    writer.writerow({"ID": 3, "Ten": "Le Van C", "Luong": 60000})
    writer.writerow({"ID": 4, "Ten": "Pham Thi D", "Luong": 48000})

# 2 & 3. Đọc file bằng csv.DictReader
print("Nhân viên có mức lương trên 50000:")
with open("nhan_vien.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # 4. Duyệt từng hàng và in nhân viên có lương > 50000
    for row in reader:
        if int(row["Luong"]) > 50000:
            print(f"ID: {row['ID']}, Tên: {row['Ten']}, Lương: {row['Luong']}")
