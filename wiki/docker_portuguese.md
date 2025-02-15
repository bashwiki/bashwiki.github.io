# [리눅스] Bash docker 사용법

## Overview
O comando `docker` é uma ferramenta de linha de comando que permite aos desenvolvedores e engenheiros gerenciar contêineres e imagens Docker. O Docker é uma plataforma que facilita a criação, o envio e a execução de aplicativos em contêineres, que são ambientes isolados que incluem tudo o que um aplicativo precisa para funcionar. O principal propósito do comando `docker` é interagir com o daemon do Docker, permitindo que os usuários realizem operações como criar, iniciar, parar e remover contêineres e imagens.

## Usage
A sintaxe básica do comando `docker` é a seguinte:

```
docker [OPTIONS] COMMAND [ARG...]
```

### Comandos Comuns
- `docker run`: Cria e inicia um novo contêiner a partir de uma imagem.
- `docker ps`: Lista os contêineres em execução.
- `docker images`: Lista as imagens disponíveis localmente.
- `docker stop`: Para um ou mais contêineres em execução.
- `docker rm`: Remove um ou mais contêineres.

### Opções Comuns
- `-d`: Executa o contêiner em segundo plano (modo desacoplado).
- `--name`: Atribui um nome ao contêiner.
- `-p`: Mapeia portas do contêiner para a máquina host.

## Examples
### Exemplo 1: Executando um contêiner Nginx
Para executar um contêiner Nginx em segundo plano e mapear a porta 80 do contêiner para a porta 8080 da máquina host, você pode usar o seguinte comando:

```bash
docker run -d --name meu-nginx -p 8080:80 nginx
```

### Exemplo 2: Listando contêineres em execução
Para listar todos os contêineres que estão atualmente em execução, você pode usar:

```bash
docker ps
```

## Tips
- Sempre verifique se o daemon do Docker está em execução antes de usar o comando `docker`.
- Utilize `docker-compose` para gerenciar múltiplos contêineres de forma mais fácil e eficiente.
- Mantenha suas imagens e contêineres organizados, removendo aqueles que não são mais necessários com `docker rm` e `docker rmi`.
- Consulte a documentação oficial do Docker para obter informações detalhadas sobre opções e melhores práticas.