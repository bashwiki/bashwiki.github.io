# [Linux] Bash printf Использование: Форматированный вывод текста

## Обзор
Команда `printf` в Bash используется для форматированного вывода текста. Она позволяет выводить строки с заданным форматом, что делает её более гибкой по сравнению с командой `echo`.

## Использование
Основной синтаксис команды выглядит следующим образом:

```bash
printf [options] [arguments]
```

## Общие параметры
- `-v var`: Сохраняет результат в переменной `var`.
- `--help`: Показывает справочную информацию о команде.
- `--version`: Выводит информацию о версии `printf`.

## Общие примеры

1. **Простой вывод строки:**
   ```bash
   printf "Hello, World!\n"
   ```

2. **Форматированный вывод чисел:**
   ```bash
   printf "Число: %d\n" 42
   ```

3. **Вывод с плавающей точкой:**
   ```bash
   printf "Число с плавающей точкой: %.2f\n" 3.14159
   ```

4. **Вывод нескольких значений:**
   ```bash
   printf "Имя: %s, Возраст: %d\n" "Алексей" 30
   ```

5. **Сохранение результата в переменной:**
   ```bash
   printf -v my_var "Результат: %.2f" 12.3456
   echo "$my_var"
   ```

## Советы
- Используйте `\n` для переноса строки в выводе.
- Для форматирования чисел используйте спецификаторы, такие как `%d` для целых чисел и `%.2f` для чисел с плавающей точкой.
- Проверяйте правильность формата, чтобы избежать неожиданных результатов.