# [لینوکس] Bash gcc استفاده: کامپایلر زبان C و C++

## Overview
دستور `gcc` (GNU Compiler Collection) یک کامپایلر برای زبان‌های برنامه‌نویسی C و C++ است. این ابزار به برنامه‌نویسان این امکان را می‌دهد که کدهای نوشته شده در این زبان‌ها را به کد ماشین تبدیل کنند تا بتوانند آن‌ها را اجرا کنند.

## Usage
سینتکس پایه دستور `gcc` به صورت زیر است:

```bash
gcc [options] [arguments]
```

## Common Options
- `-o <file>`: نام فایل خروجی را مشخص می‌کند.
- `-Wall`: هشدارهای مربوط به کد را فعال می‌کند.
- `-g`: اطلاعات دیباگ را به فایل خروجی اضافه می‌کند.
- `-O2`: بهینه‌سازی کد را فعال می‌کند.
- `-I<directory>`: دایرکتوری‌های اضافی برای جستجوی فایل‌های هدر را مشخص می‌کند.

## Common Examples
- کامپایل یک فایل C ساده:
    ```bash
    gcc hello.c -o hello
    ```
- کامپایل با فعال کردن هشدارها:
    ```bash
    gcc -Wall hello.c -o hello
    ```
- کامپایل با اطلاعات دیباگ:
    ```bash
    gcc -g hello.c -o hello
    ```
- کامپایل و بهینه‌سازی کد:
    ```bash
    gcc -O2 hello.c -o hello
    ```

## Tips
- همیشه از گزینه `-Wall` استفاده کنید تا از هشدارهای مفید در مورد کد خود مطلع شوید.
- برای دیباگ کردن برنامه‌ها، گزینه `-g` را فراموش نکنید.
- نام فایل خروجی را با استفاده از گزینه `-o` مشخص کنید تا به راحتی آن را شناسایی کنید.
- اگر از کتابخانه‌های خارجی استفاده می‌کنید، از گزینه `-I` برای مشخص کردن دایرکتوری‌های هدر استفاده کنید.