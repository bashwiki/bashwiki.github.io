# [台灣] Bash brew 用法: 安裝和管理軟體包

## Overview
`brew` 是一個包管理工具，主要用於 macOS 和 Linux 系統。它可以幫助用戶輕鬆地安裝、更新和管理各種開源軟體包。

## Usage
基本語法如下：
```bash
brew [options] [arguments]
```

## Common Options
- `install`: 安裝指定的軟體包。
- `update`: 更新 Homebrew 自身及其已安裝的包的資訊。
- `upgrade`: 升級已安裝的軟體包到最新版本。
- `remove`: 移除指定的軟體包。
- `list`: 列出所有已安裝的軟體包。

## Common Examples
以下是一些常見的用法示例：

1. 安裝一個軟體包：
   ```bash
   brew install wget
   ```

2. 更新 Homebrew 和已安裝的包：
   ```bash
   brew update
   ```

3. 升級所有已安裝的軟體包：
   ```bash
   brew upgrade
   ```

4. 移除一個軟體包：
   ```bash
   brew remove wget
   ```

5. 列出所有已安裝的軟體包：
   ```bash
   brew list
   ```

## Tips
- 在安裝新軟體包之前，建議先執行 `brew update` 以確保獲得最新的包資訊。
- 使用 `brew search <package>` 可以快速查找可用的軟體包。
- 定期執行 `brew cleanup` 來清理不再需要的舊版本，釋放磁碟空間。