# [Linux] Bash rsync 使用方法: 文件同步工具

## 概述
`rsync` 是一个强大的文件同步工具，常用于在本地和远程系统之间高效地复制和同步文件。它通过仅传输更改的部分来节省带宽和时间。

## 用法
基本语法如下：
```
rsync [选项] [源] [目标]
```

## 常用选项
- `-a`：归档模式，等同于 `-rlptgoD`，保留文件的权限、时间戳等信息。
- `-v`：详细输出，显示传输的文件信息。
- `-z`：在传输时压缩文件，以减少带宽使用。
- `-r`：递归地复制整个目录。
- `--delete`：在目标中删除源中不存在的文件。

## 常见示例
1. **同步本地目录**
   ```bash
   rsync -av /path/to/source/ /path/to/destination/
   ```

2. **从本地同步到远程服务器**
   ```bash
   rsync -avz /path/to/local/ user@remote_host:/path/to/remote/
   ```

3. **从远程服务器同步到本地**
   ```bash
   rsync -avz user@remote_host:/path/to/remote/ /path/to/local/
   ```

4. **使用删除选项同步**
   ```bash
   rsync -av --delete /path/to/source/ /path/to/destination/
   ```

## 小贴士
- 在使用 `--delete` 选项时，请务必小心，以免意外删除重要文件。
- 可以使用 `--dry-run` 选项来预览将要执行的操作，而不实际进行文件传输。
- 定期备份重要数据，使用 `rsync` 可以方便地进行增量备份。