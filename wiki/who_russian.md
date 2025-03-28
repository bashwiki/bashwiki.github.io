# [Linux] Bash who использование: показывает пользователей, вошедших в систему

## Обзор
Команда `who` в Bash используется для отображения списка пользователей, которые в данный момент вошли в систему. Она предоставляет информацию о том, кто активен на системе, включая имя пользователя, терминал, время входа и другую полезную информацию.

## Использование
Базовый синтаксис команды `who` выглядит следующим образом:

```bash
who [опции] [аргументы]
```

## Общие опции
- `-a`: Показывает все доступные данные о пользователях, включая информацию о входе и выходе.
- `-b`: Отображает время последнего перезагрузки системы.
- `-q`: Показывает только количество пользователей, вошедших в систему, и их имена.
- `--help`: Выводит справочную информацию о команде.

## Общие примеры
Вот несколько практических примеров использования команды `who`:

1. **Показать всех пользователей, вошедших в систему:**
   ```bash
   who
   ```

2. **Показать время последней перезагрузки системы:**
   ```bash
   who -b
   ```

3. **Показать только количество пользователей и их имена:**
   ```bash
   who -q
   ```

4. **Показать полную информацию о пользователях:**
   ```bash
   who -a
   ```

## Советы
- Используйте `who` вместе с другими командами, такими как `grep`, чтобы фильтровать результаты по конкретным пользователям.
- Если вам нужно отслеживать активность пользователей в реальном времени, рассмотрите возможность использования команды `w`, которая предоставляет более подробную информацию о текущих пользователях и их активности.
- Регулярно проверяйте, кто вошел в систему, чтобы поддерживать безопасность и контроль доступа к вашим системам.