m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
a = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"a[{i}][{j}] = ")))
    a.append(row)

max_sum = None
index = 0

for i in range(m):
    s = 0
    for j in range(n):
        s += a[i][j]

    if max_sum is None or s > max_sum:
        max_sum = s
        index = i

print("Hàng có tổng lớn nhất là hàng:", index)
print("Tổng lớn nhất:", max_sum)
