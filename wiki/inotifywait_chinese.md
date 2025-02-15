# [리눅스] Bash inotifywait 사용법

## 概述
`inotifywait` 是一个用于监控文件系统事件的命令行工具。它可以实时监测指定文件或目录的变化，并在发生变化时输出相应的信息。这个工具主要用于开发和运维场景，例如自动化脚本、实时日志监控等。

## 用法
`inotifywait` 的基本语法如下：

```bash
inotifywait [选项] <路径>
```

### 常用选项
- `-m`：持续监控，直到手动停止。
- `-r`：递归监控指定目录及其子目录。
- `-e <事件>`：指定要监控的事件类型，例如 `modify`、`create`、`delete` 等。
- `-q`：安静模式，只输出事件信息，不输出其他信息。

## 示例
### 示例 1：监控文件修改
以下命令将监控 `example.txt` 文件的修改事件：

```bash
inotifywait -m -e modify example.txt
```

当 `example.txt` 文件被修改时，命令行会输出类似以下内容：

```
example.txt MODIFY
```

### 示例 2：监控目录变化
以下命令将递归监控 `my_directory` 目录及其子目录的创建和删除事件：

```bash
inotifywait -m -r -e create -e delete my_directory
```

当在 `my_directory` 中创建或删除文件时，命令行会输出相应的事件信息。

## 提示
- 使用 `-m` 选项时，可以通过 `Ctrl+C` 来停止监控。
- 可以将 `inotifywait` 与其他命令结合使用，例如在文件变化时自动执行某个脚本。
- 监控大量文件或目录时，注意系统资源的使用，避免过度消耗。

通过使用 `inotifywait`，开发者和运维人员可以轻松实现对文件系统变化的实时监控，从而提高工作效率。