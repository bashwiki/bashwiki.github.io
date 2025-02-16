# [لینوکس] Bash dmesg استفاده: نمایش پیام‌های هسته

## Overview
دستور `dmesg` برای نمایش پیام‌های هسته (Kernel) سیستم عامل استفاده می‌شود. این پیام‌ها شامل اطلاعاتی درباره‌ی سخت‌افزار، درایورها و دیگر رویدادهای مربوط به سیستم هستند که در زمان بوت شدن یا در حین کار سیستم تولید می‌شوند.

## Usage
سینتکس پایه‌ی دستور `dmesg` به صورت زیر است:

```bash
dmesg [options] [arguments]
```

## Common Options
- `-C` : پاک کردن بافر پیام‌های دمسگ.
- `-c` : نمایش پیام‌ها و سپس پاک کردن بافر.
- `-n level` : تنظیم سطح گزارش‌دهی پیام‌ها.
- `-T` : نمایش زمان‌ها به صورت قابل خواندن برای انسان.
- `--help` : نمایش راهنمای استفاده از دستور.

## Common Examples
1. **نمایش تمام پیام‌های دمسگ:**
   ```bash
   dmesg
   ```

2. **نمایش پیام‌ها با زمان‌های قابل خواندن:**
   ```bash
   dmesg -T
   ```

3. **پاک کردن بافر پیام‌ها:**
   ```bash
   dmesg -C
   ```

4. **تنظیم سطح گزارش‌دهی:**
   ```bash
   dmesg -n 1
   ```

5. **نمایش پیام‌ها از زمان آخرین بوت:**
   ```bash
   dmesg | less
   ```

## Tips
- برای بررسی مشکلات سخت‌افزاری، می‌توانید از `dmesg` استفاده کنید تا ببینید آیا خطاهایی در زمان بوت شدن وجود داشته است.
- استفاده از `dmesg -T` می‌تواند به شما کمک کند تا زمان‌های دقیق‌تر و قابل فهم‌تری از رویدادها داشته باشید.
- برای فیلتر کردن پیام‌ها می‌توانید از `grep` استفاده کنید. به عنوان مثال:
  ```bash
  dmesg | grep error
  ```