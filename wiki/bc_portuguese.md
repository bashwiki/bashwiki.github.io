# [Linux] Bash bc Uso: Calculadora de precisão arbitrária

## Overview
O comando `bc` é uma calculadora de precisão arbitrária que permite realizar cálculos matemáticos diretamente no terminal. Ele suporta operações aritméticas básicas, funções matemáticas e pode ser utilizado em scripts para automatizar cálculos complexos.

## Usage
A sintaxe básica do comando `bc` é a seguinte:

```bash
bc [opções] [argumentos]
```

## Common Options
- `-l`: Carrega a biblioteca matemática padrão, que inclui funções como seno, cosseno e logaritmo.
- `-q`: Executa o `bc` em modo silencioso, sem mostrar a mensagem de boas-vindas.
- `-e`: Permite a execução de expressões diretamente na linha de comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `bc`:

### Exemplo 1: Cálculo simples
Para realizar uma soma simples:

```bash
echo "5 + 3" | bc
```
Saída:
```
8
```

### Exemplo 2: Cálculo com precisão
Para calcular a divisão com precisão de duas casas decimais:

```bash
echo "scale=2; 10 / 3" | bc
```
Saída:
```
3.33
```

### Exemplo 3: Usando a biblioteca matemática
Para calcular o seno de um ângulo em radianos:

```bash
echo "scale=4; s(1)" | bc -l
```
Saída:
```
0.8415
```

### Exemplo 4: Executando expressões diretamente
Para calcular uma expressão diretamente no terminal:

```bash
bc -e "5 * (2 + 3)"
```
Saída:
```
25
```

## Tips
- Sempre defina a variável `scale` para controlar a precisão dos resultados em operações de divisão.
- Utilize `bc -l` para acessar funções matemáticas avançadas que não estão disponíveis na versão padrão.
- Para scripts, redirecione a entrada do `bc` a partir de um arquivo para realizar cálculos mais complexos sem precisar digitar no terminal.