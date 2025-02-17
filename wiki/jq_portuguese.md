# [Linux] Bash jq Uso: Processamento de JSON

## Overview
O `jq` é uma ferramenta de linha de comando poderosa para processar e manipular dados em formato JSON. Ele permite que você filtre, transforme e extraia informações de arquivos JSON de maneira eficiente e intuitiva.

## Usage
A sintaxe básica do comando `jq` é a seguinte:

```bash
jq [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `jq`:

- `-c`: Compacta a saída, removendo quebras de linha e espaços desnecessários.
- `-r`: Retorna a saída em formato "raw", sem aspas.
- `-f <file>`: Lê as expressões jq de um arquivo em vez de da linha de comando.
- `--arg <name> <value>`: Define uma variável que pode ser usada dentro da expressão jq.

## Common Examples

### Exemplo 1: Ler um arquivo JSON
Para ler um arquivo JSON e exibir seu conteúdo:

```bash
jq . arquivo.json
```

### Exemplo 2: Filtrar um campo específico
Para extrair um campo específico de um objeto JSON:

```bash
jq '.nome' arquivo.json
```

### Exemplo 3: Filtrar uma lista de objetos
Para filtrar objetos em uma lista com base em uma condição:

```bash
jq '.pessoas[] | select(.idade > 30)' arquivo.json
```

### Exemplo 4: Modificar um campo
Para modificar um campo em um objeto JSON:

```bash
jq '.pessoas[].idade += 1' arquivo.json
```

### Exemplo 5: Exportar para um novo arquivo
Para salvar a saída filtrada em um novo arquivo:

```bash
jq '.pessoas[] | select(.idade > 30)' arquivo.json > resultado.json
```

## Tips
- Sempre verifique a estrutura do seu JSON antes de aplicar filtros. Você pode usar `jq . arquivo.json` para visualizar a estrutura.
- Utilize a opção `-r` se você precisar da saída em um formato que não seja JSON, como texto simples.
- Experimente usar variáveis com `--arg` para tornar suas expressões mais dinâmicas e reutilizáveis.