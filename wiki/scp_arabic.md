# [لينكس] Bash scp الاستخدام: نقل الملفات بأمان بين الأنظمة

## Overview
يستخدم أمر `scp` (Secure Copy Protocol) لنقل الملفات بشكل آمن بين الأنظمة عبر الشبكة. يعتمد `scp` على بروتوكول SSH لضمان أمان البيانات أثناء النقل.

## Usage
تكون الصيغة الأساسية للأمر كما يلي:
```bash
scp [options] [source] [destination]
```

## Common Options
- `-r`: لنقل المجلدات بشكل متكرر.
- `-P`: لتحديد رقم المنفذ (port) عند الاتصال بالخادم.
- `-i`: لتحديد ملف المفتاح الخاص عند استخدام المصادقة بالمفتاح.
- `-v`: لتفعيل وضع التتبع (verbose) لعرض تفاصيل إضافية عن عملية النقل.

## Common Examples
### نقل ملف من النظام المحلي إلى خادم بعيد
```bash
scp /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
```

### نقل ملف من خادم بعيد إلى النظام المحلي
```bash
scp user@remote_host:/path/to/remote/file.txt /path/to/local/directory/
```

### نقل مجلد كامل من النظام المحلي إلى خادم بعيد
```bash
scp -r /path/to/local/directory user@remote_host:/path/to/remote/
```

### استخدام منفذ مخصص لنقل ملف
```bash
scp -P 2222 /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
```

## Tips
- تأكد من أن لديك الأذونات اللازمة على كلا النظامين قبل النقل.
- استخدم خيار `-v` لتشخيص أي مشاكل قد تواجهها أثناء النقل.
- عند نقل ملفات كبيرة، يمكنك استخدام `-C` لتفعيل الضغط وتحسين سرعة النقل.