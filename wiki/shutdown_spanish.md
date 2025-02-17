# [Linux] Bash shutdown uso: Apagar o reiniciar el sistema

El comando `shutdown` se utiliza para apagar o reiniciar un sistema Linux de manera controlada.

## Overview
El comando `shutdown` permite a los usuarios y administradores de sistemas programar el apagado o reinicio del sistema. Este comando es útil para realizar mantenimientos, actualizaciones o simplemente para apagar el sistema de forma segura.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
shutdown [opciones] [tiempo] [mensaje]
```

## Common Options
- `-h`: Apagar el sistema.
- `-r`: Reiniciar el sistema.
- `-P`: Apagar el sistema y luego detener la energía (equivalente a `-h`).
- `now`: Ejecutar el comando inmediatamente.
- `+m`: Programar el apagado o reinicio en `m` minutos.
- `hh:mm`: Programar el apagado o reinicio a una hora específica.

## Common Examples
1. **Apagar el sistema inmediatamente:**
   ```bash
   shutdown -h now
   ```

2. **Reiniciar el sistema en 5 minutos:**
   ```bash
   shutdown -r +5
   ```

3. **Apagar el sistema a las 10:30 PM:**
   ```bash
   shutdown -h 22:30
   ```

4. **Enviar un mensaje a los usuarios antes de apagar el sistema:**
   ```bash
   shutdown -h +1 "El sistema se apagará en 1 minuto. Por favor, guarden su trabajo."
   ```

5. **Cancelar un apagado programado:**
   ```bash
   shutdown -c
   ```

## Tips
- Siempre es recomendable avisar a los usuarios antes de realizar un apagado o reinicio para evitar la pérdida de datos.
- Utiliza el comando `shutdown -c` si necesitas cancelar un apagado programado.
- Para evitar problemas, asegúrate de que todos los procesos críticos se hayan cerrado antes de apagar el sistema.