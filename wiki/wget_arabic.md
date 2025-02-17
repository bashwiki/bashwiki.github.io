# [لينكس] Bash wget الاستخدام: تحميل الملفات من الإنترنت

## Overview
يعتبر أمر `wget` أداة قوية لتحميل الملفات من الإنترنت. يمكن استخدامه لتحميل صفحة ويب كاملة أو ملف معين، وهو يدعم بروتوكولات HTTP وHTTPS وFTP.

## Usage
الصيغة الأساسية لأمر wget هي:

```bash
wget [options] [arguments]
```

## Common Options
- `-O [filename]`: حفظ الملف تحت اسم محدد.
- `-c`: استئناف تحميل ملف تم إيقافه سابقًا.
- `-r`: تحميل الملفات بشكل متكرر (تكرار).
- `--limit-rate=[rate]`: تحديد سرعة التحميل.
- `-q`: تشغيل الأمر في وضع صامت (بدون إخراج).

## Common Examples
- تحميل ملف من رابط مباشر:
```bash
wget https://example.com/file.zip
```

- حفظ الملف تحت اسم مختلف:
```bash
wget -O newfile.zip https://example.com/file.zip
```

- استئناف تحميل ملف:
```bash
wget -c https://example.com/largefile.zip
```

- تحميل صفحة ويب كاملة:
```bash
wget -r https://example.com
```

- تحديد سرعة التحميل:
```bash
wget --limit-rate=200k https://example.com/file.zip
```

## Tips
- تأكد من استخدام الخيار `-c` لاستئناف التحميلات الكبيرة في حالة انقطاع الاتصال.
- استخدم الخيار `-q` لتقليل الإخراج في حال كنت ترغب في تشغيل wget في الخلفية.
- يمكنك دمج wget مع أدوات أخرى مثل `tar` لضغط الملفات بعد تحميلها.