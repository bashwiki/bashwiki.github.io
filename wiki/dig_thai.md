# [Linux] Bash dig การใช้งาน: ค้นหาข้อมูล DNS

## Overview
คำสั่ง `dig` (Domain Information Groper) เป็นเครื่องมือที่ใช้ในการค้นหาข้อมูล DNS (Domain Name System) ซึ่งช่วยให้ผู้ใช้สามารถตรวจสอบและวิเคราะห์ข้อมูลเกี่ยวกับโดเมนและที่อยู่ IP ได้อย่างง่ายดาย

## Usage
รูปแบบพื้นฐานของคำสั่ง `dig` คือ:

```
dig [options] [arguments]
```

## Common Options
- `@server` : ระบุ DNS server ที่ต้องการใช้ในการค้นหา
- `-t type` : กำหนดประเภทของข้อมูลที่ต้องการค้นหา เช่น A, AAAA, MX, TXT
- `+short` : แสดงผลลัพธ์ในรูปแบบที่สั้นและเข้าใจง่าย
- `+trace` : ติดตามเส้นทางการค้นหาจาก root DNS server

## Common Examples
1. ค้นหาที่อยู่ IP ของโดเมน:
   ```bash
   dig example.com
   ```

2. ค้นหาข้อมูล MX (Mail Exchange) ของโดเมน:
   ```bash
   dig example.com -t MX
   ```

3. ใช้ DNS server ที่กำหนดในการค้นหา:
   ```bash
   dig @8.8.8.8 example.com
   ```

4. แสดงผลลัพธ์ในรูปแบบสั้น:
   ```bash
   dig example.com +short
   ```

5. ติดตามเส้นทางการค้นหา:
   ```bash
   dig example.com +trace
   ```

## Tips
- ใช้ `+short` เพื่อให้ได้ผลลัพธ์ที่รวดเร็วและเข้าใจง่าย
- หากคุณต้องการข้อมูลที่ละเอียดมากขึ้น ให้ลองใช้ตัวเลือก `+trace`
- ตรวจสอบว่า DNS server ที่คุณใช้เป็น server ที่เชื่อถือได้เพื่อให้ได้ข้อมูลที่ถูกต้อง