# [Linux] Bash usermod การใช้งาน: ใช้เพื่อปรับแต่งผู้ใช้ในระบบ

## Overview
คำสั่ง `usermod` ใช้ในการปรับแต่งข้อมูลของผู้ใช้ในระบบ Linux เช่น การเปลี่ยนชื่อผู้ใช้ การเพิ่มกลุ่ม หรือการปรับสิทธิ์ต่างๆ ของผู้ใช้

## Usage
รูปแบบพื้นฐานของคำสั่ง `usermod` คือ:

```bash
usermod [options] [arguments]
```

## Common Options
- `-l, --login NEW_LOGIN` : เปลี่ยนชื่อผู้ใช้
- `-d, --home NEW_HOME` : เปลี่ยนไดเรกทอรีบ้านของผู้ใช้
- `-m, --move-home` : ย้ายไดเรกทอรีบ้านไปยังตำแหน่งใหม่
- `-G, --groups GROUP1,GROUP2,...` : เพิ่มผู้ใช้ไปยังกลุ่มที่ระบุ
- `-a, --append` : เพิ่มผู้ใช้ไปยังกลุ่มโดยไม่ลบกลุ่มอื่น

## Common Examples
- เปลี่ยนชื่อผู้ใช้จาก `olduser` เป็น `newuser`:
    ```bash
    usermod -l newuser olduser
    ```

- เปลี่ยนไดเรกทอรีบ้านของผู้ใช้ `username` เป็น `/new/home/directory`:
    ```bash
    usermod -d /new/home/directory username
    ```

- เพิ่มผู้ใช้ `username` ไปยังกลุ่ม `sudo`:
    ```bash
    usermod -aG sudo username
    ```

- ย้ายไดเรกทอรีบ้านของผู้ใช้ `username` ไปยังตำแหน่งใหม่:
    ```bash
    usermod -d /new/home/directory -m username
    ```

## Tips
- ตรวจสอบให้แน่ใจว่าคุณมีสิทธิ์ในการใช้คำสั่ง `usermod` โดยปกติแล้วจะต้องใช้สิทธิ์ของผู้ดูแลระบบ (root)
- ใช้คำสั่ง `id username` เพื่อตรวจสอบกลุ่มและสิทธิ์ของผู้ใช้ก่อนทำการปรับแต่ง
- ควรทำการสำรองข้อมูลก่อนที่จะทำการเปลี่ยนแปลงที่สำคัญกับผู้ใช้หรือกลุ่มในระบบ