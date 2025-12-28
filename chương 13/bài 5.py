# Mở tệp nguồn để đọc nhị phân
with open("nguon.bin", "rb") as f_nguon:
    # Mở tệp đích để ghi nhị phân
    with open("dich.bin", "wb") as f_dich:
        while True:
            du_lieu = f_nguon.read(1024)  # đọc 1024 byte
            if du_lieu == b"":            # nếu hết dữ liệu thì dừng
                break
            f_dich.write(du_lieu)         # ghi vào tệp đích

print("Sao chép hoàn tất!")
