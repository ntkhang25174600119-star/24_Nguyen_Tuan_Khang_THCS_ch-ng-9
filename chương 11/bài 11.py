n = int(input("Nhập cấp ma trận: "))
a = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"a[{i}][{j}] = ")))
    a.append(row)

doi_xung = True

for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            doi_xung = False
            break

if doi_xung:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")
