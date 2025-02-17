# [Linux] Bash wget の使い方: ウェブからファイルをダウンロードする

## Overview
`wget` コマンドは、ウェブからファイルをダウンロードするための強力なツールです。HTTP、HTTPS、FTPなどのプロトコルを使用して、リモートサーバーからデータを取得することができます。

## Usage
基本的な構文は以下の通りです。

```bash
wget [options] [arguments]
```

## Common Options
- `-O [filename]`: ダウンロードしたファイルの名前を指定します。
- `-c`: 中断したダウンロードを再開します。
- `-r`: 指定したURLを再帰的にダウンロードします。
- `-q`: 静かなモードで実行し、進行状況を表示しません。
- `--limit-rate=[rate]`: ダウンロード速度を制限します。

## Common Examples
以下は、`wget` コマンドの一般的な使用例です。

### 単一ファイルのダウンロード
```bash
wget http://example.com/file.zip
```

### ファイル名を指定してダウンロード
```bash
wget -O myfile.zip http://example.com/file.zip
```

### 中断したダウンロードの再開
```bash
wget -c http://example.com/largefile.zip
```

### 再帰的にダウンロード
```bash
wget -r http://example.com/directory/
```

### ダウンロード速度を制限
```bash
wget --limit-rate=200k http://example.com/largefile.zip
```

## Tips
- 大きなファイルをダウンロードする際は、`-c` オプションを使用して中断した場合に再開できるようにしましょう。
- `-q` オプションを使用すると、スクリプトでの使用時に出力を抑えることができます。
- 再帰的ダウンロードを行う際は、必要なファイルだけをダウンロードするように注意しましょう。