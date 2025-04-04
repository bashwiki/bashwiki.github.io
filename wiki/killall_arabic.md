# [لينكس] Bash killall الاستخدام: إنهاء العمليات حسب الاسم

## Overview
يستخدم أمر `killall` لإنهاء جميع العمليات التي تحمل اسمًا معينًا. يعتبر هذا الأمر مفيدًا عندما تحتاج إلى إنهاء جميع النسخ من برنامج معين دون الحاجة إلى معرفة معرف العملية (PID) لكل منها.

## Usage
تكون الصيغة الأساسية للأمر كالتالي:

```bash
killall [options] [arguments]
```

## Common Options
- `-u` : إنهاء العمليات التي تخص مستخدم معين.
- `-i` : طلب تأكيد قبل إنهاء كل عملية.
- `-q` : عدم عرض أي رسائل خطأ.
- `-s` : تحديد إشارة معينة لإرسالها للعمليات (مثل `SIGTERM` أو `SIGKILL`).

## Common Examples
- إنهاء جميع عمليات `firefox`:
    ```bash
    killall firefox
    ```

- إنهاء جميع عمليات `python`:
    ```bash
    killall python
    ```

- إنهاء جميع العمليات التي تخص مستخدم معين (مثلاً `username`):
    ```bash
    killall -u username
    ```

- إنهاء جميع عمليات `gedit` مع طلب تأكيد:
    ```bash
    killall -i gedit
    ```

- إرسال إشارة `SIGKILL` لإنهاء جميع عمليات `myapp`:
    ```bash
    killall -s SIGKILL myapp
    ```

## Tips
- تأكد من أنك تريد إنهاء جميع العمليات قبل استخدام `killall`، حيث يمكن أن يؤدي ذلك إلى فقدان البيانات غير المحفوظة.
- استخدم الخيار `-i` إذا كنت غير متأكد من العمليات التي ستقوم بإنهائها، حيث سيساعدك ذلك على تجنب الأخطاء.
- يمكنك استخدام `killall -q` لتقليل الضوضاء في مخرجات الأوامر، خاصة في السكربتات.