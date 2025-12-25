A = set(map(int, input("Nhập set A: ").split()))
B = set(map(int, input("Nhập set B: ").split()))

A_tru_B = set()
B_tru_A = set()
A_giao_B = set()

for x in A:
    if x not in B:
        A_tru_B.add(x)

for x in B:
    if x not in A:
        B_tru_A.add(x)

for x in A:
    if x in B:
        A_giao_B.add(x)

print("A - B:", A_tru_B)
print("B - A:", B_tru_A)
print("A giao B:", A_giao_B)
