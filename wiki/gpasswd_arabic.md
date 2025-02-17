# [لينكس] Bash gpasswd الاستخدام: إدارة مجموعات المستخدمين

## Overview
يستخدم أمر `gpasswd` لإدارة مجموعات المستخدمين في نظام لينكس. يتيح لك هذا الأمر إضافة أو إزالة مستخدمين من مجموعة معينة، بالإضافة إلى تغيير كلمة مرور المجموعة.

## Usage
تكون الصيغة الأساسية للأمر كالتالي:

```bash
gpasswd [options] [arguments]
```

## Common Options
- `-a, --add`: إضافة مستخدم إلى مجموعة.
- `-d, --delete`: إزالة مستخدم من مجموعة.
- `-r, --remove`: إزالة مجموعة.
- `-A, --administrators`: تعيين مجموعة من مديري المجموعة.
- `-M, --members`: تعيين أعضاء المجموعة.

## Common Examples
- **إضافة مستخدم إلى مجموعة:**
```bash
gpasswd -a username groupname
```

- **إزالة مستخدم من مجموعة:**
```bash
gpasswd -d username groupname
```

- **تغيير كلمة مرور مجموعة:**
```bash
gpasswd groupname
```

- **تعيين مديري المجموعة:**
```bash
gpasswd -A admin1,admin2 groupname
```

- **تعيين أعضاء المجموعة:**
```bash
gpasswd -M user1,user2 groupname
```

## Tips
- تأكد من أن لديك صلاحيات الجذر (root) عند استخدام `gpasswd` لتجنب أي مشاكل في الوصول.
- استخدم الأمر `groups username` للتحقق من المجموعات التي ينتمي إليها المستخدم.
- يمكنك استخدام `man gpasswd` للحصول على مزيد من المعلومات حول الخيارات المتاحة.