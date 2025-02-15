# [리눅스] Bash getenforce 사용법

## 概要
`getenforce` コマンドは、Linux システムにおける SELinux (Security-Enhanced Linux) の現在の動作モードを表示するためのコマンドです。SELinux は、アクセス制御を強化するためのセキュリティ機能であり、`getenforce` を使用することで、システムがどのようにセキュリティポリシーを適用しているかを確認できます。

## 使用法
基本的な構文は以下の通りです。

```bash
getenforce
```

このコマンドには特にオプションはありませんが、実行することで以下のいずれかの状態が返されます。

- **Enforcing**: SELinux が有効で、ポリシーが適用されている状態。
- **Permissive**: SELinux が有効だが、ポリシー違反がログに記録されるだけで、実際にはブロックされない状態。
- **Disabled**: SELinux が無効になっている状態。

## 例
以下に、`getenforce` コマンドの使用例を示します。

### 例 1: 現在の SELinux モードを確認する
```bash
$ getenforce
Enforcing
```
このコマンドを実行すると、現在の SELinux モードが "Enforcing" であることが表示されます。

### 例 2: スクリプト内での使用
```bash
if [ "$(getenforce)" == "Enforcing" ]; then
    echo "SELinux is enforcing."
else
    echo "SELinux is not enforcing."
fi
```
このスクリプトは、SELinux が "Enforcing" モードであるかどうかを確認し、その結果に応じてメッセージを表示します。

## ヒント
- SELinux の設定を変更する前に、`getenforce` を使用して現在のモードを確認することをお勧めします。これにより、システムのセキュリティ状態を理解し、適切な対策を講じることができます。
- SELinux のトラブルシューティングを行う際には、`getenforce` の結果を基に、必要に応じてモードを変更することを検討してください。