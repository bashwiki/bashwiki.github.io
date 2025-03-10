# [لينكس] Bash wait الاستخدام: انتظار انتهاء العمليات

## Overview
أمر `wait` في Bash يُستخدم لانتظار انتهاء العمليات الفرعية (subprocesses) التي تم إنشاؤها في الجلسة الحالية. يُعتبر هذا الأمر مفيدًا في السيناريوهات التي تحتاج إلى التأكد من أن عملية معينة قد اكتملت قبل المتابعة إلى الخطوة التالية.

## Usage
التركيب الأساسي لأمر `wait` هو كما يلي:

```bash
wait [options] [arguments]
```

## Common Options
- `-n`: ينتظر انتهاء أول عملية فرعية تنتهي.
- `PID`: يُستخدم لتحديد معرف العملية (Process ID) التي ترغب في الانتظار حتى تنتهي.

## Common Examples
### مثال 1: انتظار عملية فرعية
```bash
sleep 5 &
wait $!
echo "العملية الفرعية انتهت."
```
في هذا المثال، يتم تشغيل أمر `sleep` في الخلفية، ثم ينتظر الأمر `wait` حتى تنتهي هذه العملية.

### مثال 2: انتظار عدة عمليات فرعية
```bash
sleep 3 &
sleep 5 &
wait
echo "جميع العمليات الفرعية انتهت."
```
هنا، يتم تشغيل عمليتين فرعيتين، وينتظر الأمر `wait` حتى تنتهي كلاهما.

### مثال 3: انتظار عملية معينة باستخدام PID
```bash
sleep 10 &
PID=$!
wait $PID
echo "العملية مع PID $PID انتهت."
```
في هذا المثال، يتم تخزين معرف العملية في متغير، ثم يُستخدم `wait` للانتظار حتى تنتهي هذه العملية المحددة.

## Tips
- استخدم `wait` في السكربتات لضمان أن العمليات الفرعية قد اكتملت قبل المتابعة.
- تأكد من استخدام `&` لتشغيل العمليات في الخلفية إذا كنت ترغب في استخدام `wait`.
- يمكن استخدام `wait` مع `trap` للتعامل مع الإشارات (signals) بشكل أفضل في السكربتات.