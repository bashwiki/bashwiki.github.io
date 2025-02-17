# [Linux] Bash uuidgen Uso: Geração de identificadores únicos

## Overview
O comando `uuidgen` é utilizado para gerar identificadores únicos universais (UUIDs). Esses identificadores são frequentemente usados em sistemas de computação para garantir que cada valor gerado seja único, o que é essencial para a identificação de objetos em bancos de dados, sistemas de arquivos e redes.

## Usage
A sintaxe básica do comando `uuidgen` é a seguinte:

```bash
uuidgen [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `uuidgen`:

- `-r`, `--random`: Gera um UUID baseado em números aleatórios.
- `-v`, `--version`: Especifica a versão do UUID a ser gerada (ex: 1, 3, 4, 5).
- `-h`, `--help`: Exibe a ajuda sobre o uso do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `uuidgen`:

1. **Gerar um UUID padrão:**
   ```bash
   uuidgen
   ```

2. **Gerar um UUID aleatório:**
   ```bash
   uuidgen -r
   ```

3. **Gerar um UUID da versão 4:**
   ```bash
   uuidgen -v 4
   ```

4. **Gerar múltiplos UUIDs:**
   ```bash
   for i in {1..5}; do uuidgen; done
   ```

## Tips
- Utilize o `uuidgen` em scripts para garantir que cada execução gere identificadores únicos, evitando conflitos.
- Considere a versão do UUID que você precisa; por exemplo, UUIDs da versão 4 são frequentemente usados para aplicações que requerem aleatoriedade.
- Armazene UUIDs em bancos de dados como chaves primárias para garantir a unicidade em registros.