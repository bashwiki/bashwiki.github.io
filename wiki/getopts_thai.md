# [Linux] Bash getopts การใช้งาน: ใช้สำหรับการจัดการอาร์กิวเมนต์ในสคริปต์

## Overview
คำสั่ง `getopts` ใช้สำหรับการจัดการและวิเคราะห์อาร์กิวเมนต์ที่ส่งเข้ามาในสคริปต์ Bash โดยช่วยให้สามารถกำหนดตัวเลือกและอาร์กิวเมนต์ได้อย่างมีประสิทธิภาพ

## Usage
รูปแบบพื้นฐานของคำสั่ง `getopts` คือ:

```bash
getopts [options] [arguments]
```

## Common Options
- `-a` : ใช้สำหรับการกำหนดตัวเลือกที่ต้องการ
- `-b` : ใช้สำหรับการกำหนดอาร์กิวเมนต์ที่เกี่ยวข้อง
- `-c` : ใช้สำหรับการแสดงผลข้อมูลที่ได้รับ

## Common Examples

### ตัวอย่างที่ 1: การใช้ getopts เพื่อจัดการตัวเลือก
```bash
#!/bin/bash

while getopts "ab:c:" option; do
  case $option in
    a) echo "Option A selected";;
    b) echo "Option B selected with argument: $OPTARG";;
    c) echo "Option C selected with argument: $OPTARG";;
    *) echo "Invalid option";;
  esac
done
```

### ตัวอย่างที่ 2: การใช้ getopts กับอาร์กิวเมนต์
```bash
#!/bin/bash

while getopts "u:p:" option; do
  case $option in
    u) echo "Username: $OPTARG";;
    p) echo "Password: $OPTARG";;
    *) echo "Usage: script.sh -u username -p password";;
  esac
done
```

### ตัวอย่างที่ 3: การใช้ getopts ในการตรวจสอบตัวเลือก
```bash
#!/bin/bash

while getopts "x:y:z:" option; do
  case $option in
    x) echo "Option X with value: $OPTARG";;
    y) echo "Option Y with value: $OPTARG";;
    z) echo "Option Z with value: $OPTARG";;
    *) echo "Invalid option";;
  esac
done
```

## Tips
- ควรใช้ `OPTIND` เพื่อรีเซ็ตตำแหน่งของอาร์กิวเมนต์หลังจากการใช้ `getopts`
- ใช้ `:` หลังตัวเลือกที่ต้องการอาร์กิวเมนต์เพื่อระบุว่าต้องการอาร์กิวเมนต์
- ตรวจสอบค่าของ `$OPTARG` เพื่อเข้าถึงอาร์กิวเมนต์ที่เกี่ยวข้องกับตัวเลือกที่เลือก

การใช้ `getopts` จะช่วยให้การจัดการอาร์กิวเมนต์ในสคริปต์ Bash ของคุณมีความชัดเจนและมีประสิทธิภาพมากขึ้น