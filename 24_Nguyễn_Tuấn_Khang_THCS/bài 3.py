s = input("nhập chuỗi: ")
kq = "" 
co_chu = False 
for ch in s: 
    if ch != " ":
        kq += ch
        co_chu = True
    else: 
        if co_chu:
            kq += " "
            co_chu = False 
if len(kq) > 0 and kq[-1] == " ":
    kq = kq[:1]
print(kq)