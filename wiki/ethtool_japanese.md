# [Linux] Bash ethtool の使い方: ネットワークインターフェースの設定と情報取得

## Overview
`ethtool` コマンドは、Linux システムにおけるネットワークインターフェースの設定や情報取得を行うためのツールです。主にイーサネットデバイスのパラメータを表示したり、変更したりするために使用されます。

## Usage
基本的な構文は次の通りです。

```bash
ethtool [options] [arguments]
```

## Common Options
- `-h`, `--help`: ヘルプメッセージを表示します。
- `-s`, `--set`: デバイスの設定を変更します。
- `-i`, `--driver`: ドライバ情報を表示します。
- `-p`, `--identify`: ネットワークインターフェースを識別するためのLEDを点灯させます。
- `-d`, `--dump`: デバイスのレジスタをダンプします。

## Common Examples
以下は、`ethtool` コマンドの実用的な例です。

1. ネットワークインターフェースの情報を表示する：
   ```bash
   ethtool eth0
   ```

2. ドライバ情報を表示する：
   ```bash
   ethtool -i eth0
   ```

3. ネットワークインターフェースの速度を設定する：
   ```bash
   ethtool -s eth0 speed 100 duplex full autoneg off
   ```

4. インターフェースのLEDを点灯させて識別する：
   ```bash
   ethtool -p eth0
   ```

5. デバイスのレジスタ情報をダンプする：
   ```bash
   ethtool -d eth0
   ```

## Tips
- `ethtool` を使用する際は、管理者権限が必要な場合があります。必要に応じて `sudo` を付けて実行してください。
- ネットワークのトラブルシューティングを行う際に、`ethtool` で取得した情報は非常に役立ちます。
- 設定を変更する前に、現在の設定を確認しておくことをお勧めします。