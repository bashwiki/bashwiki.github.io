# [리눅스] Bash jq 사용법

## Overview
O `jq` é uma ferramenta de linha de comando leve e flexível para processar dados JSON. Ele permite que desenvolvedores e engenheiros manipulem, filtrem e transformem dados JSON de maneira simples e eficiente. Com `jq`, é possível extrair informações específicas de documentos JSON, formatar a saída e até mesmo modificar os dados.

## Usage
A sintaxe básica do comando `jq` é a seguinte:

```bash
jq [OPÇÕES] 'FILTRAGEM' arquivo.json
```

### Opções Comuns:
- `-c`: Compacta a saída, removendo quebras de linha e espaços desnecessários.
- `-r`: Retorna a saída em formato bruto, sem aspas em torno de strings.
- `-f arquivo.jq`: Lê os filtros a partir de um arquivo externo.
- `--arg nome valor`: Define uma variável que pode ser usada dentro do filtro.

## Examples
### Exemplo 1: Extrair um campo específico
Suponha que você tenha um arquivo `dados.json` com o seguinte conteúdo:

```json
{
  "pessoas": [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25}
  ]
}
```

Para extrair apenas os nomes das pessoas, você pode usar o seguinte comando:

```bash
jq '.pessoas[].nome' dados.json
```

### Exemplo 2: Filtrar com base em uma condição
Se você quiser filtrar as pessoas com idade maior que 28, pode usar:

```bash
jq '.pessoas[] | select(.idade > 28)' dados.json
```

Isso retornará o objeto de Alice, pois ela é a única que atende à condição.

## Tips
- Sempre que possível, utilize a opção `-r` para obter uma saída mais limpa, especialmente se você estiver integrando `jq` com outros comandos ou scripts.
- Ao trabalhar com arquivos grandes, considere usar a opção `-c` para compactar a saída e facilitar a leitura.
- Familiarize-se com a sintaxe de filtragem do `jq`, pois ela é poderosa e permite realizar operações complexas em dados JSON de forma concisa.
- Utilize a documentação oficial do `jq` para explorar mais funcionalidades e exemplos avançados.