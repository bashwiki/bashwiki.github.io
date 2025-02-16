# [لینوکس] Bash xmlstarlet استفاده: پردازش و ویرایش XML

## Overview
دستورات `xmlstarlet` ابزاری قدرتمند برای پردازش و ویرایش فایل‌های XML در خط فرمان است. این ابزار به شما امکان می‌دهد تا به راحتی اطلاعات را از فایل‌های XML استخراج کنید، آن‌ها را ویرایش کنید و یا به فرمت‌های دیگر تبدیل کنید.

## Usage
سینتکس پایه دستور `xmlstarlet` به صورت زیر است:

```bash
xmlstarlet [options] [arguments]
```

## Common Options
- `xmlstarlet sel`: انتخاب و استخراج داده‌ها از فایل XML.
- `xmlstarlet ed`: ویرایش فایل XML.
- `xmlstarlet val`: اعتبارسنجی فایل XML بر اساس یک داکیومنت XSD.
- `xmlstarlet fo`: فرمت‌دهی فایل XML برای خوانایی بهتر.
- `xmlstarlet tr`: تبدیل فایل XML به فرمت‌های دیگر با استفاده از XSLT.

## Common Examples
### استخراج داده‌ها از XML
برای استخراج یک عنصر خاص از یک فایل XML:

```bash
xmlstarlet sel -t -m "/root/element" -v "text()" -n file.xml
```

### ویرایش XML
برای اضافه کردن یک عنصر جدید به فایل XML:

```bash
xmlstarlet ed -s "/root" -t -n "newElement" -v "newValue" file.xml
```

### اعتبارسنجی XML
برای اعتبارسنجی یک فایل XML با استفاده از یک داکیومنت XSD:

```bash
xmlstarlet val -e schema.xsd file.xml
```

### فرمت‌دهی XML
برای فرمت‌دهی یک فایل XML به منظور خوانایی بهتر:

```bash
xmlstarlet fo file.xml
```

## Tips
- همیشه قبل از ویرایش فایل‌های XML، یک نسخه پشتیبان از آن‌ها تهیه کنید.
- از گزینه `-d` برای حذف عناصر غیرضروری استفاده کنید تا فایل XML خود را بهینه کنید.
- برای یادگیری بیشتر، مستندات رسمی `xmlstarlet` را مطالعه کنید تا با امکانات پیشرفته‌تر آن آشنا شوید.