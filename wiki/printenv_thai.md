# [Linux] Bash printenv การใช้งาน: แสดงตัวแปรสภาพแวดล้อม

## Overview
คำสั่ง `printenv` ใช้เพื่อแสดงค่าของตัวแปรสภาพแวดล้อมในระบบปฏิบัติการ Unix/Linux โดยจะช่วยให้ผู้ใช้สามารถดูค่าต่าง ๆ ที่กำหนดไว้ในสภาพแวดล้อมของระบบได้

## Usage
รูปแบบพื้นฐานของคำสั่ง `printenv` คือ:

```bash
printenv [options] [arguments]
```

## Common Options
- `-0` : แสดงผลลัพธ์โดยใช้ null character เป็นตัวแบ่ง
- `NAME` : แสดงค่าของตัวแปรสภาพแวดล้อมที่ระบุชื่อ

## Common Examples
1. แสดงค่าทั้งหมดของตัวแปรสภาพแวดล้อม:
   ```bash
   printenv
   ```

2. แสดงค่าของตัวแปรสภาพแวดล้อมที่ชื่อว่า `HOME`:
   ```bash
   printenv HOME
   ```

3. แสดงค่าของตัวแปรสภาพแวดล้อมที่ชื่อว่า `PATH`:
   ```bash
   printenv PATH
   ```

4. ใช้ตัวเลือก `-0` เพื่อแสดงผลลัพธ์โดยใช้ null character เป็นตัวแบ่ง:
   ```bash
   printenv -0
   ```

## Tips
- ใช้ `printenv` ร่วมกับคำสั่ง `grep` เพื่อค้นหาตัวแปรที่ต้องการได้ง่ายขึ้น เช่น:
  ```bash
  printenv | grep USER
  ```
- คำสั่งนี้เป็นเครื่องมือที่มีประโยชน์ในการตรวจสอบค่าตัวแปรสภาพแวดล้อมที่อาจมีผลต่อการทำงานของโปรแกรมต่าง ๆ
- หากต้องการตั้งค่าตัวแปรสภาพแวดล้อมใหม่ สามารถใช้คำสั่ง `export` ได้ เช่น:
  ```bash
  export MY_VAR="Hello"
  ```