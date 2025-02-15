# [리눅스] Bash umask 사용법

## Visão Geral
O comando `umask` é utilizado em sistemas Unix e Linux para definir a máscara de criação de arquivos. A máscara de criação de arquivos determina as permissões padrão que serão atribuídas a novos arquivos e diretórios criados por um usuário. O principal propósito do `umask` é controlar as permissões de acesso, garantindo que os arquivos e diretórios criados tenham as permissões adequadas desde o início.

## Uso
A sintaxe básica do comando `umask` é a seguinte:

```bash
umask [máscara]
```

### Opções Comuns
- **máscara**: Um valor octal que representa as permissões que serão removidas das permissões padrão. As permissões padrão para arquivos são 666 (rw-rw-rw-) e para diretórios são 777 (rwxrwxrwx). O valor da máscara é subtraído dessas permissões.

### Máscaras Comuns
- `022`: Permite que o proprietário tenha permissões de leitura e escrita, enquanto o grupo e outros têm apenas permissão de leitura.
- `027`: Permite que o proprietário tenha permissões de leitura e escrita, enquanto o grupo tem permissão de leitura e outros não têm nenhuma permissão.

## Exemplos
### Exemplo 1: Verificar a Máscara Atual
Para verificar a máscara de criação de arquivos atual, basta executar:

```bash
umask
```

A saída pode ser algo como `0022`, indicando que as permissões padrão para novos arquivos e diretórios serão ajustadas de acordo.

### Exemplo 2: Definir uma Nova Máscara
Para definir uma nova máscara que permita apenas ao proprietário ler e escrever, enquanto o grupo e outros não têm permissões, execute:

```bash
umask 077
```

Após executar este comando, novos arquivos criados terão permissões de `rw-------` e novos diretórios terão permissões de `rwx------`.

## Dicas
- **Persistência**: Para tornar a configuração da máscara persistente entre sessões, adicione o comando `umask` ao seu arquivo de inicialização do shell, como `~/.bashrc` ou `~/.profile`.
- **Verificação Regular**: É uma boa prática verificar a máscara de criação de arquivos antes de criar novos arquivos ou diretórios, especialmente em ambientes de produção, para garantir que as permissões estejam configuradas corretamente.
- **Cuidado com Permissões**: Evite definir uma máscara que permita permissões excessivas, pois isso pode levar a problemas de segurança, permitindo que usuários não autorizados acessem arquivos sensíveis.

O comando `umask` é uma ferramenta poderosa para gerenciar as permissões de arquivos e diretórios, e seu uso adequado pode ajudar a manter a segurança e a integridade dos dados em sistemas Unix e Linux.