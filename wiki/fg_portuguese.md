# [Linux] Bash fg Uso equivalente: Retorna um processo em segundo plano para o primeiro plano

## Overview
O comando `fg` é utilizado no Bash para trazer um processo que está em segundo plano de volta para o primeiro plano. Isso é útil quando você deseja interagir com um processo que foi enviado para o fundo, permitindo que você continue a usá-lo como se estivesse rodando normalmente no terminal.

## Usage
A sintaxe básica do comando `fg` é a seguinte:

```bash
fg [opções] [número do trabalho]
```

## Common Options
- `-l`: Lista todos os trabalhos em segundo plano.
- `%n`: Especifica o trabalho a ser trazido para o primeiro plano, onde `n` é o número do trabalho.

## Common Examples

1. **Trazer o último trabalho para o primeiro plano:**
   ```bash
   fg
   ```

2. **Trazer um trabalho específico para o primeiro plano:**
   Se você tem um trabalho em segundo plano com o número 1:
   ```bash
   fg %1
   ```

3. **Listar todos os trabalhos em segundo plano:**
   ```bash
   jobs
   ```

4. **Trazer o trabalho mais recente para o primeiro plano:**
   ```bash
   fg %+
   ```

## Tips
- Use o comando `jobs` para verificar quais trabalhos estão em segundo plano antes de usar `fg`.
- Se você não especificar um número de trabalho, o `fg` trará o último trabalho em segundo plano para o primeiro plano.
- Lembre-se de que se o processo em primeiro plano for interrompido (por exemplo, pressionando `Ctrl + Z`), você pode usar `fg` para retomar a execução.