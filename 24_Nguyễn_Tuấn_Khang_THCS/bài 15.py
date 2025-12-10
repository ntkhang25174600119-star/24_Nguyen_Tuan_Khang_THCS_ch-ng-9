def nhap_vao_mot_so(n):
    if n < 2: 
        return False
    for i in range(2, n):
        if n % i == 0: 
            return False 
    return True 
# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra n có phải số nguyên tố không
if nhap_vao_mot_so(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")