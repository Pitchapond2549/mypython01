# 4 ฟังก์ชั่น 
#สร้างโปรแกรมคำนวณอายุของจากปีเกิด (พ.ศ.) ของพนักงานโรงงานแห่งหนึ่ง 
#โดยป้อนชื่อและปีเกิดทางแป้นพิมพ์ ทั้งนี้โปรแกรมจะหยุดทำงานก็ต่อเมมื่อป้อนชื่อพนักงาน เป็น SAU ก็จะหยุดทำงาน 
# input ชื่อพนักงาน
# input ปีเกิด
#input รหหัสพนักงาน 
#แสดงชื่อโปรแกรม 

def show_program_name():
    print('โปรแกรมคำนวณอายุพนักงานโรงงาน')


def input_data():
    emp_name = input('ป้อนชื่อพนักงาน : ')
    if emp_name.upper() == 'SAU':
        return emp_name,0
    emp_year = int(input('ป้อนปีเกิด(พ.ศ.): '))
    return emp_name,emp_year
def calculate_age(emp_year):
    return (datetime.now().year+543) - emp_year
  
def show_result(emp_name,emp_year,result):
    print(f'คุณ {emp_name} เกิดปี {emp_year} อายุ {result} ปี')
    
def check_sau(emp_name,emp_year,):
    if emp_name.upper() == 'SAU':
        show_result(emp_name,emp_year,'stop')
    else:
        show_result(emp_name,emp_year,'continue')
        
def show_pa():
    print('-----------------------------')
show_pa
show_program_name()
show_pa
emp_name,emp_year = input_data()
show_pa
check_sau(emp_name,emp_year)
show_pa       
