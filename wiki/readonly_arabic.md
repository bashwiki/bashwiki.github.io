# [لينكس] Bash readonly الاستخدام: تعيين المتغيرات كغير قابلة للتغيير

## Overview
يستخدم الأمر `readonly` في Bash لجعل المتغيرات غير قابلة للتغيير. عندما يتم تعيين متغير كـ readonly، لا يمكن تعديل قيمته أو إعادة تعيينه خلال جلسة العمل الحالية.

## Usage
تكون الصيغة الأساسية للأمر كما يلي:

```bash
readonly [options] [arguments]
```

## Common Options
- `-p`: يعرض جميع المتغيرات المعرفة كـ readonly مع قيمها.

## Common Examples
### تعيين متغير كـ readonly
```bash
readonly MY_VAR="Hello, World!"
```
بعد تنفيذ هذا الأمر، لن تتمكن من تغيير قيمة `MY_VAR`.

### محاولة تعديل متغير readonly
```bash
MY_VAR="New Value"  # سيؤدي هذا إلى خطأ
```

### عرض المتغيرات readonly
```bash
readonly -p
```
سيظهر لك قائمة بجميع المتغيرات المعرفة كـ readonly.

## Tips
- استخدم `readonly` عند الحاجة إلى حماية المتغيرات من التغييرات غير المقصودة.
- تأكد من أنك بحاجة إلى جعل المتغير readonly قبل تعيينه، حيث لا يمكن التراجع عن هذا الإجراء.