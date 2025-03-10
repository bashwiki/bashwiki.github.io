# [لينكس] Bash source الاستخدام: تنفيذ الأوامر من ملف

## Overview
أمر `source` في Bash يُستخدم لتنفيذ الأوامر الموجودة في ملف نصي داخل البيئة الحالية للشل. هذا يعني أن أي تغييرات تُجرى على المتغيرات أو الوظائف ستظل سارية بعد انتهاء تنفيذ الأوامر في الملف.

## Usage
التركيب الأساسي للأمر هو:
```bash
source [options] [arguments]
```

## Common Options
- `-`: يُستخدم لتحديد ملف الشل.
- `.`: اختصار للأمر `source`، يمكن استخدامه بنفس الوظيفة.

## Common Examples
- **تنفيذ ملف نصي:**
```bash
source myscript.sh
```
هذا الأمر يقوم بتنفيذ الأوامر الموجودة في الملف `myscript.sh`.

- **استخدام الاختصار:**
```bash
. myscript.sh
```
هذا الأمر يقوم بنفس وظيفة الأمر السابق، حيث يتم استخدام النقطة كاختصار لـ `source`.

- **تحديث المتغيرات من ملف:**
```bash
source env_variables.sh
```
هذا الأمر يقوم بتحميل المتغيرات البيئية المحددة في `env_variables.sh` إلى البيئة الحالية.

## Tips
- تأكد من أن الملف النصي يحتوي على الأوامر الصحيحة لتجنب الأخطاء.
- استخدم `source` لتحميل المتغيرات أو الوظائف في جلسات الشل الحالية بدلاً من إنشاء جلسة جديدة.
- يمكنك استخدام `source` مع الملفات التي تحتوي على إعدادات خاصة بالبيئة مثل `.bashrc` لتحديث الإعدادات دون الحاجة لإعادة تشغيل الشل.