# [Linux] Bash kubectl Uso: Gerenciar clusters Kubernetes

## Overview
O comando `kubectl` é a ferramenta de linha de comando para interagir com clusters Kubernetes. Ele permite que os usuários executem comandos para implantar aplicativos, inspecionar e gerenciar recursos do cluster, e visualizar logs, entre outras funcionalidades.

## Usage
A sintaxe básica do comando `kubectl` é a seguinte:

```bash
kubectl [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `kubectl`:

- `get`: Recupera informações sobre recursos no cluster.
- `apply`: Aplica alterações a recursos de configuração.
- `delete`: Remove recursos do cluster.
- `describe`: Fornece detalhes sobre um recurso específico.
- `logs`: Exibe logs de um pod específico.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `kubectl`:

### Listar todos os pods em um namespace
```bash
kubectl get pods -n nome-do-namespace
```

### Aplicar um arquivo de configuração
```bash
kubectl apply -f caminho/para/arquivo.yaml
```

### Excluir um pod específico
```bash
kubectl delete pod nome-do-pod -n nome-do-namespace
```

### Descrever um serviço
```bash
kubectl describe service nome-do-serviço -n nome-do-namespace
```

### Visualizar logs de um pod
```bash
kubectl logs nome-do-pod -n nome-do-namespace
```

## Tips
- Sempre verifique o namespace atual com `kubectl config view --minify | grep namespace:` para garantir que você está operando no contexto correto.
- Utilize `kubectl get all` para obter uma visão geral de todos os recursos em um namespace.
- Use a opção `-o wide` para obter informações adicionais sobre os recursos, como endereços IP e nós.
- Considere usar aliases para comandos comuns para agilizar seu fluxo de trabalho.