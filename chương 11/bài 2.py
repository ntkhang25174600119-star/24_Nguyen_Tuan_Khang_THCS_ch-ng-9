s = input("nhập chuỗi: ")
n = int(input("nhập n: "))
tu = ""
for ch in s + " ":
    if ch != "":
        tu += ch
    else: 
        if len(tu) > n: 
            print(tu)
            tu = "" 

    
