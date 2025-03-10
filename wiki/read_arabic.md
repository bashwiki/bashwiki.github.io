# [لينكس] Bash read الاستخدام: قراءة المدخلات من المستخدم

## Overview
يستخدم الأمر `read` في Bash لقراءة المدخلات من المستخدم وتخزينها في متغيرات. يعد هذا الأمر مفيدًا في السيناريوهات التي تحتاج فيها إلى الحصول على معلومات من المستخدم أثناء تنفيذ السكربتات.

## Usage
تكون الصيغة الأساسية للأمر `read` كما يلي:

```bash
read [options] [arguments]
```

## Common Options
- `-p`: يتيح لك تحديد رسالة توجيه تظهر للمستخدم قبل قراءة المدخلات.
- `-a`: يستخدم لقراءة المدخلات في مصفوفة.
- `-d`: يحدد حرف النهاية الذي ينهي قراءة المدخلات (افتراضيًا هو newline).
- `-s`: يخفي المدخلات أثناء الكتابة (مفيد لكلمات المرور).

## Common Examples

### مثال 1: قراءة اسم المستخدم
```bash
read -p "أدخل اسمك: " username
echo "مرحبًا، $username!"
```

### مثال 2: قراءة عدة مدخلات
```bash
read -p "أدخل اسمك وعمرك: " name age
echo "اسمك هو $name وعمرك $age."
```

### مثال 3: قراءة المدخلات في مصفوفة
```bash
read -a fruits -p "أدخل أسماء الفواكه (مفصولة بمسافة): "
echo "الفواكه التي أدخلتها هي: ${fruits[@]}"
```

### مثال 4: قراءة كلمة مرور
```bash
read -s -p "أدخل كلمة المرور: " password
echo -e "\nتم إدخال كلمة المرور."
```

## Tips
- استخدم الخيار `-p` لتوفير تعليمات واضحة للمستخدم.
- تأكد من استخدام الخيار `-s` عند قراءة كلمات المرور للحفاظ على الخصوصية.
- يمكنك استخدام `IFS` (Internal Field Separator) لتحديد كيفية تقسيم المدخلات عند استخدام `read` مع مصفوفات.