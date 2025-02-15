# [리눅스] Bash local 사용법

## 概要
`local` コマンドは、Bash スクリプト内でローカル変数を定義するために使用されます。ローカル変数は、関数内でのみ有効であり、関数が終了するとその変数は消失します。これにより、グローバル変数と衝突することなく、関数内でのデータの管理が容易になります。

## 使用法
`local` コマンドの基本的な構文は以下の通りです。

```bash
local VARIABLE_NAME=VALUE
```

ここで、`VARIABLE_NAME` は定義するローカル変数の名前であり、`VALUE` はその変数に割り当てる値です。

### 一般的なオプション
`local` コマンドには特にオプションはありませんが、変数を定義する際に以下のような特性を持たせることができます。

- `readonly`: 変数を読み取り専用にする。
- `declare`: 変数の型を指定する（例: 整数型）。

## 例
以下に、`local` コマンドを使用した実用的な例を示します。

### 例 1: 基本的なローカル変数の定義

```bash
function my_function {
    local my_var="Hello, World!"
    echo $my_var
}

my_function  # 出力: Hello, World!
echo $my_var # 出力: (何も表示されない)
```

この例では、`my_var` というローカル変数を定義し、関数内でのみアクセス可能です。関数の外からはアクセスできません。

### 例 2: ローカル変数とグローバル変数の衝突

```bash
global_var="I am global"

function another_function {
    local global_var="I am local"
    echo $global_var
}

another_function  # 出力: I am local
echo $global_var  # 出力: I am global
```

この例では、同じ名前の変数 `global_var` をローカルとグローバルで定義していますが、関数内ではローカル変数が優先されます。

## ヒント
- `local` を使用することで、関数内での変数のスコープを明確にし、コードの可読性を向上させることができます。
- 複雑なスクリプトを書く際には、ローカル変数を積極的に使用して、意図しない変数の衝突を避けることが重要です。
- 必要に応じて、`declare` コマンドを使用して変数の型を指定することで、より厳密な変数管理が可能になります。