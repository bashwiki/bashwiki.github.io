# [Linux] Bash unset การใช้งาน: ลบตัวแปรจากสภาพแวดล้อม

## Overview
คำสั่ง `unset` ใน Bash ใช้สำหรับลบตัวแปรหรือฟังก์ชันออกจากสภาพแวดล้อมของเชลล์ ซึ่งหมายความว่าหลังจากที่คุณใช้คำสั่งนี้ ตัวแปรหรือฟังก์ชันนั้นจะไม่สามารถเข้าถึงได้อีกต่อไป

## Usage
รูปแบบพื้นฐานของคำสั่ง `unset` คือ:

```
unset [options] [arguments]
```

## Common Options
- `-f` : ใช้เพื่อลบฟังก์ชัน
- `-v` : ใช้เพื่อลบตัวแปร (เป็นค่าเริ่มต้น)

## Common Examples
1. **ลบตัวแปร**:
   ```bash
   my_var="Hello, World!"
   echo $my_var  # แสดงผล: Hello, World!
   unset my_var
   echo $my_var  # แสดงผล: (ไม่มีอะไรแสดง)
   ```

2. **ลบฟังก์ชัน**:
   ```bash
   my_function() {
       echo "This is a function."
   }
   my_function  # แสดงผล: This is a function.
   unset -f my_function
   my_function  # แสดงผล: bash: my_function: command not found
   ```

3. **ลบหลายตัวแปรพร้อมกัน**:
   ```bash
   var1="First"
   var2="Second"
   unset var1 var2
   echo $var1  # แสดงผล: (ไม่มีอะไรแสดง)
   echo $var2  # แสดงผล: (ไม่มีอะไรแสดง)
   ```

## Tips
- ใช้ `unset` อย่างระมัดระวัง เพราะการลบตัวแปรหรือฟังก์ชันอาจทำให้สคริปต์ของคุณทำงานผิดพลาดได้
- ตรวจสอบให้แน่ใจว่าตัวแปรหรือฟังก์ชันที่คุณต้องการลบไม่ได้ถูกใช้งานในส่วนอื่นของสคริปต์
- คุณสามารถใช้ `declare -p` เพื่อตรวจสอบว่าตัวแปรยังคงมีอยู่ก่อนที่จะใช้ `unset`