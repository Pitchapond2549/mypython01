#คำสั่งรับข้อความ string ทางแป่้นพิมพ์ ใช้ฟังก์ชัน input
# variable ตัวแปร คือ ชื่อที่เดฟตั้งเองเอาไว้เก็บข้อมูลที่เกิดขึ้นในโปรแกรม(ต้องเป็นไปตามกฎการตั้งชื่อ)

fullname = input("ป้อนชื่อ; ")
year_born = input("ป้อนปีเกิด พ.ศ.: ")
print("-------")
print(f'สวัสดีคุณ {fullname}')
print(f'คุณเกิดในปี {year_born} ตอนนี้คุณอายุ {2568 - int(year_born)}')
# ใช้ , 
print("f'คุณ {fullname}",year_born,'ตอนนี้คุณอายุ',2568 -int(year_born)) 
# ใช้ + 
print('hallo'+str(555)+'wow'+str(999)+str(True)+'hi'+str(10 + 20 - 5)+str(152.875))
# ใช้ format 
print(' '.format('A','B','C','D','E'))
#ใช้ F+sting 
print(f'hallo (555) wow {999} {True} hi {10+20-5} {152.875}')