n = int(input("Nhập số phần tử: "))
a = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(x)

tong_chan = 0
tong_le = 0

for x in a:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x

print("Tổng số chẵn:", tong_chan)
print("Tổng số lẻ:", tong_le)
