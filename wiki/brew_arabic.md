# [لينكس] Bash brew الاستخدام: إدارة الحزم بسهولة

## Overview
أداة `brew` هي مدير حزم يُستخدم على أنظمة التشغيل المستندة إلى Unix مثل macOS وLinux. تُسهل هذه الأداة تثبيت وتحديث وإدارة البرمجيات والحزم من خلال واجهة سطر الأوامر.

## Usage
تكون الصيغة الأساسية لاستخدام الأمر `brew` كما يلي:

```bash
brew [options] [arguments]
```

## Common Options
- `install`: لتثبيت حزمة جديدة.
- `uninstall`: لإزالة حزمة مثبتة.
- `update`: لتحديث قائمة الحزم المتاحة.
- `upgrade`: لترقية الحزم المثبتة إلى أحدث إصدار.
- `list`: لعرض قائمة الحزم المثبتة.

## Common Examples
- لتثبيت حزمة جديدة مثل `wget`:
  ```bash
  brew install wget
  ```

- لإزالة حزمة مثبتة مثل `wget`:
  ```bash
  brew uninstall wget
  ```

- لتحديث قائمة الحزم:
  ```bash
  brew update
  ```

- لترقية جميع الحزم المثبتة:
  ```bash
  brew upgrade
  ```

- لعرض قائمة الحزم المثبتة:
  ```bash
  brew list
  ```

## Tips
- تأكد من تحديث `brew` بانتظام للحصول على أحدث الحزم.
- استخدم `brew search [package_name]` للبحث عن حزم معينة قبل تثبيتها.
- يمكنك استخدام `brew info [package_name]` للحصول على معلومات مفصلة عن أي حزمة.