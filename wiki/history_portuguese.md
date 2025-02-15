# [리눅스] Bash history 사용법

## Overview
O comando `history` no Bash é utilizado para exibir uma lista dos comandos que foram executados anteriormente na sessão do terminal. Ele é uma ferramenta essencial para engenheiros e desenvolvedores, pois permite revisar e reutilizar comandos sem a necessidade de reescrevê-los, aumentando a eficiência e a produtividade.

## Usage
A sintaxe básica do comando `history` é a seguinte:

```bash
history [opções] [número]
```

### Opções Comuns:
- `-c`: Limpa o histórico atual.
- `-d <n>`: Remove o comando na posição `<n>` do histórico.
- `-a`: Adiciona os comandos atuais do histórico para o arquivo de histórico.
- `-r`: Lê o histórico do arquivo e o adiciona ao histórico atual.
- `-n`: Lê novas entradas do arquivo de histórico, mas não as adiciona ao histórico atual.

## Examples
### Exemplo 1: Exibir o histórico de comandos
Para visualizar os últimos 10 comandos executados, você pode usar:

```bash
history 10
```

### Exemplo 2: Reexecutar um comando do histórico
Se você deseja reexecutar um comando específico que está na posição 5 do seu histórico, você pode usar:

```bash
!5
```

Isso executará o comando que está na linha 5 do histórico.

## Tips
- Utilize `Ctrl + R` para buscar interativamente por comandos anteriores no seu histórico, facilitando a localização de comandos específicos.
- Para evitar a poluição do histórico, considere usar `history -c` para limpar o histórico ao final de uma sessão, especialmente em ambientes sensíveis.
- Lembre-se de que o histórico é armazenado em um arquivo (geralmente `~/.bash_history`), então você pode editar esse arquivo diretamente se precisar remover ou modificar comandos antigos.