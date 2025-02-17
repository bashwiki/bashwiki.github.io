# [Linux] Bash egrep uso equivalente: busca avançada de padrões em texto

## Overview
O comando `egrep` é uma versão do comando `grep` que permite a busca de padrões em arquivos de texto utilizando expressões regulares estendidas. Ele é especialmente útil para encontrar linhas que correspondem a padrões complexos.

## Usage
A sintaxe básica do comando `egrep` é a seguinte:

```bash
egrep [opções] [padrão] [arquivo]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `egrep`:

- `-i`: Ignora a distinção entre maiúsculas e minúsculas.
- `-v`: Inverte a correspondência, ou seja, retorna linhas que não correspondem ao padrão.
- `-c`: Conta o número de linhas que correspondem ao padrão.
- `-n`: Mostra o número da linha onde a correspondência foi encontrada.
- `-r`: Busca recursivamente em diretórios.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `egrep`:

1. **Buscar um padrão em um arquivo:**
   ```bash
   egrep "erro" log.txt
   ```

2. **Buscar um padrão sem considerar maiúsculas e minúsculas:**
   ```bash
   egrep -i "aviso" log.txt
   ```

3. **Contar o número de linhas que correspondem a um padrão:**
   ```bash
   egrep -c "sucesso" log.txt
   ```

4. **Buscar linhas que não contêm um padrão:**
   ```bash
   egrep -v "debug" log.txt
   ```

5. **Buscar recursivamente por um padrão em todos os arquivos de um diretório:**
   ```bash
   egrep -r "configuração" /etc/
   ```

## Tips
- Utilize `-n` junto com `egrep` para facilitar a localização de correspondências em arquivos grandes.
- Combine `egrep` com outros comandos, como `sort` ou `uniq`, para processar melhor os resultados.
- Sempre teste suas expressões regulares em um ambiente controlado para garantir que elas correspondem exatamente ao que você espera.