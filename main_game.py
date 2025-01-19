# pip install pandas openpyxl

import pandas as pd
import hashlib

# อ่านข้อมูลจากไฟล์ Excel
def load_game_data(filename):
    df = pd.read_excel(filename)
    return df['cvv'][0], df['hints'].tolist()

# ฟังก์ชันเพื่อให้ผู้เล่นเดาคำ
def start_game(secret_word_hash, hints):
    attempts = 0  # จำนวนรอบที่ผิด
    max_attempts = len(hints) * 3  # จำกัดจำนวนการพยายามทั้งหมด (3 รอบ * จำนวนคำใบ้)
    guessed_correctly = False

    print("เกมเริ่มต้น! คำที่ต้องการเดาคือคำที่ถูกเข้ารหัสใน SHA-256")
    print("คุณสามารถหาใน google search ได้")

    while not guessed_correctly and attempts < max_attempts:
        # เผยคำใบ้ทุกๆ 3 รอบที่ผิด
        if attempts % 3 == 0 and attempts > 0:  # เผยคำใบ้หลังจากที่ผิดครบ 3 รอบ
            print(f"คำใบ้ {attempts // 3}: {hints[(attempts // 3) - 1]}")
            print("คุณสามารถหาใน google search ได้")

        user_input = input(f"เดาคำที่ถูกเข้ารหัส (รอบที่ {attempts + 1}): ")

        # ตรวจสอบว่าผู้เล่นเดาถูก
        if generate_hash(user_input) == secret_word_hash:
            guessed_correctly = True
            print("ยินดีด้วย! คุณเดาคำถูกต้อง!")
        else:
            print("คำที่คุณเดาผิด กรุณาลองใหม่อีกครั้ง")
            attempts += 1

    if not guessed_correctly:
        print("เกมจบลง! คุณไม่สามารถเดาคำได้ถูกต้องในจำนวนรอบที่จำกัด")

# ฟังก์ชันสร้าง hash
def generate_hash(word):
    return hashlib.sha256(word.encode()).hexdigest()

# เริ่มเกม
cvv, hints = load_game_data('cvv_data_with_hints.xlsx')  # อ่านไฟล์ Excel
start_game(cvv, hints)
