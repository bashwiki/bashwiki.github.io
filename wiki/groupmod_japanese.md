# [Linux] Bash groupmod の使い方: グループの属性を変更する

## Overview
`groupmod` コマンドは、既存のグループの属性を変更するために使用されます。このコマンドを使用することで、グループ名やグループID (GID) を変更することができます。

## Usage
基本的な構文は以下の通りです。

```bash
groupmod [options] [arguments]
```

## Common Options
- `-n, --new-name NEW_GROUP`: グループの新しい名前を指定します。
- `-g, --gid GID`: グループの新しい GID を指定します。
- `-h, --help`: ヘルプ情報を表示します。
- `-o, --non-unique`: 非一意の GID を許可します。

## Common Examples
以下は、`groupmod` コマンドの実用的な例です。

### グループ名の変更
グループ名を `oldgroup` から `newgroup` に変更する場合:

```bash
groupmod -n newgroup oldgroup
```

### GIDの変更
グループの GID を 1001 から 1002 に変更する場合:

```bash
groupmod -g 1002 oldgroup
```

### 非一意の GIDの設定
非一意の GID を設定する場合:

```bash
groupmod -o -g 1002 oldgroup
```

## Tips
- グループ名や GID を変更する際は、他のユーザーやプロセスに影響を与えないよう注意してください。
- 変更後は、関連する設定ファイルやスクリプトも確認し、必要に応じて更新してください。
- `groupmod` コマンドを実行するには、通常、管理者権限が必要です。`sudo` を使用して実行することをお勧めします。