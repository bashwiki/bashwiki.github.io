# [리눅스] Bash htop 사용법

## Overview
`htop` is an interactive process viewer for Unix systems. It provides a real-time, user-friendly interface for monitoring system processes, resource usage, and system performance. Unlike the traditional `top` command, `htop` allows users to scroll through the list of processes, sort them by various criteria, and send signals to processes directly from the interface. Its colorful display and intuitive controls make it a popular choice among engineers and developers for system monitoring and management.

## Usage
The basic syntax for launching `htop` is simply:

```bash
htop
```

### Common Options
- `-h`, `--help`: Display help information and exit.
- `-v`, `--version`: Show version information and exit.
- `-C`, `--no-color`: Run `htop` without color.
- `-s`, `--sort`: Specify a sorting criterion (e.g., `PID`, `MEM`, `CPU`).
- `-p`, `--pid`: Monitor specific process IDs.

## Examples
### Example 1: Launching htop
To start `htop`, simply enter the following command in your terminal:

```bash
htop
```
This will open the `htop` interface, displaying a list of currently running processes along with CPU and memory usage statistics.

### Example 2: Sorting by Memory Usage
If you want to sort the processes by memory usage, you can do this directly within the `htop` interface by pressing `F6` (or using the mouse to click on the "MEM%" column). Alternatively, you can start `htop` with sorting by memory usage by using the command:

```bash
htop -s MEM
```

## Tips
- Use the arrow keys to navigate through the process list and the `F9` key to kill a selected process.
- Press `F2` to access the setup menu, where you can customize the display options and settings to suit your preferences.
- To search for a specific process, press `F3` and type the name or part of the name of the process you are looking for.
- Regularly monitor your system's performance using `htop` to identify resource-intensive processes that may need attention.

By utilizing `htop`, you can effectively manage and monitor your system's processes, making it an essential tool for developers and engineers working in a Unix environment.