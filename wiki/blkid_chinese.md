# [Linux] Bash blkid 使用说明: 显示块设备的UUID和文件系统类型

## 概述
`blkid` 命令用于查找和显示块设备的属性，包括设备的UUID（通用唯一识别码）、文件系统类型等信息。它通常用于识别存储设备，以便在系统中进行管理和配置。

## 用法
基本语法如下：
```bash
blkid [options] [arguments]
```

## 常用选项
- `-o, --output`: 指定输出格式，例如 `value`、`full`、`list` 等。
- `-s, --match-tag`: 仅显示匹配特定标签的设备信息。
- `-p, --probe`: 强制探测设备信息，即使设备未挂载。
- `-c, --cache`: 使用或更新缓存文件。

## 常见示例
1. 显示所有块设备的信息：
   ```bash
   blkid
   ```

2. 显示特定设备的UUID和文件系统类型：
   ```bash
   blkid /dev/sda1
   ```

3. 以特定格式输出UUID：
   ```bash
   blkid -o value -s UUID /dev/sda1
   ```

4. 仅显示文件系统类型：
   ```bash
   blkid -o value -s TYPE /dev/sda1
   ```

5. 强制探测未挂载的设备信息：
   ```bash
   blkid -p /dev/sdb
   ```

## 提示
- 使用 `blkid` 时，确保你有足够的权限来访问块设备，通常需要以超级用户身份运行。
- 可以将 `blkid` 的输出与其他命令结合使用，例如通过管道将结果传递给 `grep` 进行过滤。
- 定期检查块设备的UUID和文件系统类型，以确保系统配置的正确性。