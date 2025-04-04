# [لينكس] Bash sort الاستخدام: ترتيب البيانات في الملفات

## Overview
أمر `sort` في Bash يُستخدم لترتيب خطوط النص في الملفات أو المخرجات. يمكن أن يتم الترتيب بناءً على معايير مختلفة مثل الترتيب الأبجدي أو الرقمي.

## Usage
الصيغة الأساسية للأمر هي:
```bash
sort [options] [arguments]
```

## Common Options
- `-r`: ترتيب عكسي.
- `-n`: ترتيب رقمي بدلاً من أبجدي.
- `-k`: تحديد العمود الذي سيتم الترتيب بناءً عليه.
- `-u`: إظهار القيم الفريدة فقط.

## Common Examples
- **ترتيب ملف نصي أبجدي:**
  ```bash
  sort filename.txt
  ```

- **ترتيب ملف نصي عكسي:**
  ```bash
  sort -r filename.txt
  ```

- **ترتيب أرقام في ملف:**
  ```bash
  sort -n numbers.txt
  ```

- **ترتيب بناءً على عمود معين:**
  ```bash
  sort -k 2 filename.txt
  ```

- **إظهار القيم الفريدة فقط:**
  ```bash
  sort -u filename.txt
  ```

## Tips
- تأكد من استخدام الخيار `-n` عند التعامل مع الأرقام لضمان الترتيب الصحيح.
- يمكنك دمج `sort` مع أوامر أخرى مثل `uniq` لإزالة التكرارات بعد الترتيب.
- استخدم `-o` لتوجيه النتيجة إلى ملف جديد أو نفس الملف:
  ```bash
  sort filename.txt -o sorted.txt
  ```