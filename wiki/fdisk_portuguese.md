# [Linux] Bash fdisk Uso: Gerenciar partições de disco

## Overview
O comando `fdisk` é uma ferramenta de linha de comando utilizada para criar, excluir e gerenciar partições em discos rígidos e dispositivos de armazenamento. Ele é especialmente útil para usuários que precisam configurar partições em sistemas Linux.

## Usage
A sintaxe básica do comando `fdisk` é a seguinte:

```bash
fdisk [opções] [dispositivo]
```

Onde `[dispositivo]` é o caminho para o dispositivo que você deseja manipular, como `/dev/sda`.

## Common Options
Aqui estão algumas opções comuns do `fdisk`:

- `-l`: Lista todas as partições em todos os dispositivos.
- `-u`: Usa setores como unidades de medida em vez de cilindros.
- `-v`: Exibe a versão do `fdisk`.
- `-s`: Exibe o tamanho de uma partição específica.

## Common Examples

### Listar Partições
Para listar todas as partições em todos os dispositivos, você pode usar:

```bash
fdisk -l
```

### Criar uma Nova Partição
Para criar uma nova partição em um dispositivo específico, inicie o `fdisk` com o dispositivo desejado:

```bash
fdisk /dev/sda
```
Depois, siga as instruções interativas para criar uma nova partição.

### Excluir uma Partição
Para excluir uma partição, inicie o `fdisk` como mostrado acima e, em seguida, use o comando `d` para deletar a partição desejada.

### Verificar o Tamanho de uma Partição
Para verificar o tamanho de uma partição específica, você pode usar:

```bash
fdisk -s /dev/sda1
```

## Tips
- Sempre faça backup dos seus dados antes de modificar partições, pois alterações podem resultar em perda de dados.
- Use o comando `man fdisk` para acessar o manual e obter mais informações sobre as opções disponíveis.
- Após fazer alterações nas partições, pode ser necessário reiniciar o sistema para que as mudanças tenham efeito.