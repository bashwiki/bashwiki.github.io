# [Linux] Bash trap 使用法: シグナルを捕捉する

## Overview
`trap` コマンドは、シェルスクリプト内で特定のシグナルやイベントを捕捉し、それに対して指定したコマンドを実行するために使用されます。これにより、スクリプトが終了する前にクリーンアップ処理を行ったり、特定の条件下での動作を制御したりすることができます。

## Usage
基本的な構文は以下の通りです。

```bash
trap [commands] [signals]
```

## Common Options
- `EXIT`: スクリプトが終了する際に実行されるコマンドを指定します。
- `SIGINT`: Ctrl+C で送信される割り込みシグナルを捕捉します。
- `SIGTERM`: プロセス終了のためのシグナルを捕捉します。
- `DEBUG`: 各コマンドの実行前に指定したコマンドを実行します。

## Common Examples

### 1. スクリプト終了時のクリーンアップ
スクリプトが終了する際に特定のコマンドを実行する例です。

```bash
trap 'echo "Cleaning up..."; rm -f temp_file' EXIT
```

### 2. Ctrl+C での割り込み処理
ユーザーが Ctrl+C を押したときにメッセージを表示する例です。

```bash
trap 'echo "Interrupted! Exiting..."' SIGINT
```

### 3. プロセス終了時の処理
SIGTERM シグナルを捕捉して特定の処理を行う例です。

```bash
trap 'echo "Received SIGTERM, shutting down..."' SIGTERM
```

### 4. デバッグ用のコマンド実行
各コマンドの実行前にデバッグ情報を表示する例です。

```bash
trap 'echo "Executing command: $BASH_COMMAND"' DEBUG
```

## Tips
- `trap` を使用することで、スクリプトの信頼性を向上させることができます。特に、リソースの解放やログの記録に役立ちます。
- 複数のシグナルを同時に捕捉することも可能です。例えば、`trap 'commands' SIGINT SIGTERM` のように指定できます。
- スクリプトの最初に `trap` を設定することで、予期しない終了時にも適切な処理を行うことができます。