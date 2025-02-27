# [لينكس] Bash umask الاستخدام: التحكم في أذونات الملفات الجديدة

## Overview
يستخدم أمر `umask` لتحديد الأذونات الافتراضية للملفات والمجلدات الجديدة التي يتم إنشاؤها في نظام لينكس. يقوم بتعيين قيمة "قناع" تحدد الأذونات التي سيتم إلغاؤها عند إنشاء ملف أو مجلد جديد.

## Usage
تكون الصيغة الأساسية لأمر `umask` كما يلي:

```bash
umask [options] [arguments]
```

## Common Options
- `-S`: يعرض الأذونات بشكل رمزي.
- `-p`: يعرض قيمة umask الحالية بشكل مفصل.

## Common Examples
- **عرض قيمة umask الحالية:**
  ```bash
  umask
  ```

- **تعيين قيمة umask جديدة:**
  ```bash
  umask 027
  ```

- **عرض قيمة umask بشكل رمزي:**
  ```bash
  umask -S
  ```

- **تعيين umask لتكون 002:**
  ```bash
  umask 002
  ```

## Tips
- تأكد من فهم الأذونات الثلاثة (قراءة، كتابة، تنفيذ) وكيف تؤثر قيمة umask على الملفات الجديدة.
- استخدم `umask` في ملفات التهيئة مثل `.bashrc` لضبط الأذونات الافتراضية عند بدء الجلسة.
- تذكر أن قيمة umask تحدد الأذونات التي سيتم إلغاؤها، لذا فإن القيم المنخفضة تعني أذونات أكثر مرونة.