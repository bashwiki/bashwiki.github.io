# [Linux] Bash htop Uso: Monitorización interactiva de procesos

## Overview
El comando `htop` es una herramienta de visualización interactiva que permite monitorizar los procesos en un sistema Linux. A diferencia de `top`, `htop` proporciona una interfaz más amigable y permite la gestión de procesos de manera más intuitiva.

## Usage
La sintaxis básica del comando `htop` es la siguiente:

```bash
htop [opciones] [argumentos]
```

## Common Options
- `-h`, `--help`: Muestra la ayuda y las opciones disponibles.
- `-s`, `--sort`: Permite ordenar los procesos por diferentes criterios (por ejemplo, uso de CPU o memoria).
- `-p`, `--pid`: Muestra solo los procesos con los IDs de proceso especificados.
- `-u`, `--user`: Filtra los procesos para mostrar solo los de un usuario específico.

## Common Examples
- Para iniciar `htop` simplemente, ejecuta:
  ```bash
  htop
  ```

- Para ordenar los procesos por uso de memoria, puedes usar:
  ```bash
  htop -s MEM%
  ```

- Para mostrar solo los procesos de un usuario específico, por ejemplo, "usuario1":
  ```bash
  htop -u usuario1
  ```

- Para ver los procesos con IDs específicos, por ejemplo, 1234 y 5678:
  ```bash
  htop -p 1234,5678
  ```

## Tips
- Usa las teclas de función (F1 a F10) para acceder a diferentes funcionalidades, como ayuda, búsqueda y gestión de procesos.
- Puedes usar las teclas de flecha para navegar entre los procesos y la tecla `F9` para matar un proceso seleccionado.
- Personaliza la visualización de columnas presionando `F2` para acceder al menú de configuración.