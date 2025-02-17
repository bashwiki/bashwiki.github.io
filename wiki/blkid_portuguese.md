# [Linux] Bash blkid Uso: Identificar dispositivos de armazenamento

## Overview
O comando `blkid` é utilizado para localizar e exibir informações sobre dispositivos de bloco no sistema, como partições de disco e sistemas de arquivos. Ele fornece detalhes como UUID, tipo de sistema de arquivos e rótulos, facilitando a identificação e o gerenciamento de dispositivos de armazenamento.

## Usage
A sintaxe básica do comando `blkid` é a seguinte:

```bash
blkid [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `blkid`:

- `-o, --output`: Especifica o formato de saída (por exemplo, `value`, `full`, `udev`).
- `-s, --match-tag`: Filtra a saída para mostrar apenas as tags especificadas.
- `-p, --probe`: Força a leitura do dispositivo para obter informações.
- `-c, --cache`: Usa um arquivo de cache para armazenar informações de dispositivos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `blkid`:

1. **Listar todos os dispositivos de bloco:**
   ```bash
   blkid
   ```

2. **Exibir informações em um formato específico (por exemplo, apenas UUIDs):**
   ```bash
   blkid -o value -s UUID
   ```

3. **Filtrar a saída para mostrar apenas o tipo de sistema de arquivos:**
   ```bash
   blkid -o value -s TYPE
   ```

4. **Forçar a leitura de um dispositivo específico:**
   ```bash
   blkid /dev/sda1 -p
   ```

5. **Usar um arquivo de cache para acelerar a consulta:**
   ```bash
   blkid -c /etc/blkid.tab
   ```

## Tips
- Sempre verifique as permissões do usuário, pois algumas informações podem exigir privilégios de superusuário.
- Utilize a opção `-o` para personalizar a saída e facilitar a leitura dos resultados.
- Mantenha o arquivo de cache atualizado para melhorar o desempenho em consultas frequentes.