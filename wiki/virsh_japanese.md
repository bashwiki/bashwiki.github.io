# [Linux] Bash virsh の使い方: 仮想マシンの管理

## Overview
`virsh` コマンドは、仮想化環境を管理するためのコマンドラインツールです。主に、KVM（Kernel-based Virtual Machine）やXenなどの仮想化技術を使用しているシステムで、仮想マシンの作成、削除、起動、停止などを行うことができます。

## Usage
基本的な構文は以下の通りです。

```bash
virsh [options] [arguments]
```

## Common Options
- `list`: 現在実行中の仮想マシンのリストを表示します。
- `start <domain>`: 指定した仮想マシンを起動します。
- `shutdown <domain>`: 指定した仮想マシンをシャットダウンします。
- `destroy <domain>`: 指定した仮想マシンを強制的に停止します。
- `create <file>`: 指定したXMLファイルから新しい仮想マシンを作成します。
- `define <file>`: 定義ファイルを使って仮想マシンを登録します。

## Common Examples
以下は、`virsh` コマンドの実用的な例です。

### 実行中の仮想マシンのリストを表示
```bash
virsh list
```

### 仮想マシンを起動
```bash
virsh start my_vm
```

### 仮想マシンをシャットダウン
```bash
virsh shutdown my_vm
```

### 仮想マシンを強制停止
```bash
virsh destroy my_vm
```

### 新しい仮想マシンを作成
```bash
virsh create /path/to/my_vm.xml
```

### 仮想マシンの定義を登録
```bash
virsh define /path/to/my_vm.xml
```

## Tips
- `virsh` コマンドを使用する際は、適切な権限が必要です。通常、管理者権限で実行する必要があります。
- XMLファイルを使用して仮想マシンを定義する際は、正しいフォーマットを確認してください。誤ったフォーマットはエラーの原因になります。
- `virsh` のヘルプを確認するには、`virsh --help` を実行すると、利用可能なオプションやコマンドの一覧が表示されます。