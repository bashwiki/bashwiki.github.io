# [لينكس] Bash basename الاستخدام: [الحصول على اسم الملف من مسار]

## Overview
أمر `basename` في Bash يُستخدم لاستخراج اسم الملف من مسار كامل. هذا الأمر مفيد عند الحاجة إلى التعامل مع أسماء الملفات فقط دون الحاجة إلى المسار الكامل.

## Usage
الصيغة الأساسية للأمر هي:
```bash
basename [options] [arguments]
```

## Common Options
- `-a`: يعالج جميع المسارات المعطاة ويعيد أسماء الملفات.
- `-s`: يحدد لاحقة معينة لإزالتها من اسم الملف.
- `--help`: يعرض معلومات المساعدة حول الأمر.

## Common Examples
- **استخراج اسم ملف من مسار كامل:**
```bash
basename /home/user/file.txt
```
الإخراج سيكون:
```
file.txt
```

- **إزالة لاحقة من اسم الملف:**
```bash
basename /home/user/file.txt .txt
```
الإخراج سيكون:
```
file
```

- **معالجة عدة مسارات:**
```bash
basename -a /home/user/file1.txt /home/user/file2.txt
```
الإخراج سيكون:
```
file1.txt
file2.txt
```

## Tips
- استخدم الخيار `-s` لإزالة اللاحقات الشائعة مثل `.txt` أو `.jpg` بسهولة.
- يمكن دمج الأمر مع أوامر أخرى مثل `find` للحصول على أسماء الملفات بشكل أكثر فعالية.
- تذكر أن `basename` لا يتعامل مع المسارات النسبية بشكل مختلف عن المسارات المطلقة.