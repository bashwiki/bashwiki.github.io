# [Linux] Bash systemctl uso: Gerenciar serviços e unidades do sistema

## Overview
O comando `systemctl` é uma ferramenta poderosa usada para gerenciar o sistema e os serviços no Linux, especialmente em sistemas que utilizam o systemd como sistema de inicialização. Com ele, é possível iniciar, parar, reiniciar e verificar o status de serviços, além de gerenciar unidades do sistema.

## Usage
A sintaxe básica do comando `systemctl` é a seguinte:

```bash
systemctl [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `systemctl`:

- `start`: Inicia uma unidade ou serviço.
- `stop`: Para uma unidade ou serviço em execução.
- `restart`: Reinicia uma unidade ou serviço.
- `status`: Exibe o status de uma unidade ou serviço.
- `enable`: Habilita uma unidade para iniciar automaticamente na inicialização do sistema.
- `disable`: Desabilita uma unidade para que não inicie automaticamente.
- `list-units`: Lista todas as unidades ativas.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `systemctl`:

1. **Iniciar um serviço**:
   ```bash
   sudo systemctl start nome_do_serviço
   ```

2. **Parar um serviço**:
   ```bash
   sudo systemctl stop nome_do_serviço
   ```

3. **Reiniciar um serviço**:
   ```bash
   sudo systemctl restart nome_do_serviço
   ```

4. **Verificar o status de um serviço**:
   ```bash
   systemctl status nome_do_serviço
   ```

5. **Habilitar um serviço para iniciar automaticamente**:
   ```bash
   sudo systemctl enable nome_do_serviço
   ```

6. **Desabilitar um serviço para não iniciar automaticamente**:
   ```bash
   sudo systemctl disable nome_do_serviço
   ```

7. **Listar todas as unidades ativas**:
   ```bash
   systemctl list-units --type=service
   ```

## Tips
- Sempre use `sudo` ao executar comandos que alteram o estado de serviços, pois muitas operações requerem privilégios de administrador.
- Verifique o status de um serviço após iniciar ou parar para garantir que a operação foi bem-sucedida.
- Use `systemctl list-units --failed` para identificar unidades que falharam ao iniciar ou que estão com problemas.