# [Linux] Bash hostname 使用法: 顯示或設定主機名稱

## Overview
`hostname` 命令用於顯示或設定系統的主機名稱。主機名稱是用來識別網路上的設備，對於網路管理和系統配置非常重要。

## Usage
基本語法如下：
```
hostname [options] [arguments]
```

## Common Options
- `-a`：顯示主機的別名。
- `-d`：顯示主機的域名。
- `-f`：顯示完整的主機名稱（FQDN）。
- `-i`：顯示主機的 IP 位址。
- `-s`：顯示簡短的主機名稱。

## Common Examples
以下是一些常見的使用範例：

1. 顯示當前主機名稱：
   ```bash
   hostname
   ```

2. 顯示完整的主機名稱：
   ```bash
   hostname -f
   ```

3. 顯示主機的 IP 位址：
   ```bash
   hostname -i
   ```

4. 設定新的主機名稱：
   ```bash
   sudo hostname new-hostname
   ```

5. 顯示主機的別名：
   ```bash
   hostname -a
   ```

## Tips
- 設定主機名稱後，建議重新啟動系統以確保變更生效。
- 使用 `hostnamectl` 命令可以更方便地管理主機名稱，特別是在使用 systemd 的系統上。
- 確保新的主機名稱符合網路管理的規範，以避免潛在的連接問題。