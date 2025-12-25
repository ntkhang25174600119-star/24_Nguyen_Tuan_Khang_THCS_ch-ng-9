n = int(input("Nhập số phần tử: "))
a = []

for i in range(n):
    a.append(int(input()))

# Bước 1: Tìm max1 (số lớn nhất)
max1 = a[0]
for x in a:
    if x > max1:
        max1 = x

# Bước 2: Tìm max2 (số lớn thứ hai)
max2 = None
for x in a:
    if x != max1:  # chỉ xét số nhỏ hơn max1
        if (max2 is None) or (x > max2):
            max2 = x

print("Số lớn thứ hai:", max2)
