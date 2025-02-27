# [Linux] Bash iostat Использование: мониторинг ввода-вывода системы

## Обзор
Команда `iostat` используется для мониторинга ввода-вывода (I/O) системы, предоставляя информацию о производительности дисков и загрузке процессора. Она помогает администраторам систем и пользователям анализировать, как эффективно используются ресурсы ввода-вывода.

## Использование
Базовый синтаксис команды `iostat` выглядит следующим образом:

```
iostat [options] [arguments]
```

## Общие параметры
- `-c` — показывает статистику процессора.
- `-d` — отображает статистику дисков.
- `-x` — выводит расширенную информацию о дисках.
- `-m` — выводит данные в мегабайтах.
- `-p [device]` — показывает статистику для указанного устройства или всех устройств.

## Примеры использования
Вот несколько практических примеров использования команды `iostat`:

1. **Показать общую статистику ввода-вывода:**
   ```bash
   iostat
   ```

2. **Показать статистику процессора:**
   ```bash
   iostat -c
   ```

3. **Показать статистику дисков с расширенной информацией:**
   ```bash
   iostat -dx
   ```

4. **Показать статистику ввода-вывода в мегабайтах:**
   ```bash
   iostat -m
   ```

5. **Показать статистику для конкретного устройства:**
   ```bash
   iostat -p sda
   ```

## Советы
- Используйте `iostat` в сочетании с другими инструментами мониторинга, такими как `top` или `vmstat`, для более полного анализа производительности системы.
- Настройте периодический вывод данных с помощью команды `watch`, чтобы отслеживать изменения в реальном времени:
  ```bash
  watch -n 1 iostat -x
  ```
- Обратите внимание на высокие значения `await` и `svctm`, так как они могут указывать на проблемы с производительностью дисков.