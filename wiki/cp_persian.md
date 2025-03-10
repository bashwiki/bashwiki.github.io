# [لینوکس] Bash cp استفاده: کپی فایل‌ها و دایرکتوری‌ها

## Overview
دستور `cp` در Bash برای کپی کردن فایل‌ها و دایرکتوری‌ها به کار می‌رود. این دستور به شما این امکان را می‌دهد که فایل‌ها را از یک مکان به مکان دیگر منتقل کنید یا نسخه‌های پشتیبان از آن‌ها تهیه کنید.

## Usage
سینتکس پایه دستور `cp` به شکل زیر است:

```bash
cp [options] [source] [destination]
```

## Common Options
- `-r`: کپی کردن دایرکتوری‌ها به صورت بازگشتی.
- `-i`: قبل از کپی کردن، از کاربر تأیید می‌خواهد.
- `-u`: فقط فایل‌هایی که جدیدتر از نسخه موجود هستند را کپی می‌کند.
- `-v`: نمایش اطلاعات کپی شدن فایل‌ها در حین انجام کار.

## Common Examples
- کپی کردن یک فایل به دایرکتوری دیگر:
  ```bash
  cp file.txt /path/to/destination/
  ```

- کپی کردن یک دایرکتوری به صورت بازگشتی:
  ```bash
  cp -r /path/to/source_directory /path/to/destination_directory/
  ```

- کپی کردن یک فایل و درخواست تأیید از کاربر:
  ```bash
  cp -i file.txt /path/to/destination/
  ```

- کپی کردن فقط فایل‌های جدیدتر:
  ```bash
  cp -u file.txt /path/to/destination/
  ```

- نمایش اطلاعات کپی شدن فایل‌ها:
  ```bash
  cp -v file.txt /path/to/destination/
  ```

## Tips
- همیشه قبل از استفاده از گزینه‌های خطرناک مانند `-r`، از محتوای دایرکتوری‌ها اطمینان حاصل کنید.
- از گزینه `-i` برای جلوگیری از جایگزینی ناخواسته فایل‌ها استفاده کنید.
- برای کپی کردن فایل‌های بزرگ، می‌توانید از گزینه `-v` برای پیگیری پیشرفت کار استفاده کنید.