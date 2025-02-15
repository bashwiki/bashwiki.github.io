# [리눅스] Bash xmlstarlet 사용법

## Overview
O `xmlstarlet` é uma ferramenta de linha de comando projetada para manipulação de arquivos XML. Ele permite que os usuários realizem uma variedade de operações em documentos XML, como transformação, validação, consulta e edição. O `xmlstarlet` é amplamente utilizado por desenvolvedores e engenheiros para automatizar tarefas relacionadas a XML, tornando-o uma ferramenta poderosa para processamento de dados estruturados.

## Usage
A sintaxe básica do comando `xmlstarlet` é a seguinte:

```bash
xmlstarlet [opções] comando [argumentos]
```

Alguns dos comandos e opções mais comuns incluem:

- `xmlstarlet sel`: Seleciona e extrai dados de documentos XML.
- `xmlstarlet ed`: Edita documentos XML, permitindo adicionar, modificar ou remover elementos e atributos.
- `xmlstarlet tr`: Aplica transformações XSLT a documentos XML.
- `xmlstarlet val`: Valida documentos XML contra um esquema.

Exemplo de uso básico:

```bash
xmlstarlet sel -t -m "//elemento" -v "." -n arquivo.xml
```

Neste exemplo, o comando seleciona todos os elementos chamados "elemento" no arquivo `arquivo.xml` e imprime seus valores.

## Examples
### Exemplo 1: Selecionar e exibir elementos
Suponha que você tenha um arquivo XML chamado `dados.xml` com o seguinte conteúdo:

```xml
<root>
    <item>
        <name>Item 1</name>
        <value>10</value>
    </item>
    <item>
        <name>Item 2</name>
        <value>20</value>
    </item>
</root>
```

Para selecionar e exibir todos os nomes dos itens, você pode usar o seguinte comando:

```bash
xmlstarlet sel -t -m "//item/name" -v "." -n dados.xml
```

Saída esperada:
```
Item 1
Item 2
```

### Exemplo 2: Editar um elemento
Para modificar o valor de um elemento no mesmo arquivo `dados.xml`, você pode usar o comando `ed`:

```bash
xmlstarlet ed -u "//item[name='Item 1']/value" -v "15" dados.xml
```

Este comando atualiza o valor do primeiro item para 15.

## Tips
- Utilize a opção `-h` ou `--help` para obter uma lista completa de comandos e opções disponíveis no `xmlstarlet`.
- Sempre faça um backup do seu arquivo XML antes de realizar operações de edição, para evitar perda de dados.
- Experimente usar `xmlstarlet` em combinação com outros comandos do Bash para criar scripts mais complexos e automatizados.
- Para validar um arquivo XML, utilize o comando `xmlstarlet val -e arquivo.xsd arquivo.xml` para verificar se o XML está em conformidade com um esquema específico.

Com essas informações, você deve estar apto a utilizar o `xmlstarlet` para manipular arquivos XML de maneira eficaz em seus projetos.