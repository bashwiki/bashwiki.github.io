# [Linux] Bash ip コマンドの使い方: ネットワークインターフェースの管理

## Overview
`ip` コマンドは、Linuxシステムにおけるネットワークインターフェースの管理や設定を行うための強力なツールです。このコマンドを使用することで、ネットワークデバイスの状態を確認したり、IPアドレスを設定したり、ルーティングテーブルを管理したりすることができます。

## Usage
基本的な構文は以下の通りです。

```
ip [options] [arguments]
```

## Common Options
- `link`: ネットワークインターフェースの状態を表示または管理します。
- `addr`: IPアドレスの表示や設定を行います。
- `route`: ルーティングテーブルの表示や設定を行います。
- `neigh`: ARPテーブルの表示や管理を行います。

## Common Examples
以下は、`ip` コマンドの一般的な使用例です。

### ネットワークインターフェースの一覧表示
```bash
ip link show
```

### IPアドレスの確認
```bash
ip addr show
```

### 特定のインターフェースにIPアドレスを追加
```bash
ip addr add 192.168.1.10/24 dev eth0
```

### 特定のインターフェースのIPアドレスを削除
```bash
ip addr del 192.168.1.10/24 dev eth0
```

### ルーティングテーブルの表示
```bash
ip route show
```

### 新しいルートの追加
```bash
ip route add 10.0.0.0/24 via 192.168.1.1
```

## Tips
- `ip` コマンドは非常に強力ですが、誤った設定を行うとネットワークに影響を与える可能性があるため、使用する際は注意が必要です。
- `ip` コマンドのオプションや引数については、`man ip` コマンドで詳細なマニュアルを確認できます。
- スクリプト内で使用する場合は、出力をパイプで他のコマンドに渡すことができるため、柔軟なネットワーク管理が可能です。