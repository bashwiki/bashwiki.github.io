# [Linux] Bash basename の使い方: ファイル名を取得する

## Overview
`basename` コマンドは、指定されたパスからファイル名を抽出するために使用されます。これにより、フルパスではなく、ファイル名だけを簡単に取得できます。

## Usage
基本的な構文は以下の通りです。

```bash
basename [options] [arguments]
```

## Common Options
- `-a` : 複数の引数を指定した場合、すべてのファイル名を表示します。
- `-s` : 指定したサフィックスを削除してファイル名を表示します。

## Common Examples
以下に、`basename` コマンドのいくつかの実用的な例を示します。

### 例 1: 単一のファイル名を取得
フルパスからファイル名を取得する基本的な例です。

```bash
basename /home/user/documents/file.txt
```
出力:
```
file.txt
```

### 例 2: 複数のファイル名を取得
`-a` オプションを使用して、複数のファイル名を同時に取得します。

```bash
basename -a /home/user/documents/file1.txt /home/user/documents/file2.txt
```
出力:
```
file1.txt
file2.txt
```

### 例 3: サフィックスを削除
`-s` オプションを使用して、特定のサフィックスを削除します。

```bash
basename -s .txt /home/user/documents/file.txt
```
出力:
```
file
```

## Tips
- `basename` コマンドはスクリプト内でファイル名を処理する際に非常に便利です。
- 複数のファイルを扱う場合は、`-a` オプションを活用して効率的に処理しましょう。
- サフィックスを削除する際は、正確なサフィックスを指定することが重要です。誤ったサフィックスを指定すると、期待通りの結果が得られないことがあります。