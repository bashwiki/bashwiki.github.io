# [Linux] Bash sysctl 使用法: 調整內核參數

## Overview
`sysctl` 命令用於在運行時查詢和修改 Linux 內核參數。這些參數影響系統的性能和行為，並且可以在不重新啟動系統的情況下進行調整。

## Usage
基本語法如下：
```bash
sysctl [options] [arguments]
```

## Common Options
- `-a`: 顯示所有可用的內核參數及其當前值。
- `-e`: 當發生錯誤時，繼續執行而不顯示錯誤信息。
- `-p [file]`: 從指定的文件中讀取參數設置，默認為 `/etc/sysctl.conf`。
- `-w`: 寫入新的內核參數值。

## Common Examples
1. **查詢所有內核參數**
   ```bash
   sysctl -a
   ```

2. **查詢特定內核參數**
   ```bash
   sysctl net.ipv4.ip_forward
   ```

3. **修改內核參數**
   ```bash
   sysctl -w net.ipv4.ip_forward=1
   ```

4. **從配置文件加載參數**
   ```bash
   sysctl -p /etc/sysctl.conf
   ```

## Tips
- 在修改內核參數之前，建議先備份當前的配置，以防需要恢復。
- 使用 `sysctl -a` 可以快速檢查系統的當前設置，這對於故障排除非常有幫助。
- 對於持久化的參數修改，建議將變更寫入 `/etc/sysctl.conf` 文件，並使用 `sysctl -p` 來加載。