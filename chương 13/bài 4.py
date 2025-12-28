with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("ID, tên sản phẩm, giá ")
    f.write("laptop, 1200")
    f.write("chuột máy tính 25")
    f.write("bàn phím 75")
cap_nhat = input("nhập ID từ sản phẩm cần cập nhập giá: ")
gia_moi = input("nhập giá mới: ")
danh_sach_moi = []
with open("san_pham.txt", "r", encoding="utf-8") as f:
    for dong in f:
        dong = dong.strip()
        if dong.startswith("cap_nhat" + ","):
            # Tách dữ liệu của dòng thành các phần
            phan = dong.split(", ")
            # Cập nhật giá mới
            phan[2] = gia_moi
            # Ghép lại thành dòng mới
            dong = ", ".join(phan)
        danh_sach_moi.append(dong)

# Ghi danh sách mới vào lại file san_pham.txt (ghi đè nội dung cũ)
with open("san_pham.txt", "w", encoding="utf-8") as f:
    for dong in danh_sach_moi:
        f.write(dong + "\n")

print(" Cập nhật giá sản phẩm thành công!")