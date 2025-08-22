# สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
# และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา
# เป็นเท่าใด แล้วแสดงผลทางหน้าจอ
# สูตร  
# ผลรวม = เลขตัวที่1 + เลขตัวที่2 + เลขตัวที่3 + เลขตัวที่4 + เลขตัวที่5
# ค่าเฉลี่ย = ผลรวมของเลข 5 จำนวน / 5
 
# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================

print('สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้')
print('และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา')
print('เป็นเท่าใด แล้วแสดงผลทางหน้าจอ')
print('สูตร  ')
num1 = input("ป้อนเลขตัวที่1 : ")
num2 = input("ป้อนเลขตัวที่2 : ")
num3 = input("ป้อนเลขตัวที่3 : ")
num4 = input("ป้อนเลขตัวที่4 : ")
num5 = input("ป้อนเลขตัวที่5 : ")   
sum = float(num1) + float(num2) + float(num3) + float(num4) + float(num5)
avg = sum / 5
print(f'ผลรวมของเลข 5 จำนวนค่าคือ {sum}')
print(f'ค่าเฉลี่ยของข้อมูลที่รับเข้ามาค่าคือ {avg}')                  
