# [Linux] Bash umask Uso: Define permissões padrão de arquivos e diretórios

## Overview
O comando `umask` é utilizado para definir as permissões padrão de arquivos e diretórios criados em um sistema Linux. Ele determina quais permissões serão negadas por padrão quando novos arquivos ou diretórios são criados.

## Usage
A sintaxe básica do comando `umask` é a seguinte:

```bash
umask [opções] [máscara]
```

## Common Options
- **-S**: Exibe a máscara de forma simbólica, em vez de numérica.
- **-p**: Exibe a máscara atual em um formato que pode ser usado em um script.

## Common Examples

### Exibir a máscara atual
Para verificar a máscara de permissões atual:

```bash
umask
```

### Definir uma nova máscara
Para definir uma nova máscara, por exemplo, 022 (onde os arquivos criados terão permissões 644 e diretórios 755):

```bash
umask 022
```

### Usar a opção simbólica
Para exibir a máscara atual em formato simbólico:

```bash
umask -S
```

### Definir uma máscara simbólica
Para definir uma máscara usando notação simbólica, como remover permissões de escrita para o grupo e outros:

```bash
umask u=rwx,g=rx,o=rx
```

## Tips
- Lembre-se de que a máscara `umask` é aplicada apenas a novos arquivos e diretórios criados após sua definição.
- Para tornar a configuração da máscara persistente entre sessões, adicione o comando `umask` ao seu arquivo de inicialização do shell, como `~/.bashrc`.
- Teste as permissões após definir a máscara criando um arquivo ou diretório e verificando suas permissões com `ls -l`.