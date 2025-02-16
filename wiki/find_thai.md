# [Linux] Bash find การใช้งาน: ค้นหาชื่อไฟล์

## Overview
คำสั่ง `find` ใช้สำหรับค้นหาไฟล์และไดเรกทอรีในระบบไฟล์ตามเงื่อนไขที่กำหนด เช่น ชื่อไฟล์ ขนาด หรือวันที่แก้ไขล่าสุด

## Usage
รูปแบบพื้นฐานของคำสั่ง `find` คือ:

```
find [options] [arguments]
```

## Common Options
- `-name <pattern>`: ค้นหาไฟล์ที่มีชื่อตรงตามรูปแบบที่กำหนด
- `-type <type>`: กำหนดประเภทของไฟล์ที่ต้องการค้นหา เช่น `f` สำหรับไฟล์ปกติ, `d` สำหรับไดเรกทอรี
- `-size <n>`: ค้นหาไฟล์ที่มีขนาดตามที่กำหนด
- `-mtime <n>`: ค้นหาไฟล์ที่ถูกแก้ไขเมื่อ `n` วันที่ผ่านมา
- `-exec <command> {} \;`: รันคำสั่งกับไฟล์ที่ค้นพบ

## Common Examples
- ค้นหาไฟล์ที่มีนามสกุล `.txt` ในไดเรกทอรีปัจจุบัน:
  ```bash
  find . -name "*.txt"
  ```

- ค้นหาไฟล์ที่มีขนาดมากกว่า 1MB:
  ```bash
  find /path/to/search -size +1M
  ```

- ค้นหาไฟล์ที่ถูกแก้ไขใน 7 วันที่ผ่านมา:
  ```bash
  find /path/to/search -mtime -7
  ```

- ค้นหาและลบไฟล์ที่มีนามสกุล `.tmp`:
  ```bash
  find /path/to/search -name "*.tmp" -exec rm {} \;
  ```

## Tips
- ใช้ `-type f` หรือ `-type d` เพื่อจำกัดการค้นหาเฉพาะไฟล์หรือไดเรกทอรี
- ใช้ `-print` เพื่อแสดงผลลัพธ์ที่ค้นพบ (โดยปกติจะทำโดยอัตโนมัติ)
- ทดสอบคำสั่งด้วย `-print` ก่อนที่จะใช้ `-exec` เพื่อหลีกเลี่ยงการลบไฟล์โดยไม่ตั้งใจ