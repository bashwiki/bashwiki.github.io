# [Linux] Bash mount 用法: 挂载文件系统

## 概述
`mount` 命令用于将文件系统挂载到指定的目录，使得用户可以访问存储在该文件系统中的数据。通过挂载，操作系统能够识别并使用不同的存储设备，如硬盘、USB 驱动器等。

## 用法
基本语法如下：
```
mount [options] [arguments]
```

## 常用选项
- `-t`：指定文件系统类型。
- `-o`：设置挂载选项，如只读、读写等。
- `-a`：挂载 `/etc/fstab` 文件中所有的文件系统。
- `-r`：以只读模式挂载文件系统。
- `-w`：以读写模式挂载文件系统。

## 常见示例
1. 挂载一个 USB 驱动器：
   ```bash
   mount /dev/sdb1 /mnt/usb
   ```

2. 以只读模式挂载一个 ISO 文件：
   ```bash
   mount -o loop -r /path/to/image.iso /mnt/iso
   ```

3. 挂载所有在 `/etc/fstab` 中定义的文件系统：
   ```bash
   mount -a
   ```

4. 挂载一个 ext4 文件系统并指定文件系统类型：
   ```bash
   mount -t ext4 /dev/sdc1 /mnt/data
   ```

## 提示
- 在挂载之前，确保目标目录已存在。
- 使用 `umount` 命令卸载文件系统，确保在卸载前没有进程正在使用该文件系统。
- 定期检查 `/etc/fstab` 文件，以确保挂载点和文件系统设置正确。