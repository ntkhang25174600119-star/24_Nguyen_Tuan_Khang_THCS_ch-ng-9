with open("van_ban.txt", "r", encoding="utf-8") as f: 
    text = f.read()
noi_dung = text.split()
cac_tu = text.lower().split()                                # chuyển về chữ thường và tách các từ
tan_suat = {}                                                    # từ điển lưu tần suất số lần xuất hiện mỗi từ
for tu in cac_tu:
    if tu in tan_suat:
        tan_suat[tu] += 1                                      # nếu từ đã có tăng lên 1
    else:
        tan_suat[tu] = 1                                       # ch có thì giữ nguyên gtri 
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")