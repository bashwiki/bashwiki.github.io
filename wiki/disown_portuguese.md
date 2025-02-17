# [Linux] Bash disown Uso: Remove jobs da lista de jobs do shell

## Overview
O comando `disown` é utilizado no Bash para remover um ou mais jobs da lista de jobs do shell. Isso é útil quando você deseja que um processo continue em execução mesmo após fechar a sessão do terminal, permitindo que ele funcione em segundo plano sem ser interrompido.

## Usage
A sintaxe básica do comando `disown` é a seguinte:

```bash
disown [opções] [jobs]
```

## Common Options
- `-h`: Impede que o job especificado receba um sinal SIGHUP quando a sessão do terminal for encerrada.
- `-a`: Aplica o comando a todos os jobs em segundo plano.
- `-r`: Aplica o comando apenas aos jobs em execução.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `disown`:

1. **Remover um job específico da lista de jobs:**
   ```bash
   disown %1
   ```
   Neste exemplo, `%1` refere-se ao primeiro job em segundo plano.

2. **Remover todos os jobs da lista:**
   ```bash
   disown
   ```
   Este comando remove todos os jobs da lista de jobs do shell.

3. **Impedir que um job específico receba SIGHUP:**
   ```bash
   disown -h %2
   ```
   Aqui, `%2` é o segundo job em segundo plano, que não receberá o sinal SIGHUP.

4. **Remover todos os jobs em execução:**
   ```bash
   disown -r
   ```
   Este comando remove todos os jobs que estão atualmente em execução.

## Tips
- Sempre verifique a lista de jobs em segundo plano com o comando `jobs` antes de usar `disown`, para garantir que você está removendo o job correto.
- Use `disown` após iniciar um processo em segundo plano com `&` para garantir que ele continue a funcionar mesmo se você fechar o terminal.
- Lembre-se de que, uma vez que um job é desassociado com `disown`, você não poderá mais trazê-lo de volta para o controle do terminal.