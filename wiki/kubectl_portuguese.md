# [리눅스] Bash kubectl 사용법

## Overview
O `kubectl` é uma ferramenta de linha de comando para interagir com clusters Kubernetes. Ele permite que os desenvolvedores e engenheiros gerenciem aplicações em contêineres, realizem operações de configuração, monitorem o estado dos recursos e executem comandos diretamente dentro dos pods. O `kubectl` é essencial para a administração de ambientes Kubernetes, facilitando a automação e a orquestração de contêineres.

## Usage
A sintaxe básica do comando `kubectl` é a seguinte:

```
kubectl [opções] [subcomando] [recursos] [nome] [flags]
```

### Comandos Comuns
- `get`: Recupera informações sobre recursos.
- `apply`: Aplica alterações a recursos a partir de arquivos de configuração.
- `delete`: Remove recursos especificados.
- `describe`: Fornece detalhes sobre um recurso específico.

### Opções Comuns
- `-n, --namespace`: Especifica o namespace a ser utilizado.
- `-o, --output`: Define o formato de saída (ex: `json`, `yaml`, `wide`).
- `--kubeconfig`: Especifica um arquivo de configuração diferente do padrão.

## Examples
### Exemplo 1: Listar Pods
Para listar todos os pods em um namespace específico, você pode usar o seguinte comando:

```bash
kubectl get pods -n meu-namespace
```

Este comando retornará uma lista de todos os pods que estão rodando no namespace "meu-namespace".

### Exemplo 2: Aplicar um Arquivo de Configuração
Para aplicar um arquivo de configuração YAML que define um deployment, utilize:

```bash
kubectl apply -f meu-deployment.yaml
```

Este comando criará ou atualizará os recursos definidos no arquivo `meu-deployment.yaml`.

## Tips
- Utilize `kubectl config get-contexts` para verificar os contextos de configuração disponíveis e `kubectl config use-context <contexto>` para alternar entre eles.
- Sempre revise os recursos antes de aplicar alterações com `kubectl apply --dry-run=client -f meu-arquivo.yaml` para evitar mudanças indesejadas.
- Explore a documentação oficial do Kubernetes para entender melhor as opções e recursos disponíveis com o `kubectl`.