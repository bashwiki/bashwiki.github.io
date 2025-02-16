# [Linux] Bash basename การใช้งาน: ใช้เพื่อดึงชื่อไฟล์จากเส้นทาง

## Overview
คำสั่ง `basename` ใช้เพื่อดึงชื่อไฟล์จากเส้นทางที่กำหนด โดยจะตัดส่วนของเส้นทางออกและแสดงเฉพาะชื่อไฟล์เท่านั้น ซึ่งมีประโยชน์ในการจัดการไฟล์และสคริปต์ใน Bash

## Usage
รูปแบบพื้นฐานของคำสั่ง `basename` คือ:

```bash
basename [options] [arguments]
```

## Common Options
- `-a` : แสดงชื่อไฟล์ทั้งหมดจากรายการที่กำหนด
- `-s` : กำหนดส่วนที่ต้องการตัดออกจากชื่อไฟล์

## Common Examples
### ตัวอย่างที่ 1: ดึงชื่อไฟล์จากเส้นทาง
```bash
basename /home/user/document.txt
```
ผลลัพธ์:
```
document.txt
```

### ตัวอย่างที่ 2: ดึงชื่อไฟล์และตัดนามสกุล
```bash
basename /home/user/document.txt .txt
```
ผลลัพธ์:
```
document
```

### ตัวอย่างที่ 3: ดึงชื่อไฟล์จากหลายเส้นทาง
```bash
basename -a /home/user/file1.txt /home/user/file2.txt
```
ผลลัพธ์:
```
file1.txt
file2.txt
```

## Tips
- ใช้ `basename` ร่วมกับคำสั่งอื่น ๆ เช่น `find` เพื่อจัดการไฟล์ได้ง่ายขึ้น
- เมื่อใช้ตัวเลือก `-s` ควรระบุส่วนที่ต้องการตัดออกอย่างถูกต้องเพื่อหลีกเลี่ยงข้อผิดพลาด
- คำสั่ง `basename` เป็นเครื่องมือที่มีประโยชน์ในสคริปต์ Bash เพื่อทำให้การจัดการไฟล์มีประสิทธิภาพมากขึ้น