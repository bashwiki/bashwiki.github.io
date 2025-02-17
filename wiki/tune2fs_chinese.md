# [Linux] Bash tune2fs 用法: 调整 ext2/ext3/ext4 文件系统的参数

## 概述
`tune2fs` 是一个用于调整 ext2、ext3 和 ext4 文件系统参数的命令。它允许用户修改文件系统的特性和行为，以优化性能或满足特定需求。

## 用法
基本语法如下：
```bash
tune2fs [选项] [参数]
```

## 常用选项
- `-c <max-mount-count>`: 设置最大挂载次数，超过后会强制检查文件系统。
- `-i <interval>`: 设置检查间隔时间，支持以天、周、月等形式指定。
- `-m <reserved-blocks>`: 设置保留给超级用户的块的百分比。
- `-O <feature>`: 启用特定的文件系统特性。
- `-L <label>`: 设置文件系统标签。

## 常见示例
1. 设置最大挂载次数为 20：
   ```bash
   tune2fs -c 20 /dev/sda1
   ```

2. 设置检查间隔为 30 天：
   ```bash
   tune2fs -i 30d /dev/sda1
   ```

3. 设置保留块的百分比为 5%：
   ```bash
   tune2fs -m 5 /dev/sda1
   ```

4. 启用文件系统特性，如 `dir_index`：
   ```bash
   tune2fs -O dir_index /dev/sda1
   ```

5. 设置文件系统标签为 "MyData"：
   ```bash
   tune2fs -L MyData /dev/sda1
   ```

## 提示
- 在使用 `tune2fs` 之前，确保文件系统未被挂载或以只读模式挂载，以避免数据损坏。
- 定期检查文件系统的状态，合理设置挂载次数和检查间隔可以提高系统的稳定性。
- 使用 `tune2fs -l /dev/sda1` 命令可以查看当前文件系统的参数设置，帮助你做出更好的调整。