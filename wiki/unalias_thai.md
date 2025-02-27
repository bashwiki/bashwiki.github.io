# [Linux] Bash unalias การใช้งาน: ลบการตั้งชื่อซ้ำ

## Overview
คำสั่ง `unalias` ใช้ในการลบการตั้งชื่อซ้ำที่ถูกสร้างขึ้นโดยคำสั่ง `alias` ใน Bash ซึ่งช่วยให้ผู้ใช้สามารถคืนค่าคำสั่งดั้งเดิมที่ถูกเปลี่ยนแปลงโดยการตั้งชื่อซ้ำได้

## Usage
คำสั่ง `unalias` มีรูปแบบพื้นฐานดังนี้:

```
unalias [options] [arguments]
```

## Common Options
- `-a`: ลบการตั้งชื่อซ้ำทั้งหมด
- `-p`: แสดงรายการการตั้งชื่อซ้ำที่มีอยู่ในปัจจุบัน

## Common Examples

### ลบการตั้งชื่อซ้ำเฉพาะคำสั่ง
```bash
unalias ll
```
คำสั่งนี้จะลบการตั้งชื่อซ้ำสำหรับคำสั่ง `ll` ที่อาจถูกตั้งค่าให้แสดงผลในรูปแบบที่แตกต่างจากคำสั่ง `ls -l`

### ลบการตั้งชื่อซ้ำทั้งหมด
```bash
unalias -a
```
คำสั่งนี้จะลบการตั้งชื่อซ้ำทั้งหมดที่มีอยู่ในเซสชันปัจจุบัน

### แสดงรายการการตั้งชื่อซ้ำ
```bash
unalias -p
```
คำสั่งนี้จะแสดงรายการการตั้งชื่อซ้ำที่มีอยู่ในปัจจุบัน

## Tips
- ใช้ `unalias` เมื่อคุณต้องการคืนค่าคำสั่งดั้งเดิมที่ถูกตั้งชื่อซ้ำเพื่อหลีกเลี่ยงความสับสน
- ตรวจสอบการตั้งชื่อซ้ำที่มีอยู่ก่อนที่จะลบ โดยใช้คำสั่ง `alias` เพื่อดูว่ามีการตั้งชื่อซ้ำใดบ้าง
- คำสั่ง `unalias` จะมีผลเฉพาะในเซสชันปัจจุบัน หากคุณต้องการให้การเปลี่ยนแปลงมีผลถาวร คุณจะต้องลบการตั้งชื่อซ้ำในไฟล์การตั้งค่าของ Bash เช่น `.bashrc`