# [Linux] Bash hostname uso: Exibir e configurar o nome do host

## Overview
O comando `hostname` é utilizado para exibir ou configurar o nome do host de um sistema Linux. O nome do host é um identificador único que permite que o sistema seja reconhecido em uma rede.

## Usage
A sintaxe básica do comando `hostname` é a seguinte:

```bash
hostname [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `hostname`:

- `-s`: Exibe apenas o nome curto do host.
- `-f`: Exibe o nome completo do host (FQDN).
- `-i`: Exibe o endereço IP do host.
- `-A`: Exibe todos os nomes do host associados ao sistema.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `hostname`:

1. **Exibir o nome do host atual:**
   ```bash
   hostname
   ```

2. **Exibir o nome curto do host:**
   ```bash
   hostname -s
   ```

3. **Exibir o nome completo do host:**
   ```bash
   hostname -f
   ```

4. **Exibir o endereço IP do host:**
   ```bash
   hostname -i
   ```

5. **Definir um novo nome para o host:**
   ```bash
   sudo hostname novo-nome
   ```

## Tips
- Sempre utilize `sudo` ao alterar o nome do host para garantir que você tenha as permissões necessárias.
- Após alterar o nome do host, pode ser necessário reiniciar o sistema ou reiniciar serviços de rede para que as alterações tenham efeito.
- Verifique o arquivo `/etc/hostname` para garantir que o novo nome do host persista após reinicializações.