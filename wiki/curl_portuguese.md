# [Linux] Bash curl Uso: Ferramenta para transferir dados pela rede

## Overview
O comando `curl` é uma ferramenta de linha de comando que permite transferir dados de ou para um servidor utilizando diversos protocolos, como HTTP, HTTPS, FTP e muitos outros. É amplamente utilizado para interagir com APIs e baixar arquivos.

## Usage
A sintaxe básica do comando `curl` é a seguinte:

```bash
curl [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `curl`:

- `-X`: Especifica o método HTTP a ser utilizado (GET, POST, etc.).
- `-d`: Envia dados no corpo da requisição (usado principalmente com POST).
- `-H`: Adiciona um cabeçalho à requisição.
- `-o`: Salva a saída em um arquivo em vez de exibi-la no terminal.
- `-I`: Faz uma requisição apenas para os cabeçalhos da resposta.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `curl`:

1. **Fazer uma requisição GET simples:**
   ```bash
   curl https://api.exemplo.com/dados
   ```

2. **Fazer uma requisição POST com dados:**
   ```bash
   curl -X POST -d "nome=João&idade=30" https://api.exemplo.com/usuarios
   ```

3. **Adicionar um cabeçalho à requisição:**
   ```bash
   curl -H "Authorization: Bearer seu_token" https://api.exemplo.com/protegido
   ```

4. **Salvar a saída em um arquivo:**
   ```bash
   curl -o arquivo.txt https://www.exemplo.com/pagina
   ```

5. **Fazer uma requisição apenas para os cabeçalhos:**
   ```bash
   curl -I https://www.exemplo.com
   ```

## Tips
- Sempre verifique a documentação da API que você está utilizando para entender quais métodos e dados são suportados.
- Utilize a opção `-v` para habilitar o modo verbose, que fornece informações detalhadas sobre a requisição e resposta.
- Para testar rapidamente uma API, você pode usar ferramentas como Postman, mas o `curl` é excelente para automação em scripts.