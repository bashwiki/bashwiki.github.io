# [Linux] Bash tune2fs uso: Ajusta parâmetros do sistema de arquivos ext2/ext3/ext4

## Overview
O comando `tune2fs` é utilizado para ajustar parâmetros de sistemas de arquivos ext2, ext3 e ext4 no Linux. Ele permite modificar opções de montagem e outras configurações que podem otimizar o desempenho e a integridade do sistema de arquivos.

## Usage
A sintaxe básica do comando `tune2fs` é a seguinte:

```bash
tune2fs [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `tune2fs`:

- `-c <n>`: Define o número máximo de montagens antes de uma verificação forçada do sistema de arquivos.
- `-i <intervalo>`: Define o intervalo de tempo entre verificações do sistema de arquivos.
- `-m <porcentagem>`: Define a porcentagem do sistema de arquivos reservada para o usuário root.
- `-O <opções>`: Ativa as opções especificadas para o sistema de arquivos.
- `-L <label>`: Define um novo rótulo para o sistema de arquivos.
- `-E <opções>`: Especifica opções adicionais para o sistema de arquivos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `tune2fs`:

1. **Definir o número máximo de montagens**:
   ```bash
   tune2fs -c 20 /dev/sda1
   ```

2. **Definir o intervalo de verificação para 30 dias**:
   ```bash
   tune2fs -i 30d /dev/sda1
   ```

3. **Reservar 5% do sistema de arquivos para o root**:
   ```bash
   tune2fs -m 5 /dev/sda1
   ```

4. **Adicionar uma nova opção ao sistema de arquivos**:
   ```bash
   tune2fs -O dir_index /dev/sda1
   ```

5. **Alterar o rótulo do sistema de arquivos**:
   ```bash
   tune2fs -L "MeuSistema" /dev/sda1
   ```

## Tips
- Sempre faça backup dos dados antes de usar o `tune2fs`, pois alterações indevidas podem causar perda de dados.
- Utilize o comando `tune2fs -l /dev/sda1` para listar as configurações atuais do sistema de arquivos antes de fazer alterações.
- Teste as opções em um ambiente de desenvolvimento ou em um sistema não crítico para evitar problemas em produção.