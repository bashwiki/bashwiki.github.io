# [لینوکس] Bash nohup استفاده: اجرای دستورات بدون قطع شدن

## Overview
دستور `nohup` (به معنای "بدون قطع شدن") در Bash به شما این امکان را می‌دهد که یک فرایند را در پس‌زمینه اجرا کنید، به طوری که حتی اگر شما از ترمینال خارج شوید یا اتصال قطع شود، فرایند همچنان به کار خود ادامه دهد. این دستور معمولاً برای اجرای برنامه‌های طولانی‌مدت یا اسکریپت‌ها استفاده می‌شود.

## Usage
سینتکس پایه دستور `nohup` به شکل زیر است:

```bash
nohup [options] [arguments]
```

## Common Options
- `&`: اجرای دستور در پس‌زمینه.
- `-h`: نمایش راهنما و اطلاعات مربوط به استفاده از nohup.
- `-v`: نمایش اطلاعات بیشتر در مورد فرایند در حال اجرا.

## Common Examples
### مثال ۱: اجرای یک اسکریپت در پس‌زمینه
برای اجرای یک اسکریپت به نام `script.sh` بدون قطع شدن، می‌توانید از دستور زیر استفاده کنید:

```bash
nohup bash script.sh &
```

### مثال ۲: اجرای یک برنامه طولانی‌مدت
اگر می‌خواهید یک برنامه مانند `python` را اجرا کنید و از قطع شدن آن جلوگیری کنید:

```bash
nohup python long_running_script.py &
```

### مثال ۳: ذخیره خروجی در یک فایل
برای ذخیره خروجی برنامه در یک فایل، می‌توانید به این شکل عمل کنید:

```bash
nohup command > output.log &
```

## Tips
- همیشه از `&` برای اجرای فرایند در پس‌زمینه استفاده کنید تا ترمینال شما آزاد بماند.
- خروجی فرایند را به یک فایل هدایت کنید تا بتوانید بعداً آن را بررسی کنید.
- از دستور `jobs` برای مشاهده فرایندهای در حال اجرای پس‌زمینه استفاده کنید.