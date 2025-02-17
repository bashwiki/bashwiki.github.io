# [لينكس] Bash getopts الاستخدام: [معالجة خيارات سطر الأوامر]

## Overview
تُستخدم أداة `getopts` في Bash لمعالجة خيارات سطر الأوامر بشكل منظم. تساعد هذه الأداة في تحليل الخيارات المعطاة للبرنامج، مما يسهل على المستخدمين تمرير المعلمات المختلفة.

## Usage
تكون الصيغة الأساسية لاستخدام `getopts` كالتالي:

```bash
getopts [options] [arguments]
```

## Common Options
- `-a`: يستخدم لتحديد خيارات متعددة.
- `-b`: يُستخدم لتحديد خيار واحد.
- `-c`: يُستخدم لتحديد خيار مع قيمة.
- `-d`: يُستخدم لتحديد خيار افتراضي.

## Common Examples

### مثال 1: استخدام getopts مع خيارات بسيطة
```bash
#!/bin/bash

while getopts "ab:c:" option; do
  case $option in
    a) echo "خيار a مفعل" ;;
    b) echo "خيار b مع القيمة: $OPTARG" ;;
    c) echo "خيار c مع القيمة: $OPTARG" ;;
    *) echo "خيار غير معروف" ;;
  esac
done
```

### مثال 2: معالجة خيارات مع قيم
```bash
#!/bin/bash

while getopts "u:p:" option; do
  case $option in
    u) echo "اسم المستخدم: $OPTARG" ;;
    p) echo "كلمة المرور: $OPTARG" ;;
    *) echo "خيار غير معروف" ;;
  esac
done
```

### مثال 3: استخدام خيار افتراضي
```bash
#!/bin/bash

while getopts "f:" option; do
  case $option in
    f) echo "تم تحديد الملف: $OPTARG" ;;
    *) echo "خيار غير معروف" ;;
  esac
done

# إذا لم يتم تمرير أي خيار، استخدم الخيار الافتراضي
if [ -z "$OPTARG" ]; then
  echo "لا يوجد ملف محدد، استخدام الملف الافتراضي."
fi
```

## Tips
- تأكد من استخدام `getopts` في حلقة `while` لتحليل جميع الخيارات بشكل صحيح.
- استخدم `OPTARG` للحصول على القيمة المرتبطة بالخيار.
- تأكد من التعامل مع الخيارات غير المعروفة بشكل مناسب لتجنب الأخطاء.