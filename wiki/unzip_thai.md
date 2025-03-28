# [Linux] Bash unzip การใช้งาน: ใช้สำหรับแตกไฟล์ ZIP

## Overview
คำสั่ง `unzip` ใช้สำหรับแตกไฟล์ ZIP ซึ่งเป็นรูปแบบไฟล์ที่นิยมใช้ในการบีบอัดข้อมูล โดยคำสั่งนี้ช่วยให้ผู้ใช้สามารถเข้าถึงไฟล์ภายใน ZIP ได้อย่างง่ายดาย

## Usage
รูปแบบพื้นฐานของคำสั่ง `unzip` คือ:

```bash
unzip [options] [arguments]
```

## Common Options
- `-l` : แสดงรายการไฟล์ภายใน ZIP โดยไม่แตกไฟล์
- `-d <directory>` : ระบุไดเรกทอรีที่ต้องการให้แตกไฟล์ไป
- `-o` : แตกไฟล์โดยไม่ต้องถามยืนยันหากไฟล์มีอยู่แล้ว
- `-q` : ทำงานแบบเงียบ ไม่แสดงข้อความระหว่างการแตกไฟล์

## Common Examples
- แตกไฟล์ ZIP ทั่วไป:
    ```bash
    unzip example.zip
    ```

- แสดงรายการไฟล์ภายใน ZIP:
    ```bash
    unzip -l example.zip
    ```

- แตกไฟล์ไปยังไดเรกทอรีที่กำหนด:
    ```bash
    unzip example.zip -d /path/to/directory
    ```

- แตกไฟล์โดยไม่ถามยืนยัน:
    ```bash
    unzip -o example.zip
    ```

## Tips
- ตรวจสอบให้แน่ใจว่าคุณมีสิทธิ์ในการเขียนในไดเรกทอรีที่คุณต้องการแตกไฟล์ไป
- ใช้ตัวเลือก `-q` เพื่อให้การแตกไฟล์เป็นไปอย่างเงียบ ๆ โดยไม่แสดงข้อความที่ไม่จำเป็น
- หากคุณต้องการแตกไฟล์ ZIP ที่มีรหัสผ่าน ให้ใช้คำสั่ง `unzip -P <password> example.zip`