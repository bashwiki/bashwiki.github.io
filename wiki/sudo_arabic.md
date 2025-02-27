# [لينكس] Bash sudo الاستخدام: تنفيذ الأوامر بصلاحيات مرتفعة

## Overview
يعتبر الأمر `sudo` من الأوامر الأساسية في نظام لينكس، حيث يُستخدم لتنفيذ الأوامر بصلاحيات المستخدم الجذر (root). يسمح للمستخدمين بتنفيذ أوامر معينة تتطلب صلاحيات أعلى دون الحاجة لتسجيل الدخول كجذر.

## Usage
تكون الصيغة الأساسية لاستخدام الأمر `sudo` كما يلي:

```bash
sudo [options] [arguments]
```

## Common Options
- `-u [user]`: تنفيذ الأمر كمستخدم معين بدلاً من المستخدم الجذر.
- `-k`: إلغاء صلاحيات `sudo` الحالية، مما يتطلب إدخال كلمة المرور في المرة التالية.
- `-l`: عرض الأوامر التي يمكن للمستخدم تنفيذها باستخدام `sudo`.
- `-i`: بدء جلسة جديدة كالمستخدم الجذر.

## Common Examples
- تنفيذ أمر تحديث النظام:
  ```bash
  sudo apt update
  ```

- تثبيت حزمة جديدة:
  ```bash
  sudo apt install package_name
  ```

- إعادة تشغيل النظام:
  ```bash
  sudo reboot
  ```

- عرض الأوامر المسموح بها:
  ```bash
  sudo -l
  ```

- تنفيذ أمر كمستخدم مختلف:
  ```bash
  sudo -u username command
  ```

## Tips
- تأكد من أنك تعرف الأوامر التي تقوم بتنفيذها باستخدام `sudo`، حيث أن تنفيذ أوامر غير صحيحة قد يؤثر على النظام.
- استخدم `sudo -l` للتحقق من الأوامر المسموح لك بتنفيذها.
- حاول تقليل استخدام `sudo` إلى الحد الأدنى، واستخدمه فقط عند الحاجة.