# [리눅스] Bash true 사용법

## Overview
O comando `true` é uma ferramenta simples e útil no ambiente Bash que sempre retorna um status de saída de 0, indicando sucesso. Ele é frequentemente utilizado em scripts de shell e em pipelines para garantir que uma condição seja sempre verdadeira. Isso pode ser útil em diversas situações, como em loops ou quando um comando é necessário, mas não há uma ação a ser executada.

## Usage
A sintaxe básica do comando `true` é bastante simples:

```bash
true
```

O comando não possui opções ou argumentos. Sua única função é retornar um status de saída de 0.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `true`:

### Exemplo 1: Usando `true` em um loop
Você pode usar o comando `true` em um loop infinito. Isso pode ser útil para manter um script em execução até que uma condição externa o interrompa.

```bash
while true; do
    echo "Este loop está em execução. Pressione Ctrl+C para sair."
    sleep 1
done
```

### Exemplo 2: Usando `true` em um comando condicional
O comando `true` pode ser utilizado em um contexto onde um comando é necessário, mas não há uma ação específica a ser realizada.

```bash
if true; then
    echo "Esta condição é sempre verdadeira."
fi
```

## Tips
- **Uso em scripts**: O comando `true` é frequentemente usado em scripts para criar loops ou condições que devem ser sempre verdadeiras, permitindo que você controle o fluxo do script sem a necessidade de executar um comando real.
- **Combinação com outros comandos**: Você pode usar `true` em combinação com outros comandos para garantir que um pipeline não falhe. Por exemplo, `command1 || true` garante que, mesmo que `command1` falhe, o status de saída do pipeline será 0.
- **Legibilidade**: Embora `true` seja uma ferramenta simples, seu uso pode aumentar a legibilidade do seu código, deixando claro que uma condição sempre será verdadeira.

O comando `true` é uma ferramenta poderosa em sua simplicidade e pode ser um aliado valioso em scripts e automações no Bash.