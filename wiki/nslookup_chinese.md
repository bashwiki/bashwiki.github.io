# [리눅스] Bash nslookup 사용법

## 概述
`nslookup` 是一个用于查询域名系统（DNS）记录的命令行工具。它的主要目的是帮助用户获取与域名相关的各种信息，例如 IP 地址、邮件交换（MX）记录等。`nslookup` 可以用于故障排除 DNS 问题，验证 DNS 配置，以及获取域名的相关信息。

## 用法
`nslookup` 的基本语法如下：

```bash
nslookup [选项] [域名] [服务器]
```

### 常用选项
- `-type=TYPE`：指定要查询的记录类型，例如 A、AAAA、MX、CNAME 等。
- `-debug`：显示详细的调试信息。
- `-timeout=秒数`：设置查询超时时间，默认是 5 秒。
- `-port=端口号`：指定 DNS 服务器的端口，默认是 53。

## 示例
### 示例 1：查询域名的 A 记录
要查询 `example.com` 的 A 记录，可以使用以下命令：

```bash
nslookup example.com
```

输出将显示 `example.com` 的 IP 地址。

### 示例 2：查询特定类型的 DNS 记录
如果你想查询 `example.com` 的 MX 记录，可以使用以下命令：

```bash
nslookup -type=MX example.com
```

这将返回与 `example.com` 相关的邮件交换服务器的信息。

## 提示
- 使用 `nslookup` 时，可以指定不同的 DNS 服务器进行查询，例如 Google 的公共 DNS 服务器（8.8.8.8）：

```bash
nslookup example.com 8.8.8.8
```

- 在进行 DNS 故障排除时，结合 `-debug` 选项可以获得更详细的信息，有助于分析问题。
- 定期检查域名的 DNS 记录，以确保其正确性和有效性，特别是在更改 DNS 配置后。