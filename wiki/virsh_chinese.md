# [Linux] Bash virsh 使用指南: 管理虚拟机

## 概述
`virsh` 是一个命令行工具，用于管理虚拟机和虚拟网络。它是基于 libvirt 的，支持多种虚拟化技术，如 KVM、Xen 和 QEMU。通过 `virsh`，用户可以创建、删除、启动和停止虚拟机，以及管理网络和存储。

## 用法
基本语法如下：
```bash
virsh [options] [arguments]
```

## 常用选项
- `start <domain>`: 启动指定的虚拟机。
- `shutdown <domain>`: 关闭指定的虚拟机。
- `list`: 列出当前正在运行的虚拟机。
- `define <xml-file>`: 从 XML 文件定义新的虚拟机。
- `destroy <domain>`: 强制停止指定的虚拟机。

## 常见示例
- 启动虚拟机：
```bash
virsh start myVM
```

- 关闭虚拟机：
```bash
virsh shutdown myVM
```

- 列出所有运行中的虚拟机：
```bash
virsh list
```

- 从 XML 文件定义虚拟机：
```bash
virsh define /path/to/myVM.xml
```

- 强制停止虚拟机：
```bash
virsh destroy myVM
```

## 小贴士
- 使用 `virsh list --all` 可以查看所有虚拟机，包括未运行的。
- 定义虚拟机时，确保 XML 文件格式正确，以避免错误。
- 定期备份虚拟机的配置和数据，以防数据丢失。