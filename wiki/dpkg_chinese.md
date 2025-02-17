# [Linux] Bash dpkg 用法: 管理 Debian 软件包

## 概述
`dpkg` 是 Debian 和基于 Debian 的系统（如 Ubuntu）中用于管理软件包的低级工具。它可以安装、卸载和管理软件包文件（.deb）。

## 用法
基本语法如下：
```bash
dpkg [options] [arguments]
```

## 常用选项
- `-i`：安装指定的 .deb 软件包。
- `-r`：卸载指定的软件包。
- `-l`：列出已安装的软件包。
- `-s`：显示指定软件包的状态信息。
- `-L`：列出指定软件包安装的文件。

## 常见示例
1. **安装软件包**
   ```bash
   dpkg -i package.deb
   ```

2. **卸载软件包**
   ```bash
   dpkg -r package_name
   ```

3. **列出所有已安装的软件包**
   ```bash
   dpkg -l
   ```

4. **查看软件包状态**
   ```bash
   dpkg -s package_name
   ```

5. **列出软件包安装的文件**
   ```bash
   dpkg -L package_name
   ```

## 小贴士
- 在使用 `dpkg` 安装软件包时，确保所有依赖项都已满足，或者使用 `apt` 来处理依赖关系。
- 使用 `dpkg -l | grep package_name` 可以快速查找特定软件包是否已安装。
- 在卸载软件包时，使用 `-P` 选项可以完全删除软件包及其配置文件。