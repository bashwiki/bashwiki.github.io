# [لينكس] Bash systemctl الاستخدام: إدارة خدمات النظام

## Overview
يعتبر أمر `systemctl` أداة قوية لإدارة خدمات النظام في أنظمة التشغيل المعتمدة على نظام `systemd`. يتيح لك هذا الأمر بدء وإيقاف وإعادة تشغيل الخدمات، بالإضافة إلى التحقق من حالة الخدمات وتفعيلها أو تعطيلها.

## Usage
تكون الصيغة الأساسية لأمر `systemctl` كالتالي:

```bash
systemctl [options] [arguments]
```

## Common Options
- `start`: بدء خدمة معينة.
- `stop`: إيقاف خدمة معينة.
- `restart`: إعادة تشغيل خدمة معينة.
- `status`: عرض حالة خدمة معينة.
- `enable`: تفعيل خدمة لتبدأ تلقائيًا عند إقلاع النظام.
- `disable`: تعطيل خدمة بحيث لا تبدأ تلقائيًا عند إقلاع النظام.

## Common Examples
- لبدء خدمة `nginx`:
  ```bash
  systemctl start nginx
  ```

- لإيقاف خدمة `nginx`:
  ```bash
  systemctl stop nginx
  ```

- لإعادة تشغيل خدمة `nginx`:
  ```bash
  systemctl restart nginx
  ```

- للتحقق من حالة خدمة `nginx`:
  ```bash
  systemctl status nginx
  ```

- لتفعيل خدمة `nginx` لتبدأ تلقائيًا عند الإقلاع:
  ```bash
  systemctl enable nginx
  ```

- لتعطيل خدمة `nginx` من البدء تلقائيًا:
  ```bash
  systemctl disable nginx
  ```

## Tips
- تأكد من تشغيل الأوامر كمسؤول (root) أو باستخدام `sudo` عند الحاجة.
- استخدم `systemctl list-units --type=service` لعرض جميع الخدمات المتاحة وحالتها.
- تحقق من سجلات الخدمة باستخدام `journalctl -u [service_name]` للحصول على معلومات إضافية حول الأخطاء أو المشكلات.