# [Linux] Bash local コマンド: シェル関数内での変数のスコープを制限する

## 概要
`local` コマンドは、シェル関数内で変数のスコープを制限するために使用されます。これにより、関数内で定義された変数が関数の外部に影響を与えないようにすることができます。

## 使用法
基本的な構文は以下の通りです。

```bash
local [options] [arguments]
```

## 一般的なオプション
- `name`: 定義するローカル変数の名前。
- `value`: ローカル変数に割り当てる値。

## 一般的な例
以下に、`local` コマンドのいくつかの実用的な例を示します。

### 例 1: 基本的なローカル変数の使用
```bash
my_function() {
    local my_var="Hello"
    echo $my_var
}

my_function  # 出力: Hello
echo $my_var  # 出力: (何も表示されない)
```

### 例 2: 複数のローカル変数
```bash
my_function() {
    local var1="Hello"
    local var2="World"
    echo "$var1 $var2"
}

my_function  # 出力: Hello World
```

### 例 3: ローカル変数のスコープ
```bash
my_function() {
    local count=5
    echo "Count inside function: $count"
}

my_function  # 出力: Count inside function: 5
echo "Count outside function: $count"  # 出力: (何も表示されない)
```

## ヒント
- `local` を使用することで、関数内の変数がグローバル変数と衝突するのを防ぎます。
- 複数の変数を一度に定義する場合、カンマで区切って記述することができます。
- `local` は関数内でのみ有効であり、関数が終了すると変数は消えます。これにより、スクリプトの可読性と保守性が向上します。