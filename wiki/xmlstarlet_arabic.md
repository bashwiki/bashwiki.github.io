# [لينكس] Bash xmlstarlet الاستخدام: معالجة وتحويل ملفات XML

## Overview
أداة `xmlstarlet` هي أداة سطر أوامر قوية تستخدم لمعالجة وتحويل ملفات XML. تتيح لك هذه الأداة تنفيذ مجموعة متنوعة من العمليات على مستندات XML، مثل التعديل، البحث، والتحويل إلى تنسيقات أخرى.

## Usage
تستخدم `xmlstarlet` بالصيغة التالية:

```bash
xmlstarlet [options] [arguments]
```

## Common Options
- `xmlstarlet sel`: لاختيار البيانات من ملف XML.
- `xmlstarlet ed`: لتعديل مستند XML.
- `xmlstarlet val`: للتحقق من صحة ملف XML.
- `xmlstarlet fo`: لتنسيق ملف XML.
- `xmlstarlet tr`: لتحويل XML إلى تنسيق آخر باستخدام XSLT.

## Common Examples

### اختيار عناصر من XML
لاختيار عنصر معين من ملف XML، يمكنك استخدام الأمر التالي:

```bash
xmlstarlet sel -t -m "/root/element" -v "." -n file.xml
```

### تعديل عنصر في XML
لتعديل عنصر في ملف XML، يمكنك استخدام الأمر:

```bash
xmlstarlet ed -u "/root/element" -v "new_value" file.xml
```

### التحقق من صحة ملف XML
للتحقق من صحة ملف XML بالنسبة لمخطط معين، استخدم:

```bash
xmlstarlet val -e -s schema.xsd file.xml
```

### تنسيق ملف XML
لتنسيق ملف XML ليكون أكثر قابلية للقراءة، يمكنك استخدام:

```bash
xmlstarlet fo file.xml
```

### تحويل XML باستخدام XSLT
لتحويل ملف XML باستخدام XSLT، استخدم الأمر:

```bash
xmlstarlet tr stylesheet.xsl file.xml
```

## Tips
- تأكد من تثبيت `xmlstarlet` على نظامك قبل استخدامه.
- استخدم `xmlstarlet --help` للحصول على قائمة بجميع الخيارات المتاحة.
- قم بعمل نسخة احتياطية من ملفات XML قبل إجراء أي تعديلات عليها لتجنب فقدان البيانات.