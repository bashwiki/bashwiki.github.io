# [Linux] Bash export uso: Define variáveis de ambiente

## Overview
O comando `export` no Bash é utilizado para definir variáveis de ambiente, tornando-as disponíveis para processos filhos. Isso é útil quando você deseja que uma variável seja acessível em diferentes partes de um script ou em outros programas que você executa a partir do terminal.

## Usage
A sintaxe básica do comando `export` é a seguinte:

```bash
export [opções] [variável=valor]
```

## Common Options
- `-n`: Remove a variável do ambiente exportado.
- `-p`: Exibe todas as variáveis de ambiente exportadas.

## Common Examples

### Exemplo 1: Definindo uma variável de ambiente
```bash
export MY_VAR="Hello, World!"
```
Neste exemplo, a variável `MY_VAR` é definida e exportada, tornando-se acessível em processos filhos.

### Exemplo 2: Verificando uma variável de ambiente
```bash
echo $MY_VAR
```
Isso exibirá `Hello, World!`, mostrando que a variável foi definida corretamente.

### Exemplo 3: Removendo uma variável do ambiente exportado
```bash
export -n MY_VAR
```
Este comando remove `MY_VAR` do ambiente exportado, tornando-a inacessível para processos filhos.

### Exemplo 4: Exportando múltiplas variáveis
```bash
export VAR1="Value1" VAR2="Value2"
```
Aqui, ambas as variáveis `VAR1` e `VAR2` são definidas e exportadas ao mesmo tempo.

### Exemplo 5: Listando variáveis de ambiente exportadas
```bash
export -p
```
Este comando lista todas as variáveis de ambiente que foram exportadas.

## Tips
- Sempre use aspas ao definir variáveis que contêm espaços para evitar erros.
- Lembre-se de que as variáveis exportadas só estão disponíveis para processos filhos, e não para o shell atual.
- Para tornar as variáveis permanentes, você pode adicioná-las ao seu arquivo de configuração do shell, como `~/.bashrc` ou `~/.bash_profile`.