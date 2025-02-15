# [리눅스] Bash selinuxenabled 사용법

## 概要
`selinuxenabled` コマンドは、システムで SELinux (Security-Enhanced Linux) が有効かどうかを確認するためのシンプルなツールです。SELinuxは、Linuxカーネルに組み込まれたセキュリティモジュールであり、アクセス制御を強化するために使用されます。このコマンドを使用することで、SELinuxの状態を簡単に確認できます。

## 使用法
基本的な構文は以下の通りです：

```bash
selinuxenabled
```

このコマンドは、SELinuxが有効な場合は何も出力せず、無効な場合は終了ステータス1を返します。特にオプションはありませんが、終了ステータスを利用してSELinuxの状態を確認することができます。

## 例
以下に、`selinuxenabled` コマンドの実用的な例を示します。

### 例 1: SELinuxの状態を確認する
```bash
if selinuxenabled; then
    echo "SELinuxは有効です。"
else
    echo "SELinuxは無効です。"
fi
```
このスクリプトは、SELinuxが有効かどうかを確認し、その結果に応じてメッセージを表示します。

### 例 2: SELinuxの状態をスクリプトで使用する
```bash
#!/bin/bash

if selinuxenabled; then
    echo "SELinuxが有効なので、セキュリティポリシーを確認してください。"
else
    echo "SELinuxが無効です。"
fi
```
このスクリプトは、SELinuxの状態に基づいて、ユーザーにセキュリティポリシーを確認するよう促します。

## ヒント
- `selinuxenabled` コマンドは、シェルスクリプト内での条件分岐に非常に便利です。SELinuxの状態に応じて異なる処理を実行する際に活用できます。
- SELinuxの設定を変更する場合は、システムのセキュリティに影響を与えるため、十分な注意を払って行ってください。
- SELinuxの詳細な設定や状態を確認するには、`sestatus` コマンドを併用することをお勧めします。