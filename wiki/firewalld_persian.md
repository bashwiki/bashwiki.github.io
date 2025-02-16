# [لینوکس] Bash firewalld استفاده: مدیریت فایروال

## Overview
فرمان `firewalld` ابزاری برای مدیریت فایروال در سیستم‌های لینوکسی است. این ابزار به کاربران اجازه می‌دهد تا قوانین و سیاست‌های امنیتی را به راحتی تنظیم کنند و به صورت دینامیک تغییرات را اعمال نمایند.

## Usage
سینتکس پایه فرمان `firewalld` به صورت زیر است:

```bash
firewalld [options] [arguments]
```

## Common Options
- `--zone`: تعیین ناحیه‌ای که قوانین فایروال بر آن اعمال می‌شود.
- `--add-service`: اضافه کردن سرویس به ناحیه مشخص.
- `--remove-service`: حذف سرویس از ناحیه مشخص.
- `--list-all`: نمایش تمام تنظیمات و قوانین ناحیه فعلی.
- `--reload`: بارگذاری مجدد تنظیمات فایروال.

## Common Examples
- **نمایش ناحیه‌های فعال:**
  ```bash
  firewall-cmd --get-active-zones
  ```

- **اضافه کردن سرویس HTTP به ناحیه عمومی:**
  ```bash
  firewall-cmd --zone=public --add-service=http --permanent
  ```

- **حذف سرویس FTP از ناحیه داخلی:**
  ```bash
  firewall-cmd --zone=internal --remove-service=ftp --permanent
  ```

- **نمایش تمام تنظیمات ناحیه فعلی:**
  ```bash
  firewall-cmd --list-all
  ```

- **بارگذاری مجدد تنظیمات فایروال:**
  ```bash
  firewall-cmd --reload
  ```

## Tips
- همیشه پس از تغییرات، از فرمان `--reload` برای بارگذاری مجدد تنظیمات استفاده کنید.
- از گزینه `--permanent` برای ذخیره تغییرات به صورت دائمی استفاده کنید.
- برای بررسی وضعیت فایروال، از `firewall-cmd --state` استفاده کنید تا مطمئن شوید فایروال در حال اجراست.