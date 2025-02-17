# [Linux] Bash exit uso: Finaliza um shell ou script

## Overview
O comando `exit` é utilizado para encerrar um shell ou script em Bash. Ele pode retornar um código de saída que indica o status da execução do script ou do shell. Um código de saída de zero geralmente indica sucesso, enquanto qualquer número diferente de zero indica um erro.

## Usage
A sintaxe básica do comando `exit` é a seguinte:

```bash
exit [opções] [status]
```

## Common Options
O comando `exit` não possui muitas opções, mas aqui estão algumas informações úteis:

- `status`: Um número que representa o código de saída. Se não for especificado, o código de saída será o último comando executado.

## Common Examples

1. **Saindo de um script com sucesso:**
   ```bash
   #!/bin/bash
   echo "Script executado com sucesso."
   exit 0
   ```

2. **Saindo de um script com erro:**
   ```bash
   #!/bin/bash
   echo "Ocorreu um erro."
   exit 1
   ```

3. **Saindo de um shell interativo:**
   ```bash
   exit
   ```

4. **Saindo com um código de erro específico:**
   ```bash
   exit 42
   ```

## Tips
- Sempre utilize `exit 0` ao final de scripts que foram executados com sucesso para indicar que não houve erros.
- Utilize códigos de saída diferentes para diferentes tipos de erros, facilitando a depuração.
- Em scripts mais complexos, considere capturar o código de saída de comandos críticos e usar `exit` para sair com esse código.