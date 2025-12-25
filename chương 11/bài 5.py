n = int(input("Nhập số phần tử: "))
a = []

for i in range(n):
    a.append(int(input()))

kq = []

for x in a:
    trung = False
    for y in kq:
        if x == y:
            trung = True
            break
    if not trung:
        kq.append(x)

print(kq)
