# [Linux] Bash kubectl Uso: Interactuar con clústeres de Kubernetes

## Overview
El comando `kubectl` es una herramienta de línea de comandos que permite a los usuarios interactuar con clústeres de Kubernetes. Con `kubectl`, puedes implementar aplicaciones, inspeccionar y gestionar recursos, y ver registros, entre otras funciones.

## Usage
La sintaxis básica del comando `kubectl` es la siguiente:

```bash
kubectl [opciones] [argumentos]
```

## Common Options
- `get`: Recupera información sobre recursos en el clúster.
- `apply`: Aplica cambios a los recursos definidos en archivos de configuración.
- `delete`: Elimina recursos del clúster.
- `describe`: Muestra detalles sobre un recurso específico.
- `logs`: Muestra los registros de un pod.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `kubectl`:

### Obtener todos los pods en el clúster
```bash
kubectl get pods
```

### Aplicar un archivo de configuración
```bash
kubectl apply -f archivo-configuracion.yaml
```

### Eliminar un pod específico
```bash
kubectl delete pod nombre-del-pod
```

### Describir un servicio
```bash
kubectl describe service nombre-del-servicio
```

### Ver los registros de un pod
```bash
kubectl logs nombre-del-pod
```

## Tips
- Usa `kubectl get all` para obtener un resumen de todos los recursos en el clúster.
- Asegúrate de tener configurado el contexto correcto con `kubectl config use-context nombre-del-contexto`.
- Utiliza `-o wide` para obtener más detalles sobre los recursos al usar `kubectl get`.
- Familiarízate con los archivos de configuración en formato YAML para facilitar la gestión de recursos.