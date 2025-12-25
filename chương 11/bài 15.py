t = tuple(map(int, input("Nhập tuple: ").split()))

chan = []
le = []

tong_chan = 0
tong_le = 0

for x in t:
    if x % 2 == 0:
        chan.append(x)
        tong_chan += x
    else:
        le.append(x)
        tong_le += x

tuple_chan = tuple(chan)
tuple_le = tuple(le)

print("Tuple chẵn:", tuple_chan)
print("Tổng chẵn:", tong_chan)
print("Tuple lẻ:", tuple_le)
print("Tổng lẻ:", tong_le)
