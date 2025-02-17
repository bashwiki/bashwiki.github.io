# [Linux] Bash curl の使い方: HTTP リクエストを送信する

## Overview
`curl` コマンドは、URL を通じてデータを転送するためのツールです。主に HTTP、HTTPS、FTP などのプロトコルを使用して、リモートサーバーと通信する際に利用されます。

## Usage
基本的な構文は以下の通りです。

```bash
curl [options] [arguments]
```

## Common Options
- `-X`: 使用する HTTP メソッドを指定します（例: GET, POST）。
- `-d`: POST リクエストで送信するデータを指定します。
- `-H`: リクエストヘッダーを追加します。
- `-o`: 出力ファイル名を指定します。
- `-I`: HTTP ヘッダーのみを取得します。

## Common Examples
以下は、`curl` コマンドの実用的な例です。

### 1. 基本的な GET リクエスト
```bash
curl https://www.example.com
```

### 2. POST リクエストの送信
```bash
curl -X POST -d "name=John&age=30" https://www.example.com/api
```

### 3. ヘッダーを追加したリクエスト
```bash
curl -H "Authorization: Bearer token" https://www.example.com/protected
```

### 4. 出力をファイルに保存
```bash
curl -o output.html https://www.example.com
```

### 5. HTTP ヘッダーのみを取得
```bash
curl -I https://www.example.com
```

## Tips
- `-v` オプションを使用すると、詳細なリクエストとレスポンスの情報が表示されます。
- `-L` オプションを追加すると、リダイレクトを自動的に追跡します。
- API にアクセスする際は、適切な認証情報をヘッダーに含めることを忘れないでください。