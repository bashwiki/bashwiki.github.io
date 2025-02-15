# [리눅스] Bash rsync 사용법

## 概述
`rsync` 是一个强大的文件传输和同步工具，广泛用于在本地和远程系统之间高效地复制和同步文件。它的主要目的是通过仅传输更改的部分来减少数据传输量，从而提高速度和效率。`rsync` 支持增量备份、压缩传输和多种传输协议，使其成为备份和镜像文件的理想选择。

## 用法
`rsync` 的基本语法如下：
```bash
rsync [OPTION]... SRC [SRC]... DEST
```
其中，`SRC` 是源文件或目录，`DEST` 是目标文件或目录。常用选项包括：

- `-a`：归档模式，表示以递归方式传输文件，并保持文件的权限、时间戳等信息。
- `-v`：详细模式，输出详细的传输过程信息。
- `-z`：在传输过程中进行压缩，以减少带宽使用。
- `-r`：递归复制整个目录。
- `-e`：指定远程 shell，例如 `ssh`。
- `--delete`：在目标中删除源中不存在的文件。

## 示例
以下是两个使用 `rsync` 的实际示例：

1. **本地文件同步**：
   将本地目录 `/path/to/source/` 同步到 `/path/to/destination/`：
   ```bash
   rsync -av /path/to/source/ /path/to/destination/
   ```

2. **远程文件同步**：
   将本地目录同步到远程服务器的指定目录：
   ```bash
   rsync -avz -e ssh /path/to/local/ user@remote_host:/path/to/remote/
   ```

## 提示
- 在使用 `rsync` 进行大规模数据传输时，建议使用 `-z` 选项进行压缩，以提高传输速度。
- 使用 `--dry-run` 选项可以在实际执行之前查看将要进行的操作，帮助避免意外的数据丢失：
  ```bash
  rsync -av --dry-run /path/to/source/ /path/to/destination/
  ```
- 定期使用 `rsync` 进行备份时，可以结合 `cron` 定时任务实现自动化备份。

通过掌握 `rsync` 的使用，您可以高效地管理文件传输和备份任务。