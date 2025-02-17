# [Linux] Bash scp Uso: Transferência segura de arquivos entre hosts

## Overview
O comando `scp` (Secure Copy Protocol) é utilizado para transferir arquivos de forma segura entre um computador local e um remoto, ou entre dois computadores remotos. Ele utiliza o protocolo SSH para garantir que os dados sejam transferidos de forma criptografada.

## Usage
A sintaxe básica do comando `scp` é a seguinte:

```bash
scp [opções] [origem] [destino]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `scp`:

- `-r`: Copia diretórios recursivamente.
- `-P`: Especifica a porta do servidor SSH (note que é uma letra maiúscula).
- `-i`: Especifica um arquivo de chave privada para autenticação.
- `-v`: Ativa o modo verbose, mostrando detalhes da transferência.
- `-C`: Ativa a compressão durante a transferência.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `scp`:

1. **Copiar um arquivo do local para um servidor remoto:**
   ```bash
   scp arquivo.txt usuario@servidor:/caminho/destino/
   ```

2. **Copiar um arquivo de um servidor remoto para o local:**
   ```bash
   scp usuario@servidor:/caminho/origem/arquivo.txt /caminho/destino/
   ```

3. **Copiar um diretório inteiro para um servidor remoto:**
   ```bash
   scp -r /caminho/diretorio usuario@servidor:/caminho/destino/
   ```

4. **Copiar um arquivo usando uma porta SSH diferente:**
   ```bash
   scp -P 2222 arquivo.txt usuario@servidor:/caminho/destino/
   ```

5. **Usar uma chave privada para autenticação:**
   ```bash
   scp -i /caminho/para/chave_privada arquivo.txt usuario@servidor:/caminho/destino/
   ```

## Tips
- Sempre verifique as permissões dos arquivos e diretórios que você está transferindo para evitar problemas de acesso.
- Utilize a opção `-v` para depuração se encontrar problemas durante a transferência.
- Para transferências grandes, considere usar a opção `-C` para ativar a compressão e acelerar o processo.
- Mantenha suas chaves SSH seguras e utilize autenticação baseada em chave sempre que possível para aumentar a segurança.