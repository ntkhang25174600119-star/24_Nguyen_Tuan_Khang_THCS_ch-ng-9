n = int(input("Nhập cấp ma trận: "))
a = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"a[{i}][{j}] = ")))
    a.append(row)

tong = 0

for i in range(n):
    tong += a[i][n - 1 - i]

print("Tổng đường chéo phụ:", tong)
