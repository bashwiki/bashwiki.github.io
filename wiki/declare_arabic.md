# [لينكس] Bash declare الاستخدام: تعريف المتغيرات في Bash

## Overview
يستخدم الأمر `declare` في Bash لتعريف المتغيرات وتحديد خصائصها. يمكن من خلاله إنشاء متغيرات جديدة، وتحديد نوعها، وتعيين قيم افتراضية لها.

## Usage
تكون الصيغة الأساسية للأمر كالتالي:

```bash
declare [options] [arguments]
```

## Common Options
- `-a`: تعريف مصفوفة.
- `-i`: تعريف متغير عددي (عدد صحيح).
- `-r`: تعريف متغير للقراءة فقط (لا يمكن تغييره).
- `-x`: تصدير المتغير إلى البيئة الخارجية (يمكن الوصول إليه من العمليات الفرعية).

## Common Examples

### تعريف متغير بسيط
```bash
declare myVar="Hello, World!"
echo $myVar
```

### تعريف مصفوفة
```bash
declare -a myArray=("apple" "banana" "cherry")
echo ${myArray[1]}  # النتيجة: banana
```

### تعريف متغير عددي
```bash
declare -i myNumber=10
myNumber+=5
echo $myNumber  # النتيجة: 15
```

### تعريف متغير للقراءة فقط
```bash
declare -r myConst="This is a constant"
echo $myConst
# myConst="New Value"  # سيؤدي هذا إلى خطأ
```

### تصدير متغير
```bash
declare -x myExportedVar="This is exported"
```

## Tips
- استخدم `declare` لتجنب الأخطاء عند تعريف المتغيرات، خاصة في البرامج الكبيرة.
- تأكد من استخدام الخيار `-r` للمتغيرات التي لا يجب تغييرها.
- استخدم `-x` لتصدير المتغيرات التي تحتاج إلى أن تكون متاحة في العمليات الفرعية.