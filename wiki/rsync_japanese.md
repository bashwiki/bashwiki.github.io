# [Linux] Bash rsync の使い方: ファイルの同期と転送

## Overview
`rsync` コマンドは、ファイルやディレクトリを効率的に同期および転送するためのツールです。ローカルとリモートの両方で使用でき、変更された部分のみを転送するため、ネットワーク帯域幅を節約できます。

## Usage
基本的な構文は以下の通りです。

```bash
rsync [options] [source] [destination]
```

## Common Options
- `-a` : アーカイブモード。ファイルの属性を保持しながら、再帰的にコピーします。
- `-v` : 詳細モード。進行状況を表示します。
- `-z` : 転送中にデータを圧縮します。
- `-r` : ディレクトリを再帰的にコピーします。
- `--delete` : 送信先に存在しないファイルを削除します。

## Common Examples
- **ローカルディレクトリの同期**
  ```bash
  rsync -av /path/to/source/ /path/to/destination/
  ```

- **リモートサーバーへのファイル転送**
  ```bash
  rsync -avz /path/to/local/file user@remote_host:/path/to/remote/directory/
  ```

- **リモートサーバーからのファイル取得**
  ```bash
  rsync -avz user@remote_host:/path/to/remote/file /path/to/local/directory/
  ```

- **削除オプションを使用して同期**
  ```bash
  rsync -av --delete /path/to/source/ /path/to/destination/
  ```

## Tips
- `-n` オプションを使って、実際に転送する前にどのファイルが同期されるかを確認できます。
- 大きなファイルを転送する場合は、`--progress` オプションを追加すると、進行状況が表示されます。
- SSHを使用して安全にリモートサーバーに接続する場合は、`-e ssh` オプションを追加します。