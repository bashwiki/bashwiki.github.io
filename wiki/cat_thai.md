# [Linux] Bash cat การใช้งาน: แสดงเนื้อหาของไฟล์

## Overview
คำสั่ง `cat` ใน Bash ใช้สำหรับแสดงเนื้อหาของไฟล์บนหน้าจอหรือรวมไฟล์หลายไฟล์เข้าด้วยกัน โดยสามารถใช้เพื่อดูข้อมูลหรือสร้างไฟล์ใหม่ได้

## Usage
รูปแบบพื้นฐานของคำสั่ง `cat` คือ:

```bash
cat [options] [arguments]
```

## Common Options
- `-n`: แสดงหมายเลขบรรทัดในผลลัพธ์
- `-E`: แสดงเครื่องหมาย `$` ที่ท้ายบรรทัด
- `-b`: แสดงหมายเลขบรรทัดเฉพาะบรรทัดที่ไม่ว่าง
- `-s`: ลดบรรทัดว่างที่ต่อเนื่องกันให้เหลือเพียงหนึ่งบรรทัด

## Common Examples
1. แสดงเนื้อหาของไฟล์:
   ```bash
   cat filename.txt
   ```

2. รวมไฟล์สองไฟล์เข้าด้วยกันและแสดงผล:
   ```bash
   cat file1.txt file2.txt
   ```

3. สร้างไฟล์ใหม่จากเนื้อหาของไฟล์อื่น:
   ```bash
   cat source.txt > newfile.txt
   ```

4. แสดงเนื้อหาพร้อมหมายเลขบรรทัด:
   ```bash
   cat -n filename.txt
   ```

5. แสดงเนื้อหาของไฟล์และแสดงเครื่องหมาย `$` ที่ท้ายบรรทัด:
   ```bash
   cat -E filename.txt
   ```

## Tips
- ใช้ `cat` ร่วมกับคำสั่งอื่น เช่น `grep` เพื่อค้นหาข้อมูลในไฟล์
- ระวังการใช้ `>` เพราะจะเขียนทับไฟล์ที่มีอยู่แล้ว
- ใช้ `cat` เพื่อรวมไฟล์หลายไฟล์เข้าด้วยกันในไฟล์ใหม่ได้อย่างง่ายดาย