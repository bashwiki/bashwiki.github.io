# [Linux] Bash sysctl 用法: 管理内核参数

## 概述
`sysctl` 命令用于在运行时查看和修改 Linux 内核的参数。通过这个命令，用户可以动态调整系统的性能和行为，而无需重启系统。

## 用法
基本语法如下：
```bash
sysctl [options] [arguments]
```

## 常用选项
- `-a`：显示所有可用的内核参数及其当前值。
- `-w`：写入新的值到指定的内核参数。
- `-n`：仅显示指定参数的值，不显示参数名。
- `-p`：从指定的文件加载参数，通常用于加载配置文件。

## 常见示例
1. 查看所有内核参数：
   ```bash
   sysctl -a
   ```

2. 查看特定参数的值，例如 `vm.swappiness`：
   ```bash
   sysctl vm.swappiness
   ```

3. 修改内核参数，例如将 `vm.swappiness` 设置为 10：
   ```bash
   sysctl -w vm.swappiness=10
   ```

4. 从配置文件加载内核参数，通常是 `/etc/sysctl.conf`：
   ```bash
   sysctl -p
   ```

5. 仅显示 `net.ipv4.ip_forward` 参数的值：
   ```bash
   sysctl -n net.ipv4.ip_forward
   ```

## 提示
- 在修改内核参数之前，建议先备份当前的配置，以防需要恢复。
- 使用 `sysctl -p` 加载配置文件时，确保文件格式正确，以避免加载错误。
- 可以在 `/etc/sysctl.conf` 文件中添加永久性的参数设置，这样在系统重启后仍然有效。