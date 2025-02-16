# [Linux] Bash declare การประกาศตัวแปร: ใช้สำหรับการประกาศและกำหนดค่าตัวแปรใน Bash

## Overview
คำสั่ง `declare` ใน Bash ใช้สำหรับการประกาศตัวแปรและกำหนดคุณสมบัติต่าง ๆ ให้กับตัวแปรเหล่านั้น เช่น การกำหนดประเภทของตัวแปรหรือการกำหนดค่าคงที่

## Usage
รูปแบบพื้นฐานของคำสั่ง `declare` คือ:

```bash
declare [options] [arguments]
```

## Common Options
- `-a`: ประกาศตัวแปรเป็นอาร์เรย์
- `-i`: ประกาศตัวแปรเป็นจำนวนเต็ม
- `-r`: ทำให้ตัวแปรเป็นค่าคงที่ (ไม่สามารถเปลี่ยนแปลงได้)
- `-x`: ทำให้ตัวแปรเป็นตัวแปรสภาพแวดล้อม (environment variable)

## Common Examples
### ประกาศตัวแปรธรรมดา
```bash
declare myVar="Hello, World!"
echo $myVar
```

### ประกาศตัวแปรเป็นอาร์เรย์
```bash
declare -a myArray=("apple" "banana" "cherry")
echo ${myArray[1]}  # แสดงผล: banana
```

### ประกาศตัวแปรเป็นจำนวนเต็ม
```bash
declare -i myInt=5
myInt+=10
echo $myInt  # แสดงผล: 15
```

### ประกาศตัวแปรเป็นค่าคงที่
```bash
declare -r myConst="This is a constant"
echo $myConst
# myConst="New Value"  # จะเกิดข้อผิดพลาด
```

### ประกาศตัวแปรเป็นตัวแปรสภาพแวดล้อม
```bash
declare -x myEnvVar="Some value"
echo $myEnvVar
```

## Tips
- ใช้ `declare` เพื่อทำให้โค้ดของคุณชัดเจนและเข้าใจง่ายขึ้น โดยการระบุประเภทของตัวแปร
- เมื่อใช้ตัวแปรอาร์เรย์ ควรใช้ `declare -a` เพื่อหลีกเลี่ยงความสับสน
- สำหรับการทำงานกับค่าคงที่ ควรใช้ `declare -r` เพื่อป้องกันการเปลี่ยนแปลงค่าของตัวแปร