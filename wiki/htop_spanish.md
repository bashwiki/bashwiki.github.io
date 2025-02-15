# [리눅스] Bash htop 사용법

## Overview
El comando `htop` es una herramienta interactiva de monitoreo de procesos en sistemas operativos Unix y Linux. A diferencia del comando `top`, `htop` ofrece una interfaz más amigable y colorida, permitiendo a los usuarios visualizar y gestionar los procesos en ejecución de manera más eficiente. Su propósito principal es proporcionar información en tiempo real sobre el uso de recursos del sistema, como CPU, memoria y swap, así como permitir la gestión de procesos mediante una interfaz de usuario intuitiva.

## Usage
La sintaxis básica del comando `htop` es la siguiente:

```bash
htop [opciones]
```

Algunas de las opciones más comunes que puedes utilizar con `htop` son:

- `-h`, `--help`: Muestra la ayuda y las opciones disponibles.
- `-s`, `--sort`: Permite especificar el criterio de ordenación de los procesos (por ejemplo, `-s PERCENT_CPU` para ordenar por uso de CPU).
- `-p`, `--pid`: Muestra solo los procesos con los identificadores de proceso (PID) especificados.

## Examples
Aquí tienes un par de ejemplos prácticos de cómo utilizar `htop`:

1. **Ejecutar htop sin opciones**:
   Simplemente ejecuta `htop` en la terminal para abrir la interfaz interactiva y ver los procesos en tiempo real.

   ```bash
   htop
   ```

2. **Ordenar procesos por uso de memoria**:
   Puedes iniciar `htop` y luego presionar `F6` para seleccionar el criterio de ordenación. Sin embargo, también puedes iniciar `htop` directamente ordenado por uso de memoria con el siguiente comando:

   ```bash
   htop -s PERCENT_MEM
   ```

## Tips
- **Navegación**: Usa las teclas de flecha para navegar por la lista de procesos. Puedes seleccionar un proceso y presionar `F9` para enviar una señal (como `SIGTERM` o `SIGKILL`) para finalizarlo.
- **Filtrado**: Presiona `F3` para buscar un proceso específico, lo que puede ser útil si tienes muchos procesos en ejecución.
- **Personalización**: Puedes personalizar la visualización de `htop` presionando `F2` para acceder a la configuración, donde puedes ajustar la apariencia y los datos mostrados.
- **Uso de recursos**: Observa la barra de uso de CPU y memoria en la parte superior para tener una idea rápida del estado general del sistema.

`htop` es una herramienta poderosa para ingenieros y desarrolladores que buscan un control más granular sobre los procesos en sus sistemas.