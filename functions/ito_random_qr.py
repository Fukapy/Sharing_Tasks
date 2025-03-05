## 【20241214 気象予報士学生会ito】
# itoを始める際に、入力する部分
import random
import qrcode
import pandas as pd
def qr_main(name_list, q_no):
    for i in range(len(name_list)):
        number = random_numbers[i]
        qr = qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,)
        qr.add_data(number)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        file_path = "ito_qr/QR_"+ str(q_no) +"問目_"+name_list[i]+".png"
        img.save(file_path)

# 参加者名を入力(GitHub公開時は本名ではなくアルファベットに置き換えた。)
name_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

# お題を変えるたびに実行
# 1~100の整数からランダムに重複を許さず参加人数分だけ選ぶ
random_numbers = random.sample(range(1, 101), len(name_list))
qr_main(name_list, 0)
pd.DataFrame([name_list, random_numbers],
             index=["名前", "乱数"]).T
