# [Linux] Bash cmake の使い方: プロジェクトのビルド設定を行う

## 概要
`cmake` コマンドは、ソフトウェアプロジェクトのビルド設定を行うためのツールです。CMakeは、プラットフォームに依存しないビルドシステムを生成するために使用され、さまざまなコンパイラやビルドツールと連携します。

## 使用法
基本的な構文は以下の通りです。

```bash
cmake [オプション] [引数]
```

## 一般的なオプション
- `-S <source_dir>`: ソースディレクトリを指定します。
- `-B <build_dir>`: ビルドディレクトリを指定します。
- `-D <var>=<value>`: CMake変数に値を設定します。
- `--build <build_dir>`: 指定したビルドディレクトリでビルドを実行します。
- `--target <target>`: 特定のターゲットをビルドします。

## 一般的な例
以下に、`cmake` コマンドの実用的な例を示します。

### 1. ソースディレクトリからビルドディレクトリを生成する
```bash
cmake -S . -B build
```

### 2. ビルドディレクトリでプロジェクトをビルドする
```bash
cmake --build build
```

### 3. CMake変数を設定してビルドする
```bash
cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
```

### 4. 特定のターゲットをビルドする
```bash
cmake --build build --target my_target
```

## ヒント
- CMakeの設定ファイル（CMakeLists.txt）は、プロジェクトのルートに配置してください。
- ビルドタイプ（Debug/Release）を指定することで、最適化やデバッグ情報の生成を制御できます。
- `ccmake` や `cmake-gui` を使用すると、インタラクティブに設定を変更できます。