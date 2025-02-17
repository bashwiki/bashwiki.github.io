# [Linux] Bash true uso equivalente: Comando que sempre retorna verdadeiro

## Overview
O comando `true` é uma ferramenta simples no Bash que sempre retorna um código de saída 0, indicando sucesso. Ele é frequentemente utilizado em scripts para representar uma condição verdadeira ou para preencher espaços onde um comando é esperado, mas nenhuma ação real precisa ser executada.

## Usage
A sintaxe básica do comando `true` é a seguinte:

```bash
true [opções] [argumentos]
```

No entanto, o `true` não aceita opções ou argumentos, então a execução do comando é bastante direta.

## Common Options
O comando `true` não possui opções ou argumentos comuns, pois sua única função é retornar um código de saída de 0. 

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `true`:

### Exemplo 1: Usando true em um loop
```bash
while true; do
    echo "Este loop nunca termina."
done
```
Neste exemplo, o loop `while` continuará indefinidamente, pois `true` sempre retorna verdadeiro.

### Exemplo 2: Usando true em um script de teste
```bash
#!/bin/bash
if true; then
    echo "A condição é verdadeira."
fi
```
Aqui, a mensagem "A condição é verdadeira." será exibida, pois o `true` sempre avalia como verdadeiro.

### Exemplo 3: Usando true com um comando de espera
```bash
true && echo "O comando anterior foi executado com sucesso."
```
Neste caso, a mensagem será exibida, pois o `true` garante que o comando anterior foi bem-sucedido.

## Tips
- Use `true` em scripts para criar loops infinitos ou como um espaço reservado para comandos que ainda não foram implementados.
- Combine `true` com operadores lógicos para simplificar condições em scripts.
- Lembre-se de que `true` não realiza nenhuma ação, apenas retorna um código de saída, então use-o quando precisar de uma condição sempre verdadeira.