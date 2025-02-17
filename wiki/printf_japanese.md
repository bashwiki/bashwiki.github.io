# [Linux] Bash printf の使い方: フォーマットされた出力を表示する

## Overview
`printf` コマンドは、フォーマットされた出力を生成するために使用されます。C言語の `printf` 関数に似た機能を持ち、さまざまなデータ型を指定した形式で表示することができます。

## Usage
基本的な構文は以下の通りです。

```bash
printf [options] [arguments]
```

## Common Options
- `-v var`: 指定した変数に出力を格納します。
- `-f format`: 出力のフォーマットを指定します。
- `--help`: 使用方法を表示します。

## Common Examples
以下は、`printf` コマンドの実用的な例です。

### 例1: 基本的な文字列の出力
```bash
printf "Hello, World!\n"
```

### 例2: 整数のフォーマット
```bash
printf "Number: %d\n" 42
```

### 例3: 浮動小数点数のフォーマット
```bash
printf "Pi: %.2f\n" 3.14159
```

### 例4: 複数の引数を使用
```bash
printf "Name: %s, Age: %d\n" "Alice" 30
```

### 例5: 変数を使用した出力
```bash
name="Bob"
age=25
printf "Name: %s, Age: %d\n" "$name" "$age"
```

## Tips
- フォーマット指定子を正しく使用することで、出力を柔軟にカスタマイズできます。
- エスケープシーケンス（例: `\n`）を使用して改行やタブを追加できます。
- 変数を使用する際は、ダブルクオートで囲むことを忘れないでください。これにより、空白を含む文字列も正しく処理されます。