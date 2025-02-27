# [لینوکس] Bash dirname استفاده: [دریافت نام دایرکتوری]

## Overview
دستور `dirname` در Bash برای استخراج نام دایرکتوری از یک مسیر فایل استفاده می‌شود. این دستور به شما کمک می‌کند تا بخش دایرکتوری یک مسیر کامل را جدا کنید و فقط نام دایرکتوری را به دست آورید.

## Usage
سینتکس پایه دستور `dirname` به شکل زیر است:

```bash
dirname [options] [arguments]
```

## Common Options
- `-z`: خروجی را به صورت null-terminated تولید می‌کند، که برای پردازش‌های خاص مفید است.

## Common Examples
در اینجا چند مثال عملی از استفاده از دستور `dirname` آورده شده است:

### مثال 1: استخراج نام دایرکتوری
برای استخراج نام دایرکتوری از یک مسیر کامل:

```bash
dirname /home/user/documents/file.txt
```
خروجی:
```
/home/user/documents
```

### مثال 2: استفاده با مسیر نسبی
اگر از یک مسیر نسبی استفاده کنید:

```bash
dirname ./projects/code/script.sh
```
خروجی:
```
./projects/code
```

### مثال 3: استفاده با چندین مسیر
شما می‌توانید چندین مسیر را به صورت همزمان به `dirname` بدهید:

```bash
dirname /var/log/syslog /etc/hosts
```
خروجی:
```
/var/log
/etc
```

## Tips
- از `dirname` در اسکریپت‌های خود برای جداسازی نام دایرکتوری از فایل‌ها استفاده کنید تا کد شما خواناتر و قابل نگهداری‌تر باشد.
- می‌توانید از `dirname` به همراه دستورات دیگر مانند `basename` برای پردازش‌های پیچیده‌تر استفاده کنید.
- در صورت استفاده از مسیرهای نسبی، مطمئن شوید که در دایرکتوری صحیح قرار دارید تا خروجی مورد انتظار را دریافت کنید.