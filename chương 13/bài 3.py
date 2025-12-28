danh_sach = [1, 2, 3, 4, 5]
with open ("so_nguyen.txt", "w", encoding= "utf-8") as f: 
    for so in danh_sach: 
        f.write(str(so) + "\n")                                         # write chỉ ghi dc chuỗi nên phải đổi số thành chuỗi str(so)
print("Đã ghi danh sách số nguyên vào file so_nguyen.txt")             