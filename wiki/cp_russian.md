# [Linux] Bash cp Использование: Копирование файлов и каталогов

## Обзор
Команда `cp` используется для копирования файлов и каталогов в Unix-подобных операционных системах. Она позволяет создавать дубликаты файлов или перемещать их в другое место.

## Использование
Основной синтаксис команды `cp` выглядит следующим образом:

```bash
cp [опции] [аргументы]
```

## Общие опции
- `-r` или `--recursive`: Копирует каталоги рекурсивно, включая все подкаталоги и файлы.
- `-i` или `--interactive`: Запрашивает подтверждение перед перезаписью существующих файлов.
- `-u` или `--update`: Копирует файлы только в том случае, если источник новее, чем цель, или если цель отсутствует.
- `-v` или `--verbose`: Выводит информацию о процессе копирования.

## Общие примеры
1. Копирование файла:
   ```bash
   cp файл.txt /путь/к/каталогу/
   ```

2. Копирование каталога рекурсивно:
   ```bash
   cp -r каталог/ /путь/к/новому/каталогу/
   ```

3. Копирование с подтверждением:
   ```bash
   cp -i файл.txt /путь/к/каталогу/
   ```

4. Копирование с выводом информации:
   ```bash
   cp -v файл.txt /путь/к/каталогу/
   ```

5. Копирование только новых или измененных файлов:
   ```bash
   cp -u файл.txt /путь/к/каталогу/
   ```

## Советы
- Используйте опцию `-i`, чтобы избежать случайной перезаписи файлов.
- При копировании больших каталогов с множеством файлов, опция `-v` поможет отслеживать процесс.
- Для резервного копирования данных рекомендуется использовать `cp -r`, чтобы сохранить всю структуру каталогов.