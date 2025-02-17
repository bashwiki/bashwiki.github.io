# [Linux] Bash uuidgen 使用法: UUIDを生成する

## Overview
`uuidgen` コマンドは、ユニークな識別子（UUID）を生成するためのツールです。UUIDは、特定のオブジェクトやエンティティを一意に識別するために使用されます。

## Usage
基本的な構文は以下の通りです。

```
uuidgen [options] [arguments]
```

## Common Options
- `-r` : ランダムに生成されたUUIDを作成します。
- `-t` : 時間ベースのUUIDを生成します。

## Common Examples
- 単純なUUIDの生成:
  ```bash
  uuidgen
  ```

- ランダムUUIDの生成:
  ```bash
  uuidgen -r
  ```

- 時間ベースのUUIDの生成:
  ```bash
  uuidgen -t
  ```

## Tips
- UUIDは、データベースの主キーやセッションIDなど、ユニークな識別子が必要な場面で非常に便利です。
- UUIDを生成する際は、必要に応じてランダムまたは時間ベースのオプションを選択してください。