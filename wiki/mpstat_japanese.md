# [Linux] Bash mpstat の使い方: CPU 使用状況を監視する

## Overview
`mpstat` コマンドは、システムの CPU 使用状況を監視し、各 CPU コアのパフォーマンスを表示するために使用されます。これにより、システムの負荷やボトルネックを特定するのに役立ちます。

## Usage
基本的な構文は以下の通りです。

```bash
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`：全ての CPU コアの統計を表示します。
- `-u`：CPU 使用率を表示します。
- `-r`：I/O スタッツを表示します。
- `-h`：ヘルプメッセージを表示します。

## Common Examples
以下は、`mpstat` コマンドのいくつかの実用的な例です。

### 1. 全ての CPU コアの使用状況を表示
```bash
mpstat -P ALL
```

### 2. CPU 使用率を 1 秒ごとに表示
```bash
mpstat 1
```

### 3. 特定の CPU コアの使用状況を表示
```bash
mpstat -P 0 1
```

### 4. I/O スタッツを表示
```bash
mpstat -r
```

## Tips
- 定期的に `mpstat` を実行して、CPU 使用状況のトレンドを把握すると良いでしょう。
- スクリプトに組み込んで、特定の条件下での CPU 使用状況を自動的に記録することも可能です。
- `mpstat` の出力をグラフ化することで、視覚的にパフォーマンスを分析することができます。