# [لينكس] Bash ethtool الاستخدام: أداة لإدارة إعدادات الشبكة

## نظرة عامة
تعتبر أداة `ethtool` أداة قوية في نظام لينكس تُستخدم لإدارة إعدادات واجهات الشبكة. تتيح لك هذه الأداة عرض وتعديل خصائص بطاقة الشبكة، مما يساعد في تحسين الأداء وحل المشكلات المتعلقة بالشبكة.

## الاستخدام
يمكن استخدام الأمر `ethtool` مع مجموعة من الخيارات لتحديد الإعدادات المطلوبة. الصيغة الأساسية للأمر هي:

```bash
ethtool [options] [arguments]
```

## الخيارات الشائعة
- `-h` : عرض مساعدة مختصرة.
- `-s` : تغيير إعدادات واجهة الشبكة.
- `-i` : عرض معلومات حول برنامج التشغيل.
- `-p` : تشغيل مصباح الواجهة لتسهيل التعرف عليها.
- `-t` : تشغيل اختبار على بطاقة الشبكة.

## أمثلة شائعة
- **عرض معلومات بطاقة الشبكة:**
```bash
ethtool eth0
```

- **تغيير سرعة واجهة الشبكة إلى 1000 ميجابت في الثانية:**
```bash
ethtool -s eth0 speed 1000 duplex full
```

- **عرض معلومات برنامج التشغيل لواجهة الشبكة:**
```bash
ethtool -i eth0
```

- **تشغيل مصباح الواجهة:**
```bash
ethtool -p eth0
```

## نصائح
- تأكد من تشغيل الأمر كمسؤول (root) للحصول على كافة الصلاحيات اللازمة.
- استخدم الأمر `ethtool -h` للحصول على قائمة كاملة بالخيارات المتاحة.
- تحقق من الوثائق الخاصة ببطاقة الشبكة الخاصة بك لفهم الخيارات المدعومة بشكل أفضل.