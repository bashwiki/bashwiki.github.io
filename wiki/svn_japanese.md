# [Linux] Bash svn 使用法: バージョン管理システム

## Overview
`svn`（Subversion）は、ソースコードやドキュメントなどのファイルのバージョン管理を行うためのツールです。複数のユーザーが同じプロジェクトで作業する際に、変更履歴を追跡し、ファイルのバージョンを管理することができます。

## Usage
基本的な構文は以下の通りです。

```bash
svn [options] [arguments]
```

## Common Options
- `checkout`: リポジトリから作業コピーを取得します。
- `commit`: 変更をリポジトリに送信します。
- `update`: 作業コピーをリポジトリの最新の状態に更新します。
- `add`: 新しいファイルやディレクトリをリポジトリに追加します。
- `delete`: リポジトリからファイルやディレクトリを削除します。
- `status`: 作業コピーの変更状況を表示します。

## Common Examples
以下は、`svn`コマンドのいくつかの実用的な例です。

### リポジトリから作業コピーを取得する
```bash
svn checkout https://example.com/svn/myproject/trunk
```

### 変更をリポジトリに送信する
```bash
svn commit -m "修正内容を説明するメッセージ"
```

### 作業コピーを更新する
```bash
svn update
```

### 新しいファイルをリポジトリに追加する
```bash
svn add newfile.txt
svn commit -m "新しいファイルを追加"
```

### ファイルをリポジトリから削除する
```bash
svn delete oldfile.txt
svn commit -m "古いファイルを削除"
```

### 作業コピーの変更状況を表示する
```bash
svn status
```

## Tips
- 変更をコミットする前に、必ず`svn update`を実行して最新の状態を取得しましょう。
- コミットメッセージは明確に書くことで、後から変更履歴を見たときに理解しやすくなります。
- 定期的に作業コピーの状態を確認し、不要なファイルを削除することで、リポジトリをクリーンに保ちましょう。