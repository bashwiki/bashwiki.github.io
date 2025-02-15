# [리눅스] Bash tune2fs 사용법

## Overview
O comando `tune2fs` é uma ferramenta utilizada para ajustar parâmetros de sistemas de arquivos ext2, ext3 e ext4 no Linux. Ele permite que os usuários modifiquem várias opções do sistema de arquivos, como o número máximo de montagens antes da verificação, a frequência de verificação e outras configurações que podem otimizar o desempenho e a integridade do sistema de arquivos.

## Usage
A sintaxe básica do comando `tune2fs` é a seguinte:

```bash
tune2fs [opções] dispositivo
```

### Opções Comuns:
- `-c <número>`: Define o número máximo de montagens antes que o sistema de arquivos seja verificado.
- `-i <intervalo>`: Define o intervalo entre verificações, que pode ser especificado em dias, semanas ou meses.
- `-m <porcentagem>`: Define a porcentagem de espaço reservado para o usuário root.
- `-O <opções>`: Ativa as opções de recursos do sistema de arquivos.
- `-L <rótulo>`: Altera o rótulo do sistema de arquivos.
- `-e <opções>`: Define o comportamento em caso de erro.

## Examples
### Exemplo 1: Definir o número máximo de montagens
Para definir o número máximo de montagens antes da verificação para 20, você pode usar o seguinte comando:

```bash
sudo tune2fs -c 20 /dev/sda1
```

### Exemplo 2: Alterar o intervalo de verificação
Para definir o intervalo de verificação do sistema de arquivos para 30 dias, utilize o comando abaixo:

```bash
sudo tune2fs -i 30d /dev/sda1
```

## Tips
- Sempre faça um backup dos dados antes de modificar as configurações do sistema de arquivos.
- Utilize o comando `tune2fs -l <dispositivo>` para listar as configurações atuais do sistema de arquivos antes de fazer alterações.
- É recomendável executar `tune2fs` em um sistema de arquivos desmontado para evitar corrupção de dados.
- Verifique a documentação do `tune2fs` com `man tune2fs` para obter uma lista completa de opções e detalhes adicionais.