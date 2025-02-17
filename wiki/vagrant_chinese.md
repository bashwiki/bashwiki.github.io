# [Linux] Bash vagrant 使用指南: 管理虚拟环境

## 概述
Vagrant 是一个用于构建和管理虚拟化开发环境的工具。它使得开发者能够轻松创建、配置和共享虚拟机，确保开发环境的一致性。

## 用法
基本语法如下：
```
vagrant [options] [arguments]
```

## 常用选项
- `init`：初始化一个新的 Vagrant 环境。
- `up`：启动并配置 Vagrant 虚拟机。
- `halt`：停止正在运行的虚拟机。
- `destroy`：销毁虚拟机及其所有数据。
- `ssh`：通过 SSH 连接到正在运行的虚拟机。

## 常见示例
1. 初始化一个新的 Vagrant 环境：
   ```bash
   vagrant init ubuntu/bionic64
   ```

2. 启动虚拟机：
   ```bash
   vagrant up
   ```

3. 停止虚拟机：
   ```bash
   vagrant halt
   ```

4. 销毁虚拟机：
   ```bash
   vagrant destroy
   ```

5. 通过 SSH 连接到虚拟机：
   ```bash
   vagrant ssh
   ```

## 提示
- 在使用 Vagrant 之前，确保已安装 VirtualBox 或其他支持的虚拟化软件。
- 使用 `vagrant status` 查看虚拟机的当前状态。
- 定期使用 `vagrant box update` 更新基础镜像，以获得最新的安全补丁和功能。