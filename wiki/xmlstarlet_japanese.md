# [Linux] Bash xmlstarlet 使用法: XMLデータの操作

## Overview
xmlstarletは、XMLデータを操作するためのコマンドラインツールです。XML文書の解析、変換、検証、編集など、さまざまな操作を簡単に行うことができます。

## Usage
基本的な構文は以下の通りです。

```bash
xmlstarlet [options] [arguments]
```

## Common Options
- `sel`: XML文書から特定のノードを選択します。
- `ed`: XML文書を編集します。
- `val`: XML文書の検証を行います。
- `tr`: XML文書の変換を行います。
- `fo`: XML文書をフォーマットします。

## Common Examples
### 1. XMLノードの選択
特定のノードを選択する例です。

```bash
xmlstarlet sel -t -m "//book" -v "title" -n books.xml
```

### 2. XML文書の編集
特定のノードの値を変更する例です。

```bash
xmlstarlet ed -u "//book/title" -v "新しいタイトル" books.xml
```

### 3. XML文書の検証
XML文書が正しいかどうかを検証する例です。

```bash
xmlstarlet val -e books.xml
```

### 4. XML文書のフォーマット
XML文書を整形して表示する例です。

```bash
xmlstarlet fo books.xml
```

## Tips
- XML文書を操作する前に、必ずバックアップを取っておくことをお勧めします。
- 複雑な操作を行う場合は、xmlstarletのマニュアルを参照して、詳細なオプションを確認してください。
- スクリプト内でxmlstarletを使用することで、XMLデータの自動処理を効率化できます。