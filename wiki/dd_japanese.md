# [Linux] Bash dd 使用法: データのコピーと変換

## Overview
`dd` コマンドは、ファイルやデバイスのデータをコピーしたり、変換したりするための強力なツールです。特に、ブロックデバイスやイメージファイルの作成、バックアップ、復元に利用されます。

## Usage
基本的な構文は以下の通りです。

```bash
dd [オプション] [引数]
```

## Common Options
- `if=`: 入力ファイルを指定します。
- `of=`: 出力ファイルを指定します。
- `bs=`: ブロックサイズを指定します。
- `count=`: コピーするブロックの数を指定します。
- `status=`: 実行中の進捗状況を表示するオプション（例: `none`, `noxfer`, `progress`）。

## Common Examples
以下に、`dd` コマンドのいくつかの実用的な例を示します。

### 1. ファイルのコピー
```bash
dd if=source.txt of=destination.txt
```
このコマンドは、`source.txt` から `destination.txt` へデータをコピーします。

### 2. ISOイメージの作成
```bash
dd if=/dev/cdrom of=cd_image.iso bs=2048
```
CD-ROMから `cd_image.iso` というISOイメージを作成します。

### 3. ディスクのバックアップ
```bash
dd if=/dev/sda of=/dev/sdb bs=64K
```
`/dev/sda` から `/dev/sdb` へディスク全体をバックアップします。

### 4. データの消去
```bash
dd if=/dev/zero of=/dev/sda bs=1M
```
`/dev/sda` にゼロを書き込み、データを消去します。

## Tips
- `dd` コマンドを使用する際は、特に出力先を間違えないように注意してください。誤って重要なデータを上書きする可能性があります。
- 大きなファイルを扱う場合は、`status=progress` オプションを使って進捗状況を確認すると便利です。
- `dd` の実行結果を確認するために、`sync` コマンドを使用してバッファをフラッシュすることをお勧めします。