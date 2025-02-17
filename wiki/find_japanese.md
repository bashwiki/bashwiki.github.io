# [Linux] Bash find コマンド: ファイル名を検索する

## Overview
`find` コマンドは、指定したディレクトリ内でファイルやディレクトリを検索するための強力なツールです。条件を指定することで、特定のファイルを効率的に見つけることができます。

## Usage
基本的な構文は以下の通りです。

```bash
find [options] [arguments]
```

## Common Options
- `-name <pattern>`: 指定したパターンに一致するファイル名を検索します。
- `-type <type>`: 検索するファイルのタイプを指定します（例: `f` は通常のファイル、`d` はディレクトリ）。
- `-size <n>`: サイズが指定した値のファイルを検索します（例: `+100M` は100MB以上のファイル）。
- `-mtime <n>`: 最終更新日が指定した日数前のファイルを検索します（例: `-mtime -7` は過去7日以内に更新されたファイル）。
- `-exec <command> {} \;`: 見つかったファイルに対して指定したコマンドを実行します。

## Common Examples
以下にいくつかの実用的な例を示します。

### 1. 特定の名前のファイルを検索
```bash
find /path/to/directory -name "example.txt"
```

### 2. ディレクトリ内のすべてのJPEGファイルを検索
```bash
find /path/to/directory -type f -name "*.jpg"
```

### 3. 100MB以上のファイルを検索
```bash
find /path/to/directory -type f -size +100M
```

### 4. 過去7日以内に更新されたファイルを検索
```bash
find /path/to/directory -type f -mtime -7
```

### 5. 見つかったファイルを削除
```bash
find /path/to/directory -type f -name "*.tmp" -exec rm {} \;
```

## Tips
- 検索を効率化するために、必要なオプションを組み合わせて使用しましょう。
- 大量のファイルを扱う場合、`-print` オプションを使って出力を確認すると良いでしょう。
- `-exec` オプションを使用する際は、コマンドの実行結果に注意してください。特に削除コマンドを使用する場合は慎重に行いましょう。