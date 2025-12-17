n = int(input("nhập só phần tử: "))
a = []
for i in range(n):
    a.append(int(input(f"nhập phần thử thứ {i}")))
b = int(input("nhập tổng cần tìm: "))
for i in range(n):
    for c in range(i + 1, n):
        if a[i] + a[c] == b:
            print("Cặp số:", a[i], a[c])

        
