# [Linux] Bash cat 使用法: ファイルの内容を表示する

## Overview
`cat` コマンドは、ファイルの内容を標準出力に表示するためのコマンドです。複数のファイルを連結して表示することもでき、ファイルの内容を簡単に確認するのに便利です。

## Usage
基本的な構文は次の通りです。

```bash
cat [options] [arguments]
```

## Common Options
- `-n`: 行番号を付けて表示します。
- `-b`: 空でない行にのみ行番号を付けます。
- `-E`: 行の終わりに `$` を表示します。
- `-s`: 連続する空行を1行にまとめて表示します。

## Common Examples
以下は、`cat` コマンドの一般的な使用例です。

### 1. 単一ファイルの表示
```bash
cat filename.txt
```

### 2. 複数ファイルの連結表示
```bash
cat file1.txt file2.txt
```

### 3. 行番号を付けて表示
```bash
cat -n filename.txt
```

### 4. 空行を無視して行番号を付ける
```bash
cat -b filename.txt
```

### 5. 行の終わりに `$` を表示
```bash
cat -E filename.txt
```

## Tips
- 大きなファイルを表示する際は、`less` コマンドと組み合わせて使用すると便利です。例えば、`cat filename.txt | less` とすることで、ページ単位でスクロールできます。
- 複数のファイルを結合して新しいファイルを作成したい場合は、リダイレクトを使用します。例: `cat file1.txt file2.txt > combined.txt`。
- `cat` コマンドはファイルの内容を確認するだけでなく、パイプを使って他のコマンドと組み合わせることもできます。