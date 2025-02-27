# [لينكس] Bash id الاستخدام: عرض معلومات المستخدم

## Overview
يستخدم الأمر `id` في نظام التشغيل لينكس لعرض معلومات حول المستخدم الحالي أو مستخدم آخر. يتضمن ذلك معرف المستخدم (UID) ومعرف المجموعة (GID) والمجموعات التي ينتمي إليها المستخدم.

## Usage
يمكن استخدام الأمر `id` بالصيغة التالية:

```bash
id [options] [arguments]
```

## Common Options
- `-u`: عرض معرف المستخدم (UID) فقط.
- `-g`: عرض معرف المجموعة (GID) فقط.
- `-G`: عرض جميع معرفات المجموعات التي ينتمي إليها المستخدم.
- `-n`: عرض اسم المستخدم أو اسم المجموعة بدلاً من المعرف.

## Common Examples
- لعرض معلومات المستخدم الحالي:
  ```bash
  id
  ```

- لعرض معرف المستخدم فقط:
  ```bash
  id -u
  ```

- لعرض معرف المجموعة فقط:
  ```bash
  id -g
  ```

- لعرض جميع معرفات المجموعات:
  ```bash
  id -G
  ```

- لعرض معلومات مستخدم معين (على سبيل المثال، المستخدم "username"):
  ```bash
  id username
  ```

## Tips
- استخدم `id -n` للحصول على أسماء المستخدمين والمجموعات بدلاً من الأرقام، مما يجعل المعلومات أكثر وضوحًا.
- يمكنك دمج الخيارات للحصول على معلومات محددة، مثل `id -u -n` للحصول على اسم المستخدم فقط.
- الأمر `id` مفيد في السكربتات لفهم الأذونات والمجموعات التي ينتمي إليها المستخدم.