# [Linux] Bash readonly 使用法: 変数を変更不可にする

## Overview
`readonly` コマンドは、シェル変数を変更不可にするために使用されます。このコマンドを使うことで、特定の変数が意図しない変更を受けるのを防ぎ、スクリプトの安定性を向上させることができます。

## Usage
基本的な構文は以下の通りです。

```bash
readonly [options] [arguments]
```

## Common Options
- `-p`: 現在の readonly 変数のリストを表示します。

## Common Examples

### 例1: 変数を readonly に設定する
```bash
MY_VAR="Hello"
readonly MY_VAR
```
このコマンドにより、`MY_VAR` 変数は変更不可になります。

### 例2: readonly 変数を表示する
```bash
readonly -p
```
このコマンドは、現在の readonly 変数のリストを表示します。

### 例3: readonly 変数の変更を試みる
```bash
MY_VAR="Hello"
readonly MY_VAR
MY_VAR="World"  # これはエラーになります
```
このコマンドを実行すると、`MY_VAR` を変更しようとした際にエラーが発生します。

## Tips
- `readonly` を使用する際は、変数名が他のスクリプトやシェル環境で使用されていないことを確認してください。
- スクリプトの重要な設定値や定数を `readonly` に設定することで、意図しない変更を防ぐことができます。
- `readonly` で設定した変数は、スクリプトの他の部分でも変更できないため、慎重に使用してください。