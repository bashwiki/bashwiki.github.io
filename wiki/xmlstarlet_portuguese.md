# [Linux] Bash xmlstarlet uso: Manipulação e transformação de XML

## Overview
O comando `xmlstarlet` é uma ferramenta poderosa para a manipulação e transformação de documentos XML. Ele permite que os usuários realizem operações como consulta, edição, validação e formatação de arquivos XML de maneira eficiente através da linha de comando.

## Usage
A sintaxe básica do comando `xmlstarlet` é a seguinte:

```bash
xmlstarlet [options] [arguments]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `xmlstarlet`:

- `xmlstarlet sel`: Seleciona partes de um documento XML usando XPath.
- `xmlstarlet ed`: Edita um documento XML, permitindo adicionar, modificar ou remover elementos e atributos.
- `xmlstarlet val`: Valida um documento XML contra um esquema XSD.
- `xmlstarlet fo`: Formata um documento XML para melhorar a legibilidade.
- `xmlstarlet tr`: Transforma um documento XML usando XSLT.

## Common Examples

### Selecionar elementos de um XML
Para selecionar elementos de um arquivo XML, você pode usar o seguinte comando:

```bash
xmlstarlet sel -t -m "//nome" -v "." -n arquivo.xml
```

### Editar um elemento XML
Para editar um elemento específico, você pode usar o comando `ed`:

```bash
xmlstarlet ed -u "/root/nome" -v "Novo Nome" arquivo.xml
```

### Validar um arquivo XML
Para validar um arquivo XML contra um esquema XSD, utilize:

```bash
xmlstarlet val -e -s esquema.xsd arquivo.xml
```

### Formatar um arquivo XML
Para formatar um arquivo XML e torná-lo mais legível, use:

```bash
xmlstarlet fo arquivo.xml
```

### Transformar um XML usando XSLT
Para transformar um documento XML com um arquivo XSLT, você pode fazer o seguinte:

```bash
xmlstarlet tr transformacao.xsl arquivo.xml
```

## Tips
- Sempre faça um backup dos seus arquivos XML antes de realizar edições, para evitar perda de dados.
- Utilize a opção `-o` para salvar a saída em um novo arquivo, ao invés de sobrescrever o arquivo original.
- Familiarize-se com XPath e XSLT, pois essas linguagens são fundamentais para aproveitar ao máximo o `xmlstarlet`.