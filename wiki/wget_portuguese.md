# [Linux] Bash wget Uso: Ferramenta para download de arquivos da web

## Overview
O comando `wget` é uma ferramenta de linha de comando utilizada para baixar arquivos da web. Ele suporta diversos protocolos, como HTTP, HTTPS e FTP, permitindo que os usuários façam downloads de maneira simples e eficiente.

## Usage
A sintaxe básica do comando `wget` é a seguinte:

```bash
wget [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `wget`:

- `-O [arquivo]`: Especifica o nome do arquivo de saída.
- `-c`: Continua um download interrompido.
- `-q`: Executa o comando em modo silencioso, sem mostrar progresso.
- `--limit-rate=[taxa]`: Limita a taxa de download a uma determinada velocidade.
- `-r`: Faz download recursivo de diretórios.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `wget`:

1. **Baixar um arquivo simples:**
   ```bash
   wget https://exemplo.com/arquivo.zip
   ```

2. **Baixar um arquivo e renomeá-lo:**
   ```bash
   wget -O novo_nome.zip https://exemplo.com/arquivo.zip
   ```

3. **Continuar um download interrompido:**
   ```bash
   wget -c https://exemplo.com/arquivo.zip
   ```

4. **Baixar um site inteiro de forma recursiva:**
   ```bash
   wget -r https://exemplo.com
   ```

5. **Limitar a taxa de download:**
   ```bash
   wget --limit-rate=200k https://exemplo.com/arquivo.zip
   ```

## Tips
- Sempre verifique se você tem permissão para baixar o conteúdo de um site.
- Use a opção `-q` para downloads em scripts, evitando a poluição do terminal com mensagens desnecessárias.
- Combine opções para personalizar seus downloads, como `-c` com `-O` para continuar downloads com nomes específicos.