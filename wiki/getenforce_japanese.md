# [Linux] Bash getenforce 使用法: SELinuxの現在のモードを表示する

## Overview
`getenforce` コマンドは、SELinux（Security-Enhanced Linux）の現在の動作モードを表示します。このコマンドを使用することで、システムのセキュリティポリシーがどのように適用されているかを確認できます。

## Usage
基本的な構文は以下の通りです。

```bash
getenforce [options]
```

## Common Options
`getenforce` コマンドには特にオプションはありませんが、以下のような情報を得ることができます。

- `Enforcing`: SELinuxが有効で、ポリシーが適用されている状態。
- `Permissive`: SELinuxが無効ではないが、ポリシーは適用されず、違反がログに記録される状態。
- `Disabled`: SELinuxが無効になっている状態。

## Common Examples

### 現在のSELinuxモードを確認する
```bash
getenforce
```

### SELinuxのモードを確認し、結果を変数に格納する
```bash
mode=$(getenforce)
echo "現在のSELinuxモードは: $mode"
```

### SELinuxのモードを確認し、条件に応じてメッセージを表示する
```bash
if [ "$(getenforce)" = "Enforcing" ]; then
    echo "SELinuxは有効です。"
else
    echo "SELinuxは無効または許可モードです。"
fi
```

## Tips
- SELinuxのモードを確認することは、システムのセキュリティを維持するために重要です。
- `getenforce` コマンドは、スクリプト内で条件分岐を行う際に非常に便利です。
- SELinuxの設定を変更する場合は、`setenforce` コマンドを使用してモードを変更できますが、変更後は必ず `getenforce` で確認しましょう。