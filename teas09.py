# สร้างโปรแกรมคำนวณเงินเดือนสุทธิที่ต้องจ่ายหลังจากหักภาษีแล้ว 7% ของเงินเดือน  และหักค่าประกันสังคม 3% ของเงินเดือน
# โดยรับค่ารหัสพนักงาน ชื่อพนักงาน เงินเดือน ทางแป้นพิมพ์ และแสดงผลข้อมูลที่รับมา
# พร้อมกับรายละเอียดว่าต้องเสียภาษีกี่บาท หักค่าประกันสังคมกี่บาท และต้องจ่ายเงินเดือนสุทธิกี
print('โปรแกรมคำนวนเงินเดือน')
print('**********')
emp_id = input("ป้อนรหัสพนักงาน : ")
emp_name = input("ป้อนชื่อพนักงาน : ")
emp_salary = input("ป้อนเงินเดือน : ")
print('**********')
tex = float(emp_salary) * 7 / 100 
insurance = float(emp_salary) * 3 /100
emp_salary_net= float(emp_salary) - tex- insurance
print(f'รหัสพนักงาน : {emp_id} ชื่อพนักงาน {emp_name} เงินเดือน: {emp_salary }')
print(f'ต้องเสียภาษี {tex} บาท')
print(f'ต้องหักค่าประกันสังคม {insurance} บาท')
print(f'ต้องจ่ายเงินเดือนสุทธิ {emp_salary_net} บาท')
#ใช้ , 
print("รหัสพนักงาน"),(emp_id),'ชื่อพนักงาน',(emp_name),'เงินเดือน',(emp_salary)
print("ต้องเสียภาษี",(tex),"บาท")
print("ต้องหักค่าประกันสังคม",(insurance),"บาท")
print("ต้องจ่ายเงินเดือนสุทธิ",(emp_salary_net),"บาท")
#ใช้ + 
print('รหัสพนักงาน'+str(emp_id)+' ชื่อพนักงาน '+str(emp_name)+' เงินเดือน: '+str(emp_salary))
print('ต้องเสียภาษี'+str(tex)+' บาท')
print('ต้องหักค่าประกันสังคม'+str(insurance)+' บาท') #insurance+ 'บาท')
print('ต้องจ่ายเงินเดือนสุทธิ'+str(emp_salary_net)+' บาท') #emp_salary_net+' บาท')
#ใช้ format 
print('รหัสพนักงาน {} ชื่อพนักงาน {} เงินเดือน {}'.format(emp_id,emp_name,emp_salary))
print('ต้องเสียภาษี {} บาท'.format(tex))
print('ต้องหักค่าประกันสังคม {} บาท'.format(insurance))
print('ต้องจ่ายเงินเดือนสุทธิ {} บาท'.format(emp_salary_net))