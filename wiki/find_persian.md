# [لینوکس] Bash find معادل استفاده: جستجوی نام فایل‌ها

## Overview
دستور `find` در Bash برای جستجوی فایل‌ها و دایرکتوری‌ها در یک سیستم فایل استفاده می‌شود. این دستور به شما این امکان را می‌دهد که فایل‌ها را بر اساس نام، نوع، اندازه، تاریخ و سایر ویژگی‌ها پیدا کنید.

## Usage
سینتکس پایه دستور `find` به صورت زیر است:

```bash
find [options] [arguments]
```

## Common Options
- `-name`: جستجوی فایل‌ها بر اساس نام.
- `-type`: جستجوی فایل‌ها بر اساس نوع (مثل `f` برای فایل‌های عادی و `d` برای دایرکتوری‌ها).
- `-size`: جستجوی فایل‌ها بر اساس اندازه.
- `-mtime`: جستجوی فایل‌ها بر اساس تاریخ آخرین تغییر.
- `-exec`: اجرای یک دستور بر روی فایل‌های پیدا شده.

## Common Examples
- جستجوی فایل‌ها با نام خاص:
    ```bash
    find /path/to/directory -name "filename.txt"
    ```

- جستجوی همه فایل‌های با پسوند `.jpg`:
    ```bash
    find /path/to/directory -name "*.jpg"
    ```

- جستجوی دایرکتوری‌ها:
    ```bash
    find /path/to/directory -type d -name "foldername"
    ```

- جستجوی فایل‌ها بزرگتر از 1 مگابایت:
    ```bash
    find /path/to/directory -size +1M
    ```

- جستجوی فایل‌ها که در 7 روز گذشته تغییر کرده‌اند:
    ```bash
    find /path/to/directory -mtime -7
    ```

- اجرای یک دستور بر روی فایل‌های پیدا شده:
    ```bash
    find /path/to/directory -name "*.log" -exec rm {} \;
    ```

## Tips
- برای جستجوی سریع‌تر، از گزینه `-maxdepth` برای محدود کردن عمق جستجو استفاده کنید.
- از گزینه `-iname` به جای `-name` برای جستجوی غیرحساس به حروف بزرگ و کوچک استفاده کنید.
- همیشه قبل از استفاده از `-exec`، از دستور `-print` برای بررسی فایل‌های پیدا شده استفاده کنید تا از حذف یا تغییر ناخواسته جلوگیری شود.