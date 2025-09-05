#for รู้จำนวนครั้งใช้ for
# for var_name in range(n): 
#    คำสั่ง
# for var_name in range(n, m): 
#    คำสั่ง
# for var_name in range(n, m, k): 
#    คำสั่ง

# for var_name in string:
#    คำสั่ง(s)

for aa in range(5):
    print(aa+1,'hello')
for aa in range(3,7):   #7คือรอบ เริ่มที่ 0 / 3คือเริ่มที่เลขกำกับเท่าไร 
    print('hello')
for aa in range(3,7,2): #ตัวที่ 7 คือจำนวนรอบ / 3 คือเริ่มที่เลขกำกับเท่าไร / 2 คือเพิ่มขึ้นที่ 2 แต่ละรอบ 
    print(aa,'hello')
for aa in 'iot-sau':    #string ดูที่จำนวนตัวอักษร 
    print(aa,'--hallo')

