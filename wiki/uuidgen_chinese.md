# [Linux] Bash uuidgen 用法: 生成唯一标识符

## 概述
`uuidgen` 命令用于生成 Universally Unique Identifiers (UUIDs)，这些标识符在分布式系统中非常有用，确保每个生成的 ID 都是唯一的。

## 用法
基本语法如下：
```bash
uuidgen [options] [arguments]
```

## 常用选项
- `-r`：生成随机 UUID。
- `-t`：生成基于时间的 UUID。
- `-h`：显示帮助信息。

## 常见示例
生成一个随机 UUID：
```bash
uuidgen
```

生成一个基于时间的 UUID：
```bash
uuidgen -t
```

生成多个 UUID：
```bash
uuidgen -n 5
```

## 提示
- 在需要唯一标识符的场景中使用 `uuidgen`，如数据库主键或文件名。
- 考虑使用 `-r` 选项生成随机 UUID，以增加安全性。
- 定期检查生成的 UUID 是否符合预期格式，以避免潜在的错误。