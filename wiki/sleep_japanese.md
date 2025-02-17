# [Linux] Bash sleep の使い方: プロセスの一時停止

## Overview
`sleep` コマンドは、指定した時間だけプロセスを一時停止させるために使用されます。このコマンドは、スクリプトやコマンドの実行を遅延させたい場合に便利です。

## Usage
基本的な構文は以下の通りです。

```bash
sleep [options] [arguments]
```

## Common Options
- `-m` : 分単位で指定します。
- `-s` : 秒単位で指定します（デフォルト）。
- `-h` : 時間単位で指定します。

## Common Examples
以下に、`sleep` コマンドの実用的な例をいくつか示します。

1. 5秒間の遅延を設定する:
   ```bash
   sleep 5
   ```

2. 2分間の遅延を設定する:
   ```bash
   sleep 2m
   ```

3. 1時間の遅延を設定する:
   ```bash
   sleep 1h
   ```

4. 複数の遅延を連続して実行する:
   ```bash
   echo "Starting process..."
   sleep 3
   echo "Process running..."
   sleep 2
   echo "Process completed."
   ```

## Tips
- スクリプト内で `sleep` を使用することで、特定のタスクの実行間隔を調整できます。
- 繰り返し処理の中で `sleep` を使うと、リソースの使用を抑えることができます。
- `sleep` の後に他のコマンドを続けることで、遅延を挟んだ処理を簡単に実行できます。