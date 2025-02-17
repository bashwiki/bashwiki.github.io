# [Linux] Bash htop Uso equivalente: Monitor system processes interactively

## Overview
The `htop` command is an interactive process viewer for Unix systems. It provides a dynamic real-time view of system processes, allowing users to monitor resource usage and manage processes easily. Unlike the traditional `top` command, `htop` offers a more user-friendly interface with color-coded output and the ability to scroll through the list of processes.

## Usage
The basic syntax of the `htop` command is as follows:

```bash
htop [options] [arguments]
```

## Common Options
- `-h`, `--help`: Display help information and exit.
- `-v`, `--version`: Show version information and exit.
- `-C`, `--no-color`: Run `htop` without color support.
- `-s`, `--sort`: Specify the sorting order of processes (e.g., `-s MEM` to sort by memory usage).

## Common Examples
1. **Launch htop**:
   ```bash
   htop
   ```

2. **Run htop without color**:
   ```bash
   htop -C
   ```

3. **Display help information**:
   ```bash
   htop -h
   ```

4. **Sort processes by memory usage**:
   ```bash
   htop -s MEM
   ```

5. **Filter processes by a specific user**:
   ```bash
   htop -u username
   ```

## Tips
- Use the arrow keys to navigate through the list of processes and the function keys (F1 to F10) for various actions like killing a process (F9) or changing the sorting order (F6).
- Press `F2` to access the setup menu, where you can customize the display options to suit your preferences.
- To quickly search for a process, press `F3` and type the name of the process you are looking for.