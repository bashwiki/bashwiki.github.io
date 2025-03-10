# [Linux] Bash du 用法: 显示文件和目录的磁盘使用情况

## 概述
`du`（Disk Usage）命令用于查看文件和目录所占用的磁盘空间。它可以帮助用户了解存储使用情况，从而更有效地管理文件和目录。

## 用法
基本语法如下：
```
du [选项] [参数]
```

## 常用选项
- `-h`：以人类可读的格式显示（例如 KB、MB）。
- `-s`：仅显示每个参数的总计。
- `-a`：显示所有文件和目录的磁盘使用情况。
- `-c`：在输出的最后添加一个总计。
- `--max-depth=N`：限制显示的目录层级深度。

## 常见示例
1. 查看当前目录及其子目录的磁盘使用情况：
   ```bash
   du -h
   ```

2. 查看特定目录的总磁盘使用情况：
   ```bash
   du -sh /path/to/directory
   ```

3. 显示所有文件和目录的磁盘使用情况：
   ```bash
   du -ah /path/to/directory
   ```

4. 限制显示的目录层级深度为1：
   ```bash
   du -h --max-depth=1
   ```

5. 查看多个目录的总磁盘使用情况并显示总计：
   ```bash
   du -ch /path/to/dir1 /path/to/dir2
   ```

## 提示
- 使用 `-h` 选项可以使输出更易于阅读，特别是在处理大量数据时。
- 结合 `--max-depth` 选项，可以快速了解目录结构的磁盘使用情况。
- 定期检查磁盘使用情况，及时清理不必要的文件，有助于保持系统的良好性能。