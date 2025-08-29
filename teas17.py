#โปรแกรมคำนวณราคาสินค้าที่รับส่วนลดแล้ว โดยป้อนรหัสสินค้า ชื่อสินค้า ประเภทสินค้า 
# ซึ่งมี 4 ประเภท คือ food(F/f), woman(W/w), man(M/m), kitchen(K/k) โดยป้อนเป็นตัวย่อ 
# และราคาสินค้า และราคาสินค้าทางแป้นพิมพ์ แล้วคำนวณราคาสินค้าที่รับส่วนลดแล้วทางหน้าจอ
# โดยสินค้าประเภท food ลด 2% ของราคาสินค้า, woman ลด 4% ของราคาสินค้า, man ลด 6% ของราคาสินค้า, kitchen
#ลด 10% ของราคาสินค้า หากป้อนประเภทสินค้าผิดจากที่กำหนดให้แสดงข้อความ "คุณป้อนประเภทผิด !!!"

print('โปรแกรมคำนวณราคาสินค้าที่รับส่วนลดแล้ว')
print('หากค่าราคาสินค้าที่รับส่วนลดมีค่าเกินกว่า 2% ให้แสดงข้อความว่า “คุณป้อนประเภทผิด !!!"')

product_code = input('ป้อนรหัสสินค้า : ')
product_name = input('ป้อนชื่อสินค้า : ')
product_type = input('ป้อนประเภทสินค้า (F/f, W/w, M/m, K/k) : ')
product_price = float(input('ป้อนราคาสินค้า : '))
print('-------') 
if product_type == 'F' or product_type == 'f':
    pro_sale = product_price - (product_price * 0.02/100)
    print(f'ราคาสินค้าที่รับส่วนลดแล้วคือ {pro_sale}บาท')
elif product_type == 'W' or product_type == 'w':
    pro_sale = product_price - (product_price * 0.04/100)
    print(f'ราคาสินค้าที่รับส่วนลดแล้วคือ {pro_sale}บาท')
elif product_type == 'M' or product_type == 'm':
    pro_sale = product_price - (product_price * 0.06/100)
    print(f'ราคาสินค้าที่รับส่วนลดแล้วคือ {pro_sale}บาท')
elif product_type == 'K' or product_type == 'k':
    pro_sale = product_price - (product_price * 0.10/100)
    print(f'ราคาสินค้าที่รับส่วนลดแล้วคือ {pro_sale}บาท')
else:
    print('คุณป้อนประเภทผิด !!!ป้อนใหม่หน่อยน้าาอ้วนน')
print('ขอบคุณฮาฟฟฟฟฟฟ')