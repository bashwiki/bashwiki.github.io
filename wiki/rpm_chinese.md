# [Linux] Bash rpm 用法: 管理软件包

## 概述
`rpm`（Red Hat Package Manager）是一个用于管理Linux系统中软件包的命令行工具。它可以用于安装、升级、卸载和查询软件包，广泛应用于基于RPM的Linux发行版，如Red Hat、CentOS和Fedora。

## 用法
基本语法如下：
```
rpm [options] [arguments]
```

## 常用选项
- `-i`：安装一个新的软件包。
- `-U`：升级一个已安装的软件包。
- `-e`：卸载一个已安装的软件包。
- `-q`：查询已安装的软件包。
- `-l`：列出软件包中的文件。
- `--help`：显示帮助信息。

## 常见示例
1. **安装软件包**
   ```bash
   rpm -i package.rpm
   ```

2. **升级软件包**
   ```bash
   rpm -U package.rpm
   ```

3. **卸载软件包**
   ```bash
   rpm -e package-name
   ```

4. **查询已安装的软件包**
   ```bash
   rpm -q package-name
   ```

5. **列出软件包中的文件**
   ```bash
   rpm -ql package-name
   ```

## 小贴士
- 在安装或升级软件包之前，建议使用`--checksig`选项来验证软件包的签名，以确保其来源的可信性。
- 使用`-v`选项可以在执行命令时显示详细信息，帮助排查问题。
- 定期检查和清理不再需要的软件包，以保持系统的整洁和性能。