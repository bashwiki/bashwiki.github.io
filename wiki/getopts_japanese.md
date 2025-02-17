# [Linux] Bash getopts の使い方: コマンドラインオプションの解析

## 概要
`getopts` コマンドは、シェルスクリプト内でコマンドラインオプションを解析するための便利なツールです。これにより、スクリプトに引数を渡し、オプションに基づいて異なる動作を実行することができます。

## 使用法
基本的な構文は次のとおりです。

```bash
getopts [options] [arguments]
```

## 一般的なオプション
- `-a` : オプションの解析を開始します。
- `-b` : オプションの引数を指定します。
- `-c` : オプションを無視します。

## 一般的な例
以下に、`getopts` を使用したいくつかの実用的な例を示します。

### 例 1: シンプルなオプション解析
```bash
#!/bin/bash

while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "オプション -a が指定されました"
      ;;
    b)
      echo "オプション -b が指定されました。引数: $OPTARG"
      ;;
    c)
      echo "オプション -c が指定されました。引数: $OPTARG"
      ;;
    *)
      echo "無効なオプション"
      ;;
  esac
done
```

### 例 2: 引数のデフォルト値を設定
```bash
#!/bin/bash

value="デフォルト"

while getopts "v:" opt; do
  case $opt in
    v)
      value=$OPTARG
      ;;
    *)
      echo "無効なオプション"
      ;;
  esac
done

echo "値: $value"
```

### 例 3: 複数オプションの処理
```bash
#!/bin/bash

while getopts "abc" opt; do
  case $opt in
    a)
      echo "オプション -a が指定されました"
      ;;
    b)
      echo "オプション -b が指定されました"
      ;;
    c)
      echo "オプション -c が指定されました"
      ;;
    *)
      echo "無効なオプション"
      ;;
  esac
done
```

## ヒント
- スクリプトの先頭で `OPTIND=1` を設定すると、オプションの解析をリセットできます。
- `getopts` は、オプションの引数が必要な場合、コロン `:` を使用して指定します。
- スクリプトの使用方法をユーザーに示すために、`-h` または `--help` オプションを追加することを検討してください。