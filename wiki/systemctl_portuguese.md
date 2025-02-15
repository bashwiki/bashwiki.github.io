# [리눅스] Bash systemctl 사용법

## Overview
O `systemctl` é uma ferramenta de linha de comando utilizada para interagir com o sistema de gerenciamento de serviços `systemd`, que é o sistema de inicialização padrão em muitas distribuições Linux modernas. O principal objetivo do `systemctl` é permitir que os usuários iniciem, parem, reiniciem e gerenciem serviços e unidades do sistema, além de fornecer informações sobre o estado atual dos serviços.

## Usage
A sintaxe básica do comando `systemctl` é a seguinte:

```bash
systemctl [opções] [comando] [nome_da_unidade]
```

### Comandos Comuns
- `start`: Inicia uma unidade (serviço).
- `stop`: Para uma unidade.
- `restart`: Reinicia uma unidade.
- `status`: Mostra o status de uma unidade.
- `enable`: Habilita uma unidade para iniciar automaticamente na inicialização.
- `disable`: Desabilita uma unidade para não iniciar automaticamente na inicialização.
- `list-units`: Lista todas as unidades carregadas.

### Opções Comuns
- `--quiet`: Suprime mensagens de saída.
- `--now`: Aplica o comando tanto à unidade quanto a suas dependências.

## Examples
### Exemplo 1: Iniciar um Serviço
Para iniciar um serviço chamado `nginx`, você pode usar o seguinte comando:

```bash
sudo systemctl start nginx
```

### Exemplo 2: Verificar o Status de um Serviço
Para verificar o status do serviço `nginx`, utilize:

```bash
systemctl status nginx
```

Isso fornecerá informações detalhadas sobre o estado do serviço, incluindo se ele está ativo, inativo ou falhou.

## Tips
- Sempre utilize `sudo` ao executar comandos que alteram o estado dos serviços, pois muitas operações requerem permissões de superusuário.
- Use `systemctl list-units --type=service` para obter uma visão geral de todos os serviços em execução e seus estados.
- Para garantir que um serviço inicie automaticamente na inicialização do sistema, não se esqueça de usar o comando `enable` após iniciar o serviço.
- Utilize `systemctl daemon-reload` após modificar arquivos de configuração de unidades para que as alterações sejam reconhecidas pelo `systemd`.