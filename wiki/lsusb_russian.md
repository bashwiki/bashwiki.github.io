# [Linux] Bash lsusb Использование: отображение информации о USB-устройствах

## Обзор
Команда `lsusb` используется для отображения информации о подключенных USB-устройствах на системе. Она предоставляет список всех USB-устройств, подключенных к вашему компьютеру, включая их идентификаторы и производители.

## Использование
Основной синтаксис команды выглядит следующим образом:

```bash
lsusb [options] [arguments]
```

## Общие параметры
- `-v` : Выводит подробную информацию о каждом USB-устройстве.
- `-t` : Отображает дерево USB-устройств.
- `-s <bus>:<device>` : Показывает информацию только для указанного устройства по его номеру шины и устройству.
- `-d <vendor>:<product>` : Фильтрует вывод по идентификатору производителя и продукта.

## Общие примеры
1. **Вывод списка всех USB-устройств:**
   ```bash
   lsusb
   ```

2. **Вывод подробной информации о всех USB-устройствах:**
   ```bash
   lsusb -v
   ```

3. **Отображение дерева USB-устройств:**
   ```bash
   lsusb -t
   ```

4. **Получение информации о конкретном устройстве:**
   ```bash
   lsusb -s 001:002
   ```

5. **Фильтрация по идентификатору производителя и продукта:**
   ```bash
   lsusb -d 1234:5678
   ```

## Советы
- Используйте `lsusb -v` для получения детальной информации, если вам нужно больше данных о конкретном устройстве.
- Команда `lsusb` может быть полезна для диагностики проблем с USB-устройствами, так как она показывает, распознаются ли устройства системой.
- Если вы часто используете `lsusb`, рассмотрите возможность создания алиаса в вашем `.bashrc` для быстрого доступа к наиболее используемым параметрам.