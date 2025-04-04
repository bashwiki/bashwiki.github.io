# [Linux] Bash readonly การใช้งาน: กำหนดตัวแปรให้ไม่สามารถแก้ไขได้

## Overview
คำสั่ง `readonly` ใน Bash ใช้เพื่อกำหนดตัวแปรให้เป็นแบบอ่านอย่างเดียว ซึ่งหมายความว่าหลังจากที่คุณตั้งค่าตัวแปรเป็น readonly แล้ว คุณจะไม่สามารถเปลี่ยนแปลงค่าในตัวแปรนั้นได้อีก

## Usage
รูปแบบพื้นฐานของคำสั่ง `readonly` คือ:

```bash
readonly [options] [arguments]
```

## Common Options
- `-p`: แสดงรายการตัวแปรที่ถูกตั้งค่าเป็น readonly
- `variable_name`: ชื่อของตัวแปรที่คุณต้องการตั้งค่าเป็น readonly

## Common Examples

1. ตั้งค่าตัวแปรเป็น readonly
   ```bash
   MY_VAR="Hello"
   readonly MY_VAR
   ```

2. พยายามเปลี่ยนแปลงค่าของตัวแปร readonly
   ```bash
   MY_VAR="World"  # จะเกิดข้อผิดพลาด
   ```

3. แสดงรายการตัวแปร readonly
   ```bash
   readonly -p
   ```

4. ตั้งค่าหลายตัวแปรเป็น readonly
   ```bash
   readonly VAR1="Value1" VAR2="Value2"
   ```

## Tips
- ใช้ `readonly` เพื่อป้องกันการเปลี่ยนแปลงค่าของตัวแปรที่สำคัญในสคริปต์ของคุณ
- ตรวจสอบตัวแปร readonly โดยใช้คำสั่ง `readonly -p` เพื่อให้แน่ใจว่าตัวแปรที่คุณต้องการไม่สามารถแก้ไขได้
- ควรใช้ `readonly` กับตัวแปรที่คุณต้องการให้มีค่าคงที่ตลอดการทำงานของสคริปต์