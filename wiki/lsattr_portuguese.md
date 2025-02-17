# [Linux] Bash lsattr Uso: Exibir atributos de arquivos

## Overview
O comando `lsattr` é utilizado para listar os atributos de arquivos em sistemas de arquivos Linux. Esses atributos podem controlar o comportamento dos arquivos, como se eles podem ser modificados, excluídos ou renomeados.

## Usage
A sintaxe básica do comando `lsattr` é a seguinte:

```bash
lsattr [opções] [arquivos]
```

## Common Options
Aqui estão algumas opções comuns do `lsattr`:

- `-a`: Exibe todos os arquivos, incluindo os ocultos.
- `-d`: Exibe atributos de diretórios em vez de arquivos.
- `-R`: Realiza a busca recursiva em diretórios.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `lsattr`:

1. **Listar atributos de arquivos em um diretório:**
   ```bash
   lsattr /caminho/para/diretorio
   ```

2. **Listar atributos de arquivos, incluindo ocultos:**
   ```bash
   lsattr -a /caminho/para/diretorio
   ```

3. **Listar atributos de um diretório específico:**
   ```bash
   lsattr -d /caminho/para/diretorio
   ```

4. **Listar atributos de arquivos recursivamente:**
   ```bash
   lsattr -R /caminho/para/diretorio
   ```

## Tips
- Sempre verifique os atributos de arquivos críticos antes de realizar operações de modificação, pois atributos como `i` (imutável) podem impedir alterações.
- Use `lsattr` em conjunto com `chattr` para modificar atributos de arquivos, garantindo que você tenha as permissões necessárias.
- Familiarize-se com os diferentes atributos disponíveis, pois eles podem ajudar a proteger arquivos importantes contra exclusões acidentais.