# [리눅스] Bash kubectl 사용법

## Overview
`kubectl` es la herramienta de línea de comandos para interactuar con Kubernetes, un sistema de orquestación de contenedores. Su propósito principal es permitir a los desarrolladores y administradores gestionar aplicaciones en contenedores, así como el clúster de Kubernetes en sí. Con `kubectl`, puedes desplegar aplicaciones, inspeccionar y gestionar recursos, y ver registros, entre otras tareas.

## Usage
La sintaxis básica de `kubectl` es la siguiente:

```bash
kubectl [opciones] [comando] [tipo] [nombre] [flags]
```

- **opciones**: Modificadores globales que afectan el comportamiento de `kubectl`.
- **comando**: La acción que deseas realizar, como `get`, `create`, `delete`, etc.
- **tipo**: El tipo de recurso que deseas gestionar, como `pod`, `service`, `deployment`, etc.
- **nombre**: El nombre específico del recurso que deseas manipular.
- **flags**: Opciones adicionales que pueden modificar el comportamiento del comando.

### Opciones Comunes
- `--namespace`: Especifica el espacio de nombres en el que se ejecutará el comando.
- `-o`: Define el formato de salida, como `json` o `yaml`.
- `--kubeconfig`: Especifica el archivo de configuración de Kubernetes que se utilizará.

## Examples
### Ejemplo 1: Listar Pods
Para listar todos los pods en el espacio de nombres actual, puedes usar el siguiente comando:

```bash
kubectl get pods
```

### Ejemplo 2: Crear un Deployment
Para crear un nuevo deployment llamado "mi-aplicacion" con una imagen de contenedor específica, puedes usar:

```bash
kubectl create deployment mi-aplicacion --image=mi-imagen:latest
```

## Tips
- Asegúrate de tener configurado correctamente tu contexto de Kubernetes utilizando `kubectl config use-context`.
- Utiliza el flag `-o wide` para obtener más información sobre los recursos listados, como las direcciones IP y los nodos donde están corriendo.
- Familiarízate con los comandos de `kubectl` utilizando `kubectl --help` para obtener una lista completa de comandos y opciones disponibles.
- Considera el uso de alias para comandos comunes para mejorar tu eficiencia en la línea de comandos.