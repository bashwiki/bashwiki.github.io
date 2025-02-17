# [Linux] Bash yes uso equivalente: Gera uma sequência contínua de uma string

## Overview
O comando `yes` é uma ferramenta simples que gera uma sequência contínua de uma string, que por padrão é a palavra "y". Ele é frequentemente utilizado para automatizar a resposta a prompts de confirmação em scripts ou comandos que requerem uma entrada do usuário.

## Usage
A sintaxe básica do comando `yes` é a seguinte:

```bash
yes [opções] [argumentos]
```

## Common Options
- `-h`, `--help`: Exibe a ajuda e sai.
- `-V`, `--version`: Mostra a versão do comando e sai.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `yes`:

1. **Gerar uma sequência de "y":**
   ```bash
   yes
   ```
   Este comando irá gerar uma sequência infinita de "y".

2. **Gerar uma sequência de uma string personalizada:**
   ```bash
   yes "Sim"
   ```
   Isso irá gerar uma sequência infinita de "Sim".

3. **Usar yes para automatizar um comando:**
   ```bash
   yes | rm -i arquivo.txt
   ```
   Neste exemplo, `yes` é usado para responder "y" a todos os prompts de confirmação do comando `rm`.

4. **Limitar a saída usando head:**
   ```bash
   yes | head -n 5
   ```
   Este comando irá gerar apenas as primeiras 5 linhas de "y".

## Tips
- Use `yes` com cautela, especialmente em comandos destrutivos, pois ele pode confirmar automaticamente ações sem que você tenha a chance de revisar.
- Combine `yes` com outros comandos para automatizar tarefas que requerem confirmação, economizando tempo e esforço.
- Para interromper a execução do `yes`, você pode usar `Ctrl + C`.