# [Linux] Bash mkfs 用法: 创建文件系统

## 概述
`mkfs` 命令用于在块设备上创建文件系统。它是“make filesystem”的缩写，通常用于格式化磁盘或分区，使其可以存储数据。

## 用法
基本语法如下：
```bash
mkfs [options] [arguments]
```

## 常用选项
- `-t`：指定文件系统类型，例如 `ext4`、`vfat` 等。
- `-L`：为文件系统设置标签。
- `-n`：在创建文件系统时不实际写入数据，只进行测试。
- `-V`：显示详细的执行过程。

## 常见示例
1. 创建一个 `ext4` 文件系统：
   ```bash
   mkfs -t ext4 /dev/sdb1
   ```

2. 创建一个 `vfat` 文件系统并设置标签：
   ```bash
   mkfs -t vfat -L MY_USB /dev/sdc1
   ```

3. 测试创建文件系统而不实际写入：
   ```bash
   mkfs -n -t ext4 /dev/sdb1
   ```

4. 显示详细的创建过程：
   ```bash
   mkfs -V -t ext4 /dev/sdb1
   ```

## 提示
- 在使用 `mkfs` 之前，请确保备份重要数据，因为格式化将删除设备上的所有数据。
- 使用 `lsblk` 命令查看当前的块设备和分区，以避免误格式化。
- 在创建文件系统时，选择合适的文件系统类型以满足你的需求，例如 `ext4` 适合大多数 Linux 系统，`vfat` 适合与 Windows 兼容的 USB 驱动器。