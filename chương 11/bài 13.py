# Nhập cấp của ma trận (số hàng = số cột)
n = int(input("Nhập cấp ma trận: "))

# Khởi tạo danh sách rỗng để chứa ma trận
a = []

# Nhập từng phần tử của ma trận
for i in range(n):              # Duyệt qua từng hàng
    row = []                    # Tạo một hàng mới
    for j in range(n):          # Duyệt qua từng cột
        # Nhập giá trị phần tử tại vị trí hàng i, cột j
        row.append(int(input(f"a[{i}][{j}] = ")))
    a.append(row)               # Thêm hàng vào ma trận

# Giả sử ban đầu ma trận là ma trận đơn vị
la_don_vi = True

# Kiểm tra từng phần tử của ma trận
for i in range(n):              # Duyệt hàng
    for j in range(n):          # Duyệt cột
        # Nếu là phần tử trên đường chéo chính mà khác 1 → không phải ma trận đơn vị
        if i == j and a[i][j] != 1:
            la_don_vi = False
        # Nếu không nằm trên đường chéo chính mà khác 0 → không phải ma trận đơn vị
        if i != j and a[i][j] != 0:
            la_don_vi = False

if la_don_vi:
    print("Ma trận đơn vị")
else:
    print("Không phải ma trận đơn vị")
