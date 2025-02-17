# [Linux] Bash podman uso: Gerenciar contêineres sem daemon

## Overview
O comando `podman` é uma ferramenta de gerenciamento de contêineres que permite criar, executar e gerenciar contêineres de forma semelhante ao Docker, mas sem a necessidade de um daemon em execução. Ele é projetado para ser seguro e fácil de usar, permitindo que os usuários executem contêineres em ambientes de desenvolvimento e produção.

## Usage
A sintaxe básica do comando `podman` é a seguinte:

```bash
podman [options] [arguments]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `podman`:

- `run`: Executa um novo contêiner.
- `ps`: Lista os contêineres em execução.
- `images`: Lista as imagens disponíveis localmente.
- `pull`: Baixa uma imagem de um repositório remoto.
- `rm`: Remove um ou mais contêineres.
- `rmi`: Remove uma ou mais imagens.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `podman`:

1. **Executar um novo contêiner:**
   ```bash
   podman run -d --name meu-contêiner nginx
   ```
   Este comando executa um contêiner em segundo plano com o nome "meu-contêiner" usando a imagem do Nginx.

2. **Listar contêineres em execução:**
   ```bash
   podman ps
   ```
   Este comando exibe todos os contêineres que estão atualmente em execução.

3. **Baixar uma imagem:**
   ```bash
   podman pull alpine
   ```
   Este comando baixa a imagem "alpine" do repositório padrão.

4. **Remover um contêiner:**
   ```bash
   podman rm meu-contêiner
   ```
   Este comando remove o contêiner chamado "meu-contêiner".

5. **Remover uma imagem:**
   ```bash
   podman rmi alpine
   ```
   Este comando remove a imagem "alpine" do sistema.

## Tips
- Sempre verifique os contêineres em execução com `podman ps` antes de tentar removê-los.
- Use `podman logs [nome ou ID do contêiner]` para visualizar os logs de um contêiner específico.
- Considere usar `podman-compose` para gerenciar múltiplos contêineres de forma mais fácil, especialmente em ambientes de desenvolvimento.