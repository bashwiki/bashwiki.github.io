# [日本] Bash netstat の使い方: ネットワーク接続の表示

## 概要
`netstat` コマンドは、ネットワーク接続、ルーティングテーブル、インターフェース統計など、ネットワークに関する情報を表示するためのツールです。このコマンドを使用することで、システムのネットワーク状態を把握することができます。

## 使用法
基本的な構文は以下の通りです。

```
netstat [オプション] [引数]
```

## 一般的なオプション
- `-a`: すべての接続とリスニングポートを表示します。
- `-t`: TCP接続を表示します。
- `-u`: UDP接続を表示します。
- `-n`: アドレスとポート番号を数値形式で表示します。
- `-l`: リスニング状態のソケットのみを表示します。
- `-p`: 各接続に関連するプロセスIDとプログラム名を表示します。

## 一般的な例
以下に、`netstat` コマンドのいくつかの実用的な例を示します。

### すべての接続を表示
```bash
netstat -a
```

### TCP接続を表示
```bash
netstat -t
```

### UDP接続を表示
```bash
netstat -u
```

### リスニングポートを表示
```bash
netstat -l
```

### 数値形式で表示
```bash
netstat -n
```

### プロセス情報を表示
```bash
netstat -p
```

## ヒント
- `netstat` コマンドは、特にネットワークトラブルシューティングやセキュリティ監視に役立ちます。
- `netstat` の出力を `grep` コマンドと組み合わせることで、特定の接続をフィルタリングできます。例えば、特定のポートを監視する場合は次のようにします。
  ```bash
  netstat -an | grep :80
  ```
- 定期的に `netstat` を実行し、ネットワークの状態を確認することで、異常な接続を早期に発見できます。