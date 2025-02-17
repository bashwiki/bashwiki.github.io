# [Linux] Bash dig Uso: Consulta de DNS

O comando `dig` é uma ferramenta poderosa para consultar informações do Sistema de Nomes de Domínio (DNS). Ele permite que os usuários obtenham detalhes sobre registros DNS, como endereços IP, registros MX, entre outros.

## Overview
O `dig` (Domain Information Groper) é utilizado para realizar consultas DNS. Ele é amplamente utilizado por administradores de sistemas e redes para diagnosticar problemas de DNS e verificar a configuração de domínios.

## Usage
A sintaxe básica do comando `dig` é a seguinte:

```bash
dig [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `dig`:

- `@servidor`: Especifica um servidor DNS para consultar.
- `-t tipo`: Define o tipo de registro DNS a ser consultado (ex: A, AAAA, MX).
- `+short`: Exibe uma saída mais concisa, mostrando apenas a resposta.
- `+trace`: Segue a cadeia de servidores DNS para resolver o nome.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `dig`:

1. **Consultar o endereço IP de um domínio:**
   ```bash
   dig exemplo.com
   ```

2. **Consultar um registro MX (Mail Exchange) de um domínio:**
   ```bash
   dig -t MX exemplo.com
   ```

3. **Consultar um servidor DNS específico:**
   ```bash
   dig @8.8.8.8 exemplo.com
   ```

4. **Obter uma saída curta:**
   ```bash
   dig +short exemplo.com
   ```

5. **Seguir a cadeia de servidores DNS:**
   ```bash
   dig +trace exemplo.com
   ```

## Tips
- Utilize a opção `+short` para obter respostas rápidas e diretas, especialmente útil para verificar endereços IP.
- Sempre que possível, teste consultas com diferentes servidores DNS para verificar a consistência das respostas.
- Combine o `dig` com outros comandos, como `grep`, para filtrar informações específicas da saída.