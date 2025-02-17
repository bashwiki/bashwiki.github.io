# [Linux] Bash cal Uso: Exibir calendários

## Overview
O comando `cal` é utilizado para exibir calendários no terminal. Ele pode mostrar o calendário do mês atual, de um mês específico ou até mesmo de um ano inteiro. É uma ferramenta útil para visualizar datas rapidamente.

## Usage
A sintaxe básica do comando `cal` é a seguinte:

```bash
cal [opções] [argumentos]
```

## Common Options
- `-m`: Exibe o calendário começando pela segunda-feira.
- `-y`: Mostra o calendário do ano atual.
- `-3`: Exibe o calendário do mês anterior, do mês atual e do próximo mês.
- `-j`: Mostra o calendário com os dias do ano (número do dia).
- `-A <n>`: Exibe n meses após o mês atual.
- `-B <n>`: Exibe n meses antes do mês atual.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `cal`:

1. **Exibir o calendário do mês atual:**
   ```bash
   cal
   ```

2. **Exibir o calendário de um mês específico (por exemplo, março de 2023):**
   ```bash
   cal 03 2023
   ```

3. **Exibir o calendário do ano atual:**
   ```bash
   cal -y
   ```

4. **Exibir o calendário de três meses (mês anterior, atual e próximo):**
   ```bash
   cal -3
   ```

5. **Exibir o calendário com os dias do ano:**
   ```bash
   cal -j
   ```

## Tips
- Utilize a opção `-m` se preferir que a semana comece na segunda-feira, que é o padrão em muitos países.
- Combine as opções `-A` e `-B` para visualizar calendários de meses específicos em relação ao mês atual.
- Para uma visualização mais clara, considere redirecionar a saída do comando para um arquivo de texto, se precisar consultar mais tarde.