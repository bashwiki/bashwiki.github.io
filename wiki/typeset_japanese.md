# [Linux] Bash typeset の使い方: 変数の属性を設定する

## Overview
`typeset` コマンドは、Bash シェルで変数の属性を設定するために使用されます。このコマンドを使うことで、変数のスコープや型、オプションを指定することができます。

## Usage
基本的な構文は以下の通りです。

```bash
typeset [options] [arguments]
```

## Common Options
- `-i` : 変数を整数として扱う。
- `-r` : 変数を読み取り専用に設定する。
- `-x` : 変数を環境変数としてエクスポートする。
- `-a` : 配列変数を定義する。

## Common Examples

### 1. 整数変数の定義
```bash
typeset -i num=10
echo $num  # 出力: 10
```

### 2. 読み取り専用変数の設定
```bash
typeset -r constant=100
echo $constant  # 出力: 100
# constant=200  # エラー: constantは読み取り専用です
```

### 3. 環境変数のエクスポート
```bash
typeset -x PATH="/usr/local/bin:$PATH"
echo $PATH  # 新しいPATHが表示される
```

### 4. 配列の定義
```bash
typeset -a fruits
fruits=("apple" "banana" "cherry")
echo ${fruits[1]}  # 出力: banana
```

## Tips
- `typeset` は主にスクリプト内で使用されるため、スクリプトの可読性を向上させるために適切に利用しましょう。
- 変数のスコープを明確にすることで、予期しないエラーを防ぐことができます。
- 配列を使用する場合は、`-a` オプションを忘れずに指定しましょう。