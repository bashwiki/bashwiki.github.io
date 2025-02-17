# [Linux] Bash git uso: Controle de versões de código

## Overview
O comando `git` é uma ferramenta de controle de versões amplamente utilizada para gerenciar projetos de desenvolvimento de software. Ele permite que os desenvolvedores rastreiem alterações no código, colaborem com outras pessoas e mantenham um histórico completo do projeto.

## Usage
A sintaxe básica do comando `git` é a seguinte:

```bash
git [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `git`:

- `git init`: Inicializa um novo repositório Git.
- `git clone [url]`: Clona um repositório remoto para o seu sistema local.
- `git add [arquivo]`: Adiciona arquivos ao índice para serem incluídos no próximo commit.
- `git commit -m "[mensagem]"`: Registra as alterações no repositório com uma mensagem descritiva.
- `git status`: Mostra o estado atual do repositório, incluindo arquivos modificados e não rastreados.
- `git push`: Envia as alterações locais para um repositório remoto.
- `git pull`: Atualiza o repositório local com as alterações do repositório remoto.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `git`:

1. **Inicializar um novo repositório:**
   ```bash
   git init meu-projeto
   ```

2. **Clonar um repositório remoto:**
   ```bash
   git clone https://github.com/usuario/repo.git
   ```

3. **Adicionar um arquivo ao índice:**
   ```bash
   git add arquivo.txt
   ```

4. **Fazer um commit das alterações:**
   ```bash
   git commit -m "Adiciona novo recurso"
   ```

5. **Verificar o estado do repositório:**
   ```bash
   git status
   ```

6. **Enviar alterações para o repositório remoto:**
   ```bash
   git push origin main
   ```

7. **Atualizar o repositório local com alterações remotas:**
   ```bash
   git pull origin main
   ```

## Tips
- Sempre escreva mensagens de commit claras e descritivas para facilitar o entendimento do histórico do projeto.
- Use branches para desenvolver novos recursos ou corrigir bugs sem afetar a versão principal do código.
- Realize commits frequentes para manter um histórico detalhado das alterações e facilitar o rastreamento de problemas.
- Não esqueça de fazer `git pull` antes de começar a trabalhar para garantir que você esteja sempre atualizado com as alterações mais recentes do repositório remoto.