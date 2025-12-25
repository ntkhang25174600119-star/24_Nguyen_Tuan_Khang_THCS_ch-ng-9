m = int(input("nhập só hàng A: "))
n = int(input("nhập số cột A: "))                              # n là số cột của A (cũng là số hàng của B)
p = int (input("nhập số cột B: "))

# tạo ma trận rỗng 
A = []
B = []

print("nhập ma trận A: ")
for i in range(m):                                             # duyệt từng hàng của A                                  
    row = []                                                   # tạo row để chứa 1 hàng của A  
    for j in range(n):                                         # duyệt từng cột trong hàng 
        row.append(int(input(f"A[{i}][{j}] = ")))              # nhập số nguyên và thêm vào hàng
    A.append(row)                                              # thêm hàng row vào mt A 

print("nhập ma trận B: ")
for i in range(m):                                             
    row = []
    for j in range(p):   
        row.append(int(input(f"B[{i}][{j}] = ")))
    B.append(row)
        
C = []
for i in range(m):                                            # duyệt từng hàng của A (hàng của C)
    row = []
    for j in range(p):                                        # duyệt từng cột của B (cột của C) 
        s = 0                                                 # khởi tạo tổng tạm s = 0 cho phần tử C[i][j]
        for k in range(n):                                    # chạy qua từng phần tử hàng i của A và cột j của B
            s += A[i][k] * B[k][j]                            # cộng tích A[i][k] * B[k][j] vào s 
        row.append(s)                                         # sau vòng k, thêm s vào hàng C
    C.append(row)
print("ma trận tích C: ")
for row in C:                                                 # duyệt từng hàng của C
    print(row)                                          
        
             
        
    