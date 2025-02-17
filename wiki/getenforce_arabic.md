# [لينكس] Bash getenforce الاستخدام: عرض حالة SELinux

## Overview
يستخدم أمر `getenforce` لعرض حالة SELinux (Security-Enhanced Linux) على النظام. يوضح ما إذا كان SELinux مفعلًا أو معطلًا أو في وضع الإنفاذ.

## Usage
تكون الصيغة الأساسية للأمر كما يلي:
```bash
getenforce [options]
```

## Common Options
- لا توجد خيارات شائعة لأمر `getenforce`، حيث أنه يقوم فقط بعرض الحالة الحالية لـ SELinux.

## Common Examples
### مثال 1: عرض حالة SELinux
لعرض حالة SELinux الحالية، يمكنك ببساطة استخدام الأمر:
```bash
getenforce
```
سيظهر لك أحد القيم التالية: 
- Enforcing
- Permissive
- Disabled

### مثال 2: استخدام getenforce في سكربت
يمكنك استخدام `getenforce` في سكربت Bash للتحقق من حالة SELinux قبل تنفيذ أوامر معينة:
```bash
if [ "$(getenforce)" == "Enforcing" ]; then
    echo "SELinux مفعل"
else
    echo "SELinux غير مفعل أو في وضع Permissive"
fi
```

## Tips
- تأكد من تشغيل الأمر كجذر أو كمستخدم لديه صلاحيات كافية للحصول على معلومات SELinux.
- استخدم `getenforce` كجزء من عمليات التحقق من الأمان في سكربتاتك لضمان أن إعدادات SELinux متوافقة مع متطلبات الأمان الخاصة بك.