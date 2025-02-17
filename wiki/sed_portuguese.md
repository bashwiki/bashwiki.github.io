# [Linux] Bash sed Uso equivalente: Editar texto em arquivos

## Overview
O comando `sed` (Stream Editor) é uma ferramenta poderosa para manipulação de texto em arquivos e streams. Ele permite realizar operações como substituição, inserção e exclusão de texto de forma não interativa, o que o torna ideal para automação de tarefas de edição de texto.

## Usage
A sintaxe básica do comando `sed` é a seguinte:

```bash
sed [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `sed`:

- `-e`: Permite adicionar múltiplas expressões de edição.
- `-i`: Edita os arquivos no local, ou seja, faz as alterações diretamente nos arquivos.
- `-n`: Supressão da saída padrão, útil quando você deseja apenas imprimir linhas específicas.
- `s/padrão/substituição/`: Realiza uma substituição de texto, onde "padrão" é o texto a ser encontrado e "substituição" é o texto que irá substituí-lo.

## Common Examples

### Substituir texto em um arquivo
Para substituir a palavra "antigo" por "novo" em um arquivo chamado `exemplo.txt`, você pode usar:

```bash
sed -i 's/antigo/novo/g' exemplo.txt
```

### Exibir linhas específicas
Para exibir apenas as linhas que contêm a palavra "erro" em um arquivo:

```bash
sed -n '/erro/p' exemplo.txt
```

### Remover linhas vazias
Para remover todas as linhas vazias de um arquivo:

```bash
sed -i '/^$/d' exemplo.txt
```

### Adicionar texto antes de uma linha
Para adicionar a palavra "Início:" antes de cada linha que contém "exemplo":

```bash
sed -i '/exemplo/i Início:' exemplo.txt
```

## Tips
- Sempre faça um backup dos seus arquivos antes de usar a opção `-i`, pois as alterações são irreversíveis.
- Use `sed` em combinação com outros comandos, como `grep`, para filtrar e processar dados de forma mais eficaz.
- Teste suas expressões `sed` sem a opção `-i` primeiro para garantir que o resultado seja o esperado antes de aplicar as mudanças diretamente no arquivo.