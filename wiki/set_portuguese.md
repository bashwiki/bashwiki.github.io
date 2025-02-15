# [리눅스] Bash set 사용법

## Overview
O comando `set` no Bash é utilizado para definir ou exibir variáveis de ambiente e opções de shell. Ele permite que os usuários configurem o comportamento do shell, ativando ou desativando certas funcionalidades. O comando é especialmente útil para ajustar o ambiente de execução de scripts e para depuração.

## Usage
A sintaxe básica do comando `set` é a seguinte:

```bash
set [opções] [argumentos]
```

### Comuns opções:
- `-e`: Faz com que o shell saia imediatamente se um comando retornar um status de saída diferente de zero.
- `-u`: Trata variáveis não definidas como um erro e sai imediatamente.
- `-x`: Ativa o modo de depuração, exibindo cada comando antes de ser executado.
- `-o`: Permite ativar ou desativar opções de shell específicas, como `noclobber`, `pipefail`, entre outras.

## Examples
### Exemplo 1: Usando `set -e`
Este exemplo demonstra como usar `set -e` para garantir que o script pare ao encontrar um erro.

```bash
#!/bin/bash
set -e

echo "Iniciando o script..."
cp arquivo_inexistente.txt /destino/
echo "Este texto não será exibido se o comando acima falhar."
```

### Exemplo 2: Usando `set -x`
Aqui, o `set -x` é utilizado para depuração, permitindo que o usuário veja os comandos sendo executados.

```bash
#!/bin/bash
set -x

echo "Executando comandos..."
mkdir nova_pasta
cd nova_pasta
touch arquivo.txt
```

## Tips
- Utilize `set -e` em scripts críticos para evitar que erros não tratados continuem a execução do script.
- O uso de `set -x` é altamente recomendado durante a fase de desenvolvimento e depuração, mas deve ser removido em produção para evitar a exposição de informações sensíveis.
- Combine `set -u` com `set -e` para garantir que seu script não falhe silenciosamente devido a variáveis não definidas.
- Sempre teste suas configurações de `set` em um ambiente seguro antes de aplicá-las em scripts de produção.