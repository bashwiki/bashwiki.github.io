# [Linux] Bash users использование: управление пользователями в системе

## Обзор
Команда `users` в Bash используется для отображения имен пользователей, которые в данный момент вошли в систему. Она показывает, кто активно использует систему в данный момент времени.

## Использование
Основной синтаксис команды выглядит следующим образом:

```bash
users [options] [arguments]
```

## Общие параметры
- `-n`: отображает только уникальные имена пользователей.
- `-r`: отображает только имена пользователей, которые имеют активные сеансы.

## Общие примеры
Вот несколько практических примеров использования команды `users`:

1. **Показать всех пользователей, вошедших в систему:**
   ```bash
   users
   ```

2. **Показать уникальные имена пользователей:**
   ```bash
   users -n
   ```

3. **Показать только активные сеансы пользователей:**
   ```bash
   users -r
   ```

## Советы
- Используйте команду `who` для получения более подробной информации о пользователях, включая время входа и терминал.
- Команда `users` может быть полезна для мониторинга активности системы, особенно на серверах с несколькими пользователями.
- Если вам нужно узнать, сколько пользователей в системе, вы можете использовать команду `who | wc -l`, чтобы подсчитать количество активных сеансов.