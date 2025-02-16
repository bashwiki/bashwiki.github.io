# [Linux] Bash scp การใช้งาน: คัดลอกไฟล์ระหว่างโฮสต์

## Overview
คำสั่ง `scp` (Secure Copy Protocol) ใช้สำหรับการคัดลอกไฟล์หรือไดเรกทอรีระหว่างโฮสต์ในเครือข่ายที่มีการเข้ารหัสข้อมูล โดยใช้ SSH (Secure Shell) เพื่อความปลอดภัยในการส่งข้อมูล

## Usage
การใช้งานคำสั่ง `scp` มีรูปแบบพื้นฐานดังนี้:
```
scp [options] [source] [destination]
```

## Common Options
- `-r`: คัดลอกไดเรกทอรีและเนื้อหาทั้งหมดภายใน
- `-P port`: ระบุพอร์ตที่ใช้สำหรับการเชื่อมต่อ (หมายเหตุ: ใช้ตัวพิมพ์ใหญ่ P)
- `-i identity_file`: ใช้ไฟล์คีย์ส่วนตัวสำหรับการตรวจสอบตัวตน
- `-v`: แสดงข้อมูลการทำงานเพื่อการดีบัก

## Common Examples
1. คัดลอกไฟล์จากเครื่องท้องถิ่นไปยังเซิร์ฟเวอร์:
   ```bash
   scp /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
   ```

2. คัดลอกไฟล์จากเซิร์ฟเวอร์ไปยังเครื่องท้องถิ่น:
   ```bash
   scp user@remote_host:/path/to/remote/file.txt /path/to/local/directory/
   ```

3. คัดลอกไดเรกทอรีทั้งหมดจากเครื่องท้องถิ่นไปยังเซิร์ฟเวอร์:
   ```bash
   scp -r /path/to/local/directory user@remote_host:/path/to/remote/directory/
   ```

4. คัดลอกไฟล์โดยระบุพอร์ตที่ไม่ใช่พอร์ตเริ่มต้น:
   ```bash
   scp -P 2222 /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
   ```

## Tips
- ตรวจสอบให้แน่ใจว่าคุณมีสิทธิ์ในการเข้าถึงไฟล์และไดเรกทอรีที่คุณต้องการคัดลอก
- ใช้ตัวเลือก `-v` เพื่อดูรายละเอียดการเชื่อมต่อและการคัดลอกในกรณีที่มีปัญหา
- หากคุณใช้คีย์ SSH ควรตั้งค่าการอนุญาตไฟล์คีย์ให้เหมาะสมเพื่อความปลอดภัย