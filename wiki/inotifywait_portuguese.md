# [Linux] Bash inotifywait Uso: Monitora alterações em arquivos e diretórios

## Overview
O comando `inotifywait` é uma ferramenta poderosa no Linux que permite monitorar alterações em arquivos e diretórios em tempo real. Ele utiliza o sistema de notificação inotify do kernel Linux para detectar eventos como criação, modificação ou exclusão de arquivos.

## Usage
A sintaxe básica do comando `inotifywait` é a seguinte:

```bash
inotifywait [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `inotifywait`:

- `-m`: Modo de monitoramento contínuo. O comando continuará rodando e monitorando as alterações.
- `-r`: Monitora diretórios de forma recursiva, incluindo subdiretórios.
- `-e`: Especifica quais eventos você deseja monitorar (por exemplo, `modify`, `create`, `delete`).
- `--format`: Permite personalizar a saída do comando.
- `-q`: Modo silencioso, reduz a quantidade de saída.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `inotifywait`:

1. **Monitorar um diretório para alterações:**

```bash
inotifywait -m /caminho/para/diretorio
```

2. **Monitorar um diretório recursivamente para criação de arquivos:**

```bash
inotifywait -mr -e create /caminho/para/diretorio
```

3. **Monitorar um arquivo específico para modificações:**

```bash
inotifywait -e modify /caminho/para/arquivo.txt
```

4. **Usar formato personalizado para a saída:**

```bash
inotifywait -m -e modify --format '%w%f %e' /caminho/para/diretorio
```

5. **Monitorar múltiplos eventos:**

```bash
inotifywait -m -e create -e delete /caminho/para/diretorio
```

## Tips
- Utilize o modo `-m` para manter o comando ativo e monitorando continuamente, especialmente útil para scripts de automação.
- Combine o `inotifywait` com outros comandos usando pipes para criar soluções mais robustas, como fazer backup automático de arquivos modificados.
- Teste suas configurações em um diretório de teste antes de aplicá-las em ambientes de produção para evitar perda de dados.