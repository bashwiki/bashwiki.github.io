# [Linux] Bash usermod の使い方: ユーザーアカウントの変更

## Overview
`usermod` コマンドは、Linux システムにおけるユーザーアカウントの属性を変更するために使用されます。このコマンドを使用することで、ユーザーのグループ、ホームディレクトリ、シェルなどを簡単に変更できます。

## Usage
基本的な構文は以下の通りです。

```bash
usermod [options] [username]
```

## Common Options
- `-aG` : 指定したグループにユーザーを追加します（既存のグループを保持）。
- `-d` : ユーザーのホームディレクトリを変更します。
- `-s` : ユーザーのログインシェルを変更します。
- `-l` : ユーザー名を変更します。
- `-g` : ユーザーの主グループを変更します。

## Common Examples
以下は、`usermod` コマンドの実用的な例です。

### ユーザーをグループに追加する
```bash
usermod -aG sudo username
```
このコマンドは、`username` を `sudo` グループに追加します。

### ユーザーのホームディレクトリを変更する
```bash
usermod -d /new/home/directory username
```
このコマンドは、`username` のホームディレクトリを `/new/home/directory` に変更します。

### ユーザーのログインシェルを変更する
```bash
usermod -s /bin/zsh username
```
このコマンドは、`username` のログインシェルを `/bin/zsh` に変更します。

### ユーザー名を変更する
```bash
usermod -l newusername oldusername
```
このコマンドは、`oldusername` を `newusername` に変更します。

## Tips
- `usermod` コマンドを実行するには、通常、管理者権限（root）が必要です。
- 変更を適用するために、ユーザーがログインしている場合は、再ログインが必要です。
- グループの変更を行う際は、`-aG` オプションを忘れずに使用し、既存のグループを保持してください。