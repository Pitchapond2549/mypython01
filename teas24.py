#break,continue
# break in loop ทำงานเมื่อใด จบ ลูปทันที่ 
# continue in loop ทำงานเมื่อใด จบลูปทันที่ ข้ามไปทำงานรอบถัดไปทันที

for aa in range(5):
    if aa == 2:
        break
    print(aa,'hello')
print('................................')
for aa in range(5):
    if aa == 2:
        continue 
    print(aa,'hello')