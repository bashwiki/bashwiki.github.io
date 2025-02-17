# [Linux] Bash local uso equivalente: Definir variáveis locais em funções

## Overview
O comando `local` é utilizado em scripts Bash para declarar variáveis que têm um escopo local dentro de uma função. Isso significa que as variáveis definidas com `local` não afetam o ambiente global e são destruídas assim que a função termina sua execução.

## Usage
A sintaxe básica do comando `local` é a seguinte:

```bash
local [opções] nome_variável=valor
```

## Common Options
O comando `local` não possui muitas opções, mas aqui estão algumas considerações importantes:

- **nome_variável**: O nome da variável que você deseja declarar como local.
- **valor**: O valor que você deseja atribuir à variável local.

## Common Examples

### Exemplo 1: Declarar uma variável local simples
```bash
minha_funcao() {
    local mensagem="Olá, mundo!"
    echo $mensagem
}

minha_funcao
# Saída: Olá, mundo!
```

### Exemplo 2: Usar uma variável local em cálculos
```bash
soma() {
    local a=5
    local b=10
    local resultado=$((a + b))
    echo "A soma é: $resultado"
}

soma
# Saída: A soma é: 15
```

### Exemplo 3: Variável local não acessível fora da função
```bash
minha_funcao() {
    local numero=42
}

minha_funcao
echo $numero
# Saída: (nada, pois 'numero' é uma variável local)
```

## Tips
- Sempre que você precisar de uma variável que não deve interferir em outras partes do seu script, use `local`.
- Lembre-se de que variáveis locais são destruídas após a função ser concluída, então não conte com elas fora do escopo da função.
- Utilize `local` para evitar conflitos de nomes de variáveis em scripts mais complexos, especialmente quando várias funções estão sendo usadas.