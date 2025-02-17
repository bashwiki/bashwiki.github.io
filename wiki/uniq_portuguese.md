# [Linux] Bash uniq Uso: Remove linhas duplicadas de um arquivo

## Overview
O comando `uniq` é utilizado para filtrar linhas duplicadas em um arquivo ou na entrada padrão. Ele é frequentemente usado em conjunto com o comando `sort`, pois o `uniq` apenas remove duplicatas que estão adjacentes.

## Usage
A sintaxe básica do comando `uniq` é a seguinte:

```bash
uniq [opções] [arquivo]
```

## Common Options
Aqui estão algumas opções comuns do comando `uniq`:

- `-c`: Conta o número de ocorrências de cada linha.
- `-d`: Exibe apenas as linhas duplicadas.
- `-u`: Exibe apenas as linhas únicas.
- `-i`: Ignora diferenças entre maiúsculas e minúsculas.

## Common Examples

### Remover linhas duplicadas de um arquivo
```bash
uniq arquivo.txt
```

### Contar ocorrências de cada linha
```bash
uniq -c arquivo.txt
```

### Exibir apenas linhas duplicadas
```bash
uniq -d arquivo.txt
```

### Exibir apenas linhas únicas
```bash
uniq -u arquivo.txt
```

### Usar com sort para remover duplicatas não adjacentes
```bash
sort arquivo.txt | uniq
```

## Tips
- Sempre use `sort` antes de `uniq` se você quiser remover todas as duplicatas, não apenas as adjacentes.
- Combine `uniq` com redirecionamento para salvar a saída em um novo arquivo: 
  ```bash
  sort arquivo.txt | uniq > arquivo_unico.txt
  ```
- Utilize a opção `-i` se você estiver lidando com dados que podem ter variações de capitalização.