##โปรแกรมตรวจสอบรถว่าผ่านเกณฑ์ของการตรวจสอบค่าคาร์บอนไดซ์ออกไซน์หรือ
#โดยหากค่าคาร์บอนไดซ์ออกไซน์มีค่าเกินกว่า 678.55 ให้แสดงข้อความว่า “ไม่ผ่าน”  
# หากน้อยกว่า 678.55 ให้แสดงข้อความ “ผ่าน” โดยให้รับชื่อเจ้าของ ทะเบียนรถ 
# และปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ที่วัดได้ ทางแป้นพิมพ์
#input ชื่อเจ้าของรถ
#input หมายเลขรถ
#input ปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ 
#ตรวจสอบก๊าซ  
# แสดงผล 
#แสดงชื่อโปรแกรม
def show_program_name():
 print('ตรวจสอบรถว่าผ่านเกณฑ์ของการตรวจสอบค่าคาร์บอนไดซ์ออกไซน์หรือไม่')

def input_data():
    car_owner = input('ป้อนชื่อเจ้าของรถ : ')
    car_number = input('ป้อนหมายเลขรถ : ')
    car_carbon = float(input('ป้อนปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ : '))
    return car_owner,car_number,car_carbon 

def show_result(car_owner,car_number,car_carbon,result):
    print(f'ทะเบียนรถ {car_number} ของคุณ{car_owner} ไม่ผ่านเกณฑ์ของการตรวจสอบ')
    print(f'ก๊าซที่วัดได้{car_carbon}สรุป {result}')

def check_gas(car_owner,car_number,car_carbon):
    if car_carbon > 678.55: #แสดงว่าผ่าน หลังเอล ไม่ผผ่าน 
        show_result (car_owner,car_number,car_carbon,'ไม่ผ่าน')
    else : 
        show_result(car_owner,car_number,car_carbon,'ผ่าน')

def show_pa():
    print('-----------------------------')

show_pa() 
show_program_name()
show_pa() 
car_owner,car_number,car_carbon = input_data()
show_pa()
check_gas(car_owner,car_number,car_carbon)
show_pa()