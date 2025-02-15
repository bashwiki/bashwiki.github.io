# [리눅스] Bash podman 사용법

## Overview
O `podman` é uma ferramenta de gerenciamento de contêineres que permite aos usuários criar, executar e gerenciar contêineres e imagens de contêineres. Ele é projetado para ser uma alternativa leve ao Docker, oferecendo uma interface semelhante, mas sem a necessidade de um daemon em execução. O `podman` é especialmente útil para desenvolvedores e engenheiros que trabalham com aplicações em contêineres, pois permite a execução de contêineres de forma simples e eficiente, além de suportar a criação de pods, que são grupos de um ou mais contêineres que compartilham recursos.

## Usage
A sintaxe básica do comando `podman` é a seguinte:

```bash
podman [opções] comando [argumentos]
```

Algumas opções comuns incluem:

- `--help`: Mostra a ajuda sobre o comando.
- `--version`: Exibe a versão do Podman instalada.
- `-d`, `--detach`: Executa o contêiner em segundo plano.
- `--rm`: Remove o contêiner após a sua parada.
- `-it`: Executa o contêiner em modo interativo, permitindo acesso ao terminal.

## Examples
### Exemplo 1: Executando um contêiner simples
Para executar um contêiner do Nginx em segundo plano, você pode usar o seguinte comando:

```bash
podman run -d --name meu-nginx -p 8080:80 nginx
```
Neste exemplo, o `podman` baixa a imagem do Nginx, cria um contêiner chamado "meu-nginx" e o executa em segundo plano, mapeando a porta 80 do contêiner para a porta 8080 do host.

### Exemplo 2: Listando contêineres em execução
Para listar todos os contêineres em execução, utilize o comando:

```bash
podman ps
```
Este comando exibirá uma lista de contêineres ativos, incluindo informações como ID, nome, status e portas.

## Tips
- Utilize `podman-compose` se você estiver trabalhando com múltiplos contêineres e quiser orquestrá-los facilmente, semelhante ao `docker-compose`.
- Sempre verifique as imagens disponíveis localmente com `podman images` antes de tentar executar um contêiner, para evitar downloads desnecessários.
- Para depuração, você pode usar `podman logs <nome ou ID do contêiner>` para visualizar os logs de um contêiner específico.
- Considere usar `podman network` para gerenciar redes de contêineres, permitindo comunicação entre eles de forma mais eficiente.