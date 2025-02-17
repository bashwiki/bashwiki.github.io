# [Linux] Bash dmidecode 用法: 查询系统硬件信息

## 概述
`dmidecode` 是一个用于提取计算机硬件信息的命令行工具。它从系统的 DMI（桌面管理接口）表中读取数据，提供有关硬件组件的详细信息，如 BIOS、内存、处理器等。

## 用法
基本语法如下：
```bash
dmidecode [options] [arguments]
```

## 常用选项
- `-t` 或 `--type`: 指定要显示的 DMI 类型，例如 `-t memory` 仅显示内存信息。
- `-q` 或 `--quiet`: 以安静模式运行，减少输出信息。
- `-h` 或 `--help`: 显示帮助信息。

## 常见示例
1. **查看所有 DMI 信息**
   ```bash
   dmidecode
   ```

2. **仅查看内存信息**
   ```bash
   dmidecode -t memory
   ```

3. **查看 BIOS 信息**
   ```bash
   dmidecode -t bios
   ```

4. **查看处理器信息**
   ```bash
   dmidecode -t processor
   ```

5. **以安静模式查看所有信息**
   ```bash
   dmidecode -q
   ```

## 提示
- 使用 `sudo` 权限运行 `dmidecode`，以确保能够访问所有硬件信息。
- 可以将输出重定向到文件中，方便后续查看：
  ```bash
  dmidecode > hardware_info.txt
  ```
- 定期检查硬件信息，尤其是在升级或更换组件后，以确保系统配置的正确性。