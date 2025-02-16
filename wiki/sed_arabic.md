# [لينكس] Bash sed الاستخدام: أداة لتعديل النصوص

## نظرة عامة
أداة `sed` (Stream Editor) هي أداة قوية لمعالجة النصوص في نظام لينكس. تُستخدم `sed` لتعديل النصوص بشكل غير تفاعلي، مما يعني أنه يمكن استخدامها لتطبيق تغييرات على الملفات أو البيانات في تدفق البيانات دون الحاجة إلى فتحها في محرر نصوص.

## الاستخدام
الصيغة الأساسية لأمر `sed` هي:

```bash
sed [options] [arguments]
```

## الخيارات الشائعة
- `-e`: يسمح بإضافة تعبيرات متعددة.
- `-i`: تعديل الملفات في الموقع (بدون إنشاء نسخة احتياطية).
- `-n`: يمنع `sed` من طباعة كل الأسطر، ويستخدم مع أوامر الطباعة مثل `p`.
- `s`: يستخدم لاستبدال النصوص.

## أمثلة شائعة
### استبدال نص في ملف
لنفترض أن لديك ملفًا يسمى `file.txt` وتريد استبدال كل ظهور لكلمة "old" بكلمة "new":

```bash
sed -i 's/old/new/g' file.txt
```

### حذف أسطر معينة
لحذف الأسطر من 2 إلى 4 من ملف:

```bash
sed '2,4d' file.txt
```

### طباعة أسطر معينة
لطباعة الأسطر من 1 إلى 3 فقط:

```bash
sed -n '1,3p' file.txt
```

### إضافة نص في نهاية كل سطر
لإضافة كلمة "end" في نهاية كل سطر في ملف:

```bash
sed 's/$/ end/' file.txt
```

## نصائح
- استخدم الخيار `-i` بحذر، حيث أنه يعدل الملفات الأصلية مباشرة. من الأفضل عمل نسخة احتياطية قبل التعديل.
- يمكنك استخدام التعبيرات العادية (regex) لجعل عمليات البحث والاستبدال أكثر قوة.
- جرب الأوامر أولاً مع خيار `-n` لمعرفة النتائج قبل تطبيق التعديلات على الملفات.