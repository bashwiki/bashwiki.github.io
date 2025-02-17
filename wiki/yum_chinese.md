# [Linux] Bash yum 用法：软件包管理工具

## 概述
`yum` 是一个用于在基于 RPM 的 Linux 发行版中管理软件包的命令行工具。它可以帮助用户安装、更新和删除软件包，同时处理软件包之间的依赖关系。

## 用法
基本语法如下：
```
yum [options] [arguments]
```

## 常用选项
- `install`：安装指定的软件包。
- `remove`：卸载指定的软件包。
- `update`：更新已安装的软件包到最新版本。
- `search`：搜索软件包。
- `info`：显示软件包的详细信息。
- `list`：列出可用的软件包。

## 常见示例
- 安装软件包：
  ```bash
  yum install httpd
  ```

- 卸载软件包：
  ```bash
  yum remove httpd
  ```

- 更新所有已安装的软件包：
  ```bash
  yum update
  ```

- 搜索软件包：
  ```bash
  yum search nginx
  ```

- 显示软件包信息：
  ```bash
  yum info vim
  ```

- 列出所有可用的软件包：
  ```bash
  yum list available
  ```

## 小贴士
- 在执行更新或安装操作之前，建议先运行 `yum check-update` 来检查可用的更新。
- 使用 `-y` 选项可以自动回答“是”以确认操作，适合批量处理：
  ```bash
  yum -y install git
  ```
- 定期清理缓存可以节省磁盘空间，使用命令 `yum clean all` 来清理所有缓存。