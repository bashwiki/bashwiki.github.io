# [Linux] Bash mkdir Использование: создание каталогов

## Обзор
Команда `mkdir` используется для создания новых каталогов в файловой системе. Она позволяет пользователям организовывать файлы и директории, создавая иерархию данных.

## Использование
Основной синтаксис команды выглядит следующим образом:

```bash
mkdir [опции] [аргументы]
```

## Общие опции
- `-p`: Создает промежуточные каталоги, если они не существуют.
- `-v`: Выводит сообщение о каждом созданном каталоге.
- `-m`: Устанавливает права доступа для создаваемого каталога.

## Общие примеры
Создание простого каталога:

```bash
mkdir my_directory
```

Создание нескольких каталогов одновременно:

```bash
mkdir dir1 dir2 dir3
```

Создание каталога с промежуточными директориями:

```bash
mkdir -p parent/child/grandchild
```

Создание каталога с установленными правами доступа:

```bash
mkdir -m 755 my_secure_directory
```

## Советы
- Используйте опцию `-p`, чтобы избежать ошибок при создании вложенных каталогов.
- Проверяйте права доступа, если создаете каталоги, которые будут доступны другим пользователям.
- Регулярно организуйте свои файлы и каталоги, чтобы поддерживать порядок в системе.