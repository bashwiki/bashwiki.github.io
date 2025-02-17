# [Linux] Bash ufw 使用法: ファイアウォールの管理

## Overview
`ufw`（Uncomplicated Firewall）は、Linuxシステムにおけるファイアウォールの設定と管理を簡素化するためのコマンドラインツールです。ユーザーが簡単にファイアウォールのルールを追加、削除、表示できるように設計されています。

## Usage
基本的な構文は以下の通りです。

```
ufw [options] [arguments]
```

## Common Options
- `enable`：ufwを有効にします。
- `disable`：ufwを無効にします。
- `status`：現在のファイアウォールの状態を表示します。
- `allow`：特定のポートまたはサービスへのアクセスを許可します。
- `deny`：特定のポートまたはサービスへのアクセスを拒否します。
- `delete`：既存のルールを削除します。

## Common Examples
以下は、`ufw`コマンドの一般的な使用例です。

### 1. ufwの有効化
```bash
sudo ufw enable
```

### 2. ufwの無効化
```bash
sudo ufw disable
```

### 3. 現在のファイアウォールの状態を確認
```bash
sudo ufw status
```

### 4. ポート22（SSH）へのアクセスを許可
```bash
sudo ufw allow 22
```

### 5. HTTP（ポート80）へのアクセスを許可
```bash
sudo ufw allow http
```

### 6. 特定のIPアドレスからのアクセスを拒否
```bash
sudo ufw deny from 192.168.1.100
```

### 7. ルールの削除
```bash
sudo ufw delete allow 22
```

## Tips
- ルールを追加する前に、`ufw status`で現在の設定を確認することをお勧めします。
- `ufw`を使用する際は、特にSSHの設定に注意し、誤って自分自身をロックアウトしないようにしましょう。
- 定期的にファイアウォールの設定を見直し、不要なルールを削除することが重要です。