# [Linux] Bash tput использование: управление терминальным выводом

## Обзор
Команда `tput` используется для управления выводом в терминале, позволяя изменять атрибуты текста, такие как цвет, стиль и позицию курсора. Она взаимодействует с терминальными устройствами, используя термальные базы данных.

## Использование
Основной синтаксис команды `tput` выглядит следующим образом:

```bash
tput [options] [arguments]
```

## Общие опции
- `setaf [n]` — устанавливает цвет текста (где `n` — номер цвета).
- `setab [n]` — устанавливает цвет фона.
- `bold` — включает жирный шрифт.
- `clear` — очищает экран терминала.
- `cup [x] [y]` — перемещает курсор в позицию (x, y).

## Общие примеры
Вот несколько практических примеров использования команды `tput`:

### Изменение цвета текста
```bash
tput setaf 1
echo "Это красный текст"
tput sgr0
```

### Изменение цвета фона
```bash
tput setab 4
echo "Это текст на синем фоне"
tput sgr0
```

### Включение жирного шрифта
```bash
tput bold
echo "Это жирный текст"
tput sgr0
```

### Очистка экрана
```bash
tput clear
```

### Перемещение курсора
```bash
tput cup 10 20
echo "Курсор перемещён на строку 10, колонка 20"
```

## Советы
- Используйте `tput sgr0` после изменения атрибутов текста, чтобы сбросить их к стандартным значениям.
- Для получения списка доступных цветов используйте `tput colors`.
- Команда `tput` может быть полезна в скриптах для создания более интерактивного пользовательского интерфейса в терминале.