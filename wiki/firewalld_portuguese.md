# [Linux] Bash firewalld Uso: Gerenciar regras de firewall

## Overview
O comando `firewalld` é uma ferramenta de gerenciamento de firewall que fornece uma interface dinâmica para configurar regras de firewall no Linux. Ele permite que os usuários definam e gerenciem zonas de segurança e regras de filtragem de pacotes de forma simples e eficaz.

## Usage
A sintaxe básica do comando `firewalld` é a seguinte:

```bash
firewalld [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `firewalld`:

- `--zone=<zona>`: Especifica a zona de firewall a ser usada.
- `--add-service=<serviço>`: Adiciona um serviço à zona especificada.
- `--remove-service=<serviço>`: Remove um serviço da zona especificada.
- `--list-all`: Lista todas as regras e serviços configurados na zona atual.
- `--set-target=<alvo>`: Define o alvo da zona (por exemplo, `ACCEPT`, `DROP`).

## Common Examples
Aqui estão alguns exemplos práticos de como usar o `firewalld`:

1. **Listar todas as zonas disponíveis:**
   ```bash
   firewall-cmd --get-zones
   ```

2. **Adicionar o serviço HTTP à zona pública:**
   ```bash
   firewall-cmd --zone=public --add-service=http
   ```

3. **Remover o serviço SSH da zona interna:**
   ```bash
   firewall-cmd --zone=internal --remove-service=ssh
   ```

4. **Listar todas as regras na zona pública:**
   ```bash
   firewall-cmd --zone=public --list-all
   ```

5. **Definir a zona de um dispositivo de rede:**
   ```bash
   firewall-cmd --zone=home --change-interface=eth0
   ```

## Tips
- Sempre verifique a configuração atual do firewall antes de fazer alterações, usando `firewall-cmd --list-all`.
- Use a opção `--permanent` para tornar as alterações persistentes após a reinicialização do sistema.
- Teste suas regras em um ambiente seguro antes de aplicá-las em um servidor de produção para evitar interrupções no serviço.