# [Linux] Bash ps Использование: [просмотр процессов]

## Обзор
Команда `ps` используется для отображения текущих процессов, работающих на системе. Она предоставляет информацию о запущенных процессах, включая их идентификаторы, состояние и использование ресурсов.

## Использование
Основной синтаксис команды выглядит следующим образом:

```bash
ps [options] [arguments]
```

## Общие параметры
- `-e` или `-A`: показать все процессы.
- `-f`: вывести полную информацию о процессах.
- `-u [user]`: показать процессы, запущенные конкретным пользователем.
- `-aux`: показать все процессы с дополнительной информацией.
- `--sort`: сортировать вывод по указанному критерию.

## Общие примеры
1. Показать все процессы:
   ```bash
   ps -e
   ```

2. Показать процессы с полной информацией:
   ```bash
   ps -f
   ```

3. Показать процессы конкретного пользователя:
   ```bash
   ps -u username
   ```

4. Показать все процессы с дополнительной информацией:
   ```bash
   ps aux
   ```

5. Сортировать процессы по использованию памяти:
   ```bash
   ps aux --sort=-%mem
   ```

## Советы
- Используйте `ps aux` для получения наиболее полной информации о процессах.
- Комбинируйте параметры для более точного вывода, например, `ps -ef | grep process_name` для поиска конкретного процесса.
- Помните, что `ps` показывает состояние процессов на момент выполнения команды, поэтому для динамического мониторинга используйте `top` или `htop`.