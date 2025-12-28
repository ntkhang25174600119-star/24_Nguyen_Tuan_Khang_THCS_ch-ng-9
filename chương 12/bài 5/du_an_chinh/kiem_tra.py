import sys
import os

# Lấy đường dẫn thư mục hiện tại của file kiem_tra.py
current_dir = os.path.dirname(__file__)

# Tạo đường dẫn tới thu_vien_chung
thu_vien_chung_path = os.path.join(current_dir, "..", "thu_vien_chung")

# Thêm vào sys.path
sys.path.append(thu_vien_chung_path)

import xu_ly_so

so = 17

if xu_ly_so.kiem_tra_so_nguyen_to(so):
    print(so, "là số nguyên tố")
else:
    print(so, "không phải là số nguyên tố")

