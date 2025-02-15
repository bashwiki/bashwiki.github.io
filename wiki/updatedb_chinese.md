# [리눅스] Bash updatedb 사용법

## 概述
`updatedb` 是一个用于更新文件数据库的 Bash 命令，通常与 `locate` 命令配合使用。其主要目的是快速索引文件系统中的文件和目录，以便用户可以通过 `locate` 命令快速查找文件。`updatedb` 会扫描指定的目录并将文件路径存储在数据库中，从而提高搜索效率。

## 用法
基本语法如下：
```bash
updatedb [选项]
```

常见选项包括：
- `--local`：仅更新本地文件系统的数据库。
- `--prunepaths`：指定不应包含在数据库中的路径。
- `--output`：指定输出数据库的文件名，默认为 `/var/lib/mlocate/mlocate.db`。

## 示例
1. 更新默认数据库：
   ```bash
   sudo updatedb
   ```
   这个命令会以超级用户权限更新默认的文件数据库。

2. 更新数据库并排除特定路径：
   ```bash
   sudo updatedb --prunepaths='/tmp,/var/tmp'
   ```
   这个命令会更新数据库，同时排除 `/tmp` 和 `/var/tmp` 目录中的文件。

## 提示
- 定期运行 `updatedb` 可以确保文件数据库保持最新，特别是在频繁添加或删除文件的环境中。
- 使用 `--prunepaths` 选项可以有效减少数据库的大小，从而提高 `locate` 命令的搜索速度。
- 在大型文件系统上运行 `updatedb` 可能需要一些时间，建议在系统负载较低时执行该命令。