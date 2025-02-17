# [Linux] Bash docker uso: Gerenciamento de contêineres

## Overview
O comando `docker` é utilizado para gerenciar contêineres, que são ambientes isolados que permitem executar aplicações de forma eficiente e consistente. Com o Docker, é possível criar, executar, parar e gerenciar contêineres de maneira simples.

## Usage
A sintaxe básica do comando `docker` é a seguinte:

```bash
docker [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `docker`:

- `run`: Cria e inicia um novo contêiner.
- `ps`: Lista os contêineres em execução.
- `stop`: Para um ou mais contêineres em execução.
- `rm`: Remove um ou mais contêineres.
- `images`: Lista as imagens disponíveis no sistema.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `docker`:

1. **Iniciar um novo contêiner**:
   ```bash
   docker run -d --name meu_contêiner nginx
   ```
   Este comando inicia um contêiner em segundo plano com o nome "meu_contêiner" usando a imagem do Nginx.

2. **Listar contêineres em execução**:
   ```bash
   docker ps
   ```
   Este comando exibe todos os contêineres que estão atualmente em execução.

3. **Parar um contêiner**:
   ```bash
   docker stop meu_contêiner
   ```
   Este comando para o contêiner chamado "meu_contêiner".

4. **Remover um contêiner**:
   ```bash
   docker rm meu_contêiner
   ```
   Este comando remove o contêiner "meu_contêiner" do sistema.

5. **Listar imagens disponíveis**:
   ```bash
   docker images
   ```
   Este comando mostra todas as imagens que estão disponíveis no seu sistema Docker.

## Tips
- Sempre verifique se o Docker está em execução antes de usar os comandos.
- Utilize `docker-compose` para gerenciar aplicações que consistem em múltiplos contêineres.
- Mantenha suas imagens e contêineres organizados, removendo aqueles que não são mais necessários com `docker rm` e `docker rmi`.
- Explore a documentação oficial do Docker para entender melhor as opções avançadas e os melhores padrões de uso.