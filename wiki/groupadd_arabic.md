# [لينكس] Bash groupadd الاستخدام: إنشاء مجموعة جديدة

## Overview
يستخدم الأمر `groupadd` لإنشاء مجموعة جديدة في نظام التشغيل لينكس. يمكن أن تكون المجموعات مفيدة لتنظيم المستخدمين ومنحهم أذونات معينة.

## Usage
التركيب الأساسي للأمر هو:
```bash
groupadd [options] [arguments]
```

## Common Options
- `-g GID` : تحديد معرف المجموعة (GID) للمجموعة الجديدة.
- `-r` : إنشاء مجموعة نظام (system group).
- `-f` : إذا كانت المجموعة موجودة بالفعل، لا يظهر أي خطأ.

## Common Examples
- لإنشاء مجموعة جديدة باسم "developers":
```bash
groupadd developers
```

- لإنشاء مجموعة جديدة مع معرف مجموعة محدد:
```bash
groupadd -g 1001 mygroup
```

- لإنشاء مجموعة نظام:
```bash
groupadd -r sysgroup
```

- لإنشاء مجموعة جديدة مع خيار عدم إظهار الأخطاء إذا كانت المجموعة موجودة:
```bash
groupadd -f existinggroup
```

## Tips
- تأكد من أن لديك الأذونات اللازمة لإنشاء مجموعات جديدة، عادةً ما تحتاج إلى صلاحيات الجذر.
- استخدم الخيار `-g` لتجنب التعارض مع معرفات المجموعات الموجودة.
- تحقق من وجود المجموعة باستخدام الأمر `getent group` بعد إنشائها.