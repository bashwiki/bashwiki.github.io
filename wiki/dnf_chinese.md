# [Linux] Bash dnf 用法：用于管理软件包的命令

## 概述
`dnf`（Dandified YUM）是一个用于管理Linux系统软件包的命令行工具，主要用于安装、更新和删除软件包。它是YUM的下一代版本，提供了更快的性能和更好的依赖关系管理。

## 用法
基本语法如下：
```bash
dnf [options] [arguments]
```

## 常用选项
- `install`：安装指定的软件包。
- `remove`：删除指定的软件包。
- `update`：更新已安装的软件包。
- `search`：搜索软件包。
- `list`：列出可用或已安装的软件包。
- `info`：显示软件包的详细信息。

## 常见示例
- 安装软件包：
  ```bash
  dnf install package_name
  ```

- 删除软件包：
  ```bash
  dnf remove package_name
  ```

- 更新所有已安装的软件包：
  ```bash
  dnf update
  ```

- 搜索软件包：
  ```bash
  dnf search package_name
  ```

- 列出所有可用的软件包：
  ```bash
  dnf list available
  ```

- 显示软件包信息：
  ```bash
  dnf info package_name
  ```

## 提示
- 在执行安装或删除操作时，可以使用`-y`选项来自动确认所有提示，例如：
  ```bash
  dnf install -y package_name
  ```
- 定期运行`dnf update`以确保系统软件包保持最新状态。
- 使用`dnf clean all`命令清理缓存，以释放磁盘空间。