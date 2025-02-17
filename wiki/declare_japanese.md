# [Linux] Bash declare の使い方: 変数の属性を設定する

## Overview
`declare` コマンドは、Bash シェルにおいて変数の属性を設定するために使用されます。このコマンドを使うことで、変数を特定のデータ型に指定したり、配列を宣言したりすることができます。

## Usage
基本的な構文は次の通りです。

```bash
declare [options] [arguments]
```

## Common Options
- `-a`: 配列変数を宣言します。
- `-i`: 整数変数を宣言します。数値演算が自動的に行われます。
- `-r`: 読み取り専用変数を宣言します。変更できません。
- `-x`: 環境変数としてエクスポートします。

## Common Examples

### 配列の宣言
```bash
declare -a fruits
fruits=("apple" "banana" "cherry")
echo ${fruits[1]}  # 出力: banana
```

### 整数変数の宣言
```bash
declare -i num
num=5
num=num+10
echo $num  # 出力: 15
```

### 読み取り専用変数の宣言
```bash
declare -r pi=3.14
echo $pi  # 出力: 3.14
# pi=3.14159  # エラー: piは読み取り専用です
```

### 環境変数の宣言
```bash
declare -x MY_VAR="Hello, World!"
echo $MY_VAR  # 出力: Hello, World!
```

## Tips
- 変数を宣言する際は、必要に応じて属性を設定することで、意図しない変更を防ぐことができます。
- 配列を使用する場合は、`declare -a` を使うことで、配列の要素を簡単に管理できます。
- 整数演算を行う場合は、`declare -i` を使用すると便利です。