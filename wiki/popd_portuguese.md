# [Linux] Bash popd Uso: Remove o diretório do topo da pilha

## Overview
O comando `popd` é utilizado para remover o diretório do topo da pilha de diretórios, permitindo que você retorne rapidamente ao diretório anterior que foi armazenado com o comando `pushd`. É uma maneira eficiente de navegar entre diretórios sem precisar digitar o caminho completo.

## Usage
A sintaxe básica do comando `popd` é a seguinte:

```bash
popd [opções] [argumentos]
```

## Common Options
- `+n`: Remove o diretório na posição `n` da pilha, onde `n` é um número que representa a posição do diretório.
- `-n`: Remove o diretório na posição `n` da pilha, mas conta de trás para frente.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `popd`:

1. **Remover o diretório do topo da pilha:**
   ```bash
   popd
   ```

2. **Remover o segundo diretório da pilha:**
   ```bash
   popd +1
   ```

3. **Remover o diretório na posição 0 da pilha (primeiro diretório adicionado):**
   ```bash
   popd -0
   ```

4. **Usando `pushd` e `popd` juntos:**
   ```bash
   pushd /home/usuario
   pushd /var/log
   popd  # Retorna para /home/usuario
   ```

## Tips
- Utilize `pushd` antes de `popd` para maximizar a eficiência na navegação entre diretórios.
- Verifique a pilha de diretórios atual com o comando `dirs` antes de usar `popd`, para saber quais diretórios estão disponíveis.
- Lembre-se de que `popd` só funcionará se houver diretórios na pilha; caso contrário, você receberá uma mensagem de erro.