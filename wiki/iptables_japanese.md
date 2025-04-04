# [Linux] Bash iptables の使い方: ネットワークトラフィックのフィルタリング

## 概要
`iptables` コマンドは、Linux システムにおけるネットワークトラフィックのフィルタリングを管理するためのツールです。これにより、特定のトラフィックを許可または拒否するルールを設定し、セキュリティを強化することができます。

## 使用法
基本的な構文は以下の通りです。

```bash
iptables [options] [arguments]
```

## 一般的なオプション
- `-A` : ルールをチェーンの末尾に追加します。
- `-D` : ルールをチェーンから削除します。
- `-L` : 現在のルールをリスト表示します。
- `-F` : すべてのルールをフラッシュ（削除）します。
- `-P` : デフォルトポリシーを設定します。

## 一般的な例
以下にいくつかの実用的な例を示します。

### 1. すべてのトラフィックを拒否する
```bash
iptables -P INPUT DROP
```

### 2. 特定のポート（例: 80番ポート）へのアクセスを許可する
```bash
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

### 3. 現在のルールを表示する
```bash
iptables -L
```

### 4. ルールを削除する
```bash
iptables -D INPUT -p tcp --dport 80 -j ACCEPT
```

### 5. すべてのルールをフラッシュする
```bash
iptables -F
```

## ヒント
- ルールを設定する前に、現在の設定をバックアップすることをお勧めします。
- 変更を加えた後は、必ずルールを確認して、意図した通りに機能しているか確認してください。
- `iptables` の設定は再起動後に失われる場合があるため、永続化する方法を検討してください。