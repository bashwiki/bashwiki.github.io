# [Linux] Bash let 使用法: 用於數學運算的命令

## Overview
`let` 命令是一個用於在 Bash 中執行數學運算的工具。它可以用來計算數值表達式，並將結果儲存到變數中。

## Usage
基本語法如下：

```bash
let [options] [arguments]
```

## Common Options
- `-n`：在運算之前不輸出結果。
- `-e`：如果運算結果為非零，則返回錯誤碼。

## Common Examples
以下是一些常見的使用範例：

1. **簡單加法運算**
   ```bash
   let result=5+3
   echo $result  # 輸出 8
   ```

2. **複雜運算**
   ```bash
   let total=10*2-5
   echo $total  # 輸出 15
   ```

3. **使用變數**
   ```bash
   a=10
   b=20
   let sum=a+b
   echo $sum  # 輸出 30
   ```

4. **自增運算**
   ```bash
   let count++
   echo $count  # 如果 count 初始為 0，則輸出 1
   ```

## Tips
- 確保變數已正確初始化，否則可能會導致意外的結果。
- 使用 `let` 時，可以省略空格，例如 `let x=5+3` 和 `let x = 5 + 3` 是等效的，但前者更為簡潔。
- `let` 命令不會自動輸出結果，如果需要查看結果，必須使用 `echo` 或其他輸出命令。