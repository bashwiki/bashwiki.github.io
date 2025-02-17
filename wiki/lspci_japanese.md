# [Linux] Bash lspci の使い方: PCIデバイスの情報を表示する

## Overview
`lspci` コマンドは、Linuxシステム上で接続されているPCIデバイスの情報を表示するために使用されます。このコマンドを使うことで、ハードウェアの構成を確認したり、トラブルシューティングを行ったりすることができます。

## Usage
基本的な構文は以下の通りです。

```
lspci [options] [arguments]
```

## Common Options
- `-v` : 詳細情報を表示します。
- `-vv` : さらに詳細な情報を表示します。
- `-k` : ドライバ情報を表示します。
- `-n` : デバイスのIDを数値形式で表示します。
- `-s <bus:device.function>` : 特定のデバイスのみを表示します。

## Common Examples
以下は、`lspci` コマンドの実用的な例です。

### 1. 基本的なPCIデバイスのリスト表示
```bash
lspci
```

### 2. 詳細情報の表示
```bash
lspci -v
```

### 3. 特定のデバイスの情報を表示
```bash
lspci -s 00:1f.0
```

### 4. ドライバ情報の表示
```bash
lspci -k
```

### 5. 数値形式でのデバイスID表示
```bash
lspci -n
```

## Tips
- `lspci` の出力を `grep` と組み合わせることで、特定のデバイスを簡単に検索できます。例えば、NVIDIAのデバイスを探す場合は次のようにします。
  ```bash
  lspci | grep NVIDIA
  ```
- `lspci` の出力をファイルにリダイレクトして保存することもできます。例えば、次のコマンドで出力を `pci_devices.txt` に保存できます。
  ```bash
  lspci > pci_devices.txt
  ```
- `-t` オプションを使用すると、PCIデバイスのツリー構造を表示できます。これにより、デバイスの階層関係を視覚的に確認できます。
  ```bash
  lspci -t
  ```