# [리눅스] Bash kubectl 사용법

## Overview
`kubectl` is a command-line tool for interacting with Kubernetes clusters. It allows users to deploy applications, manage cluster resources, and view logs, among other tasks. `kubectl` serves as the primary interface for managing Kubernetes resources and is essential for developers and engineers working with container orchestration.

## Usage
The basic syntax for the `kubectl` command is as follows:

```
kubectl [command] [TYPE] [NAME] [flags]
```

- **command**: The specific action you want to perform (e.g., `get`, `create`, `delete`, `apply`).
- **TYPE**: The type of resource you are interacting with (e.g., `pod`, `service`, `deployment`).
- **NAME**: The name of the resource you want to manage (optional for some commands).
- **flags**: Additional options that modify the command's behavior (e.g., `--namespace`, `--output`).

### Common Options
- `--namespace`: Specify the namespace to operate within.
- `-o`: Format the output (e.g., `-o json`, `-o yaml`, `-o wide`).
- `--kubeconfig`: Specify a custom kubeconfig file.
- `--context`: Specify the context to use from the kubeconfig.

## Examples

### Example 1: Get Pods
To list all the pods in the default namespace, you can use the following command:

```bash
kubectl get pods
```

This command will return a list of all pods currently running in the default namespace, along with their status and other details.

### Example 2: Create a Deployment
To create a new deployment named `nginx-deployment` with 3 replicas of an NGINX container, you can use the following command:

```bash
kubectl create deployment nginx-deployment --image=nginx --replicas=3
```

This command will create a deployment that manages three instances of the NGINX container.

## Tips
- Always specify the namespace if you are working with multiple namespaces to avoid confusion.
- Use `kubectl get all` to quickly view all resources in the current namespace.
- Leverage the `-o` flag to format output for easier reading or further processing (e.g., `kubectl get pods -o wide`).
- Familiarize yourself with `kubectl explain [resource]` to understand the fields and options available for different resource types.
- Use `kubectl apply -f [filename]` to manage resources declaratively with YAML or JSON files, which is a best practice for version control and reproducibility.