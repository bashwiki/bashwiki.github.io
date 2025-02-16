# [لينكس] Bash lsof استخدام: عرض الملفات المفتوحة

## Overview
أداة `lsof` (التي تعني "list open files") تُستخدم في أنظمة التشغيل لعرض جميع الملفات المفتوحة والعمليات المرتبطة بها. تعتبر هذه الأداة مفيدة جدًا لتشخيص المشكلات المتعلقة بالملفات والعمليات.

## Usage
الصيغة الأساسية لاستخدام الأمر `lsof` هي:

```bash
lsof [options] [arguments]
```

## Common Options
- `-a`: يستخدم لتحديد جميع الخيارات المحددة.
- `-c <command>`: يعرض الملفات المفتوحة بواسطة عملية معينة.
- `-u <user>`: يعرض الملفات المفتوحة من قبل مستخدم معين.
- `-p <pid>`: يعرض الملفات المفتوحة بواسطة عملية ذات معرف محدد.
- `-i`: يعرض الملفات المفتوحة التي تتعلق بالشبكة.

## Common Examples
- لعرض جميع الملفات المفتوحة في النظام:
  ```bash
  lsof
  ```

- لعرض الملفات المفتوحة بواسطة مستخدم معين:
  ```bash
  lsof -u username
  ```

- لعرض الملفات المفتوحة بواسطة عملية معينة:
  ```bash
  lsof -c process_name
  ```

- لعرض الملفات المفتوحة بواسطة معرف عملية محدد:
  ```bash
  lsof -p 1234
  ```

- لعرض جميع الاتصالات الشبكية المفتوحة:
  ```bash
  lsof -i
  ```

## Tips
- استخدم الأمر مع `grep` لتصفية النتائج، مثل:
  ```bash
  lsof | grep filename
  ```
- تأكد من تشغيل الأمر كمدير (root) للحصول على معلومات أكثر دقة حول جميع العمليات.
- يمكنك استخدام الخيار `-n` لتجنب تحويل عناوين IP إلى أسماء مضيفين، مما قد يسهل القراءة.