# [Linux] Bash kubectl 使用法: Kubernetes クラスターの管理

## Overview
`kubectl` は、Kubernetes クラスターを管理するためのコマンドラインツールです。このコマンドを使用することで、ポッドの作成、削除、更新、情報の取得など、さまざまな操作を行うことができます。

## Usage
基本的な構文は以下の通りです。

```
kubectl [options] [arguments]
```

## Common Options
- `--namespace`: 操作を行う名前空間を指定します。
- `-f`: YAML または JSON ファイルを指定してリソースを適用します。
- `--kubeconfig`: 使用する kubeconfig ファイルを指定します。
- `--context`: 使用するコンテキストを指定します。

## Common Examples
以下に、よく使われる `kubectl` コマンドの例を示します。

### ポッドの一覧を表示
```bash
kubectl get pods
```

### 特定の名前空間内のポッドを表示
```bash
kubectl get pods --namespace=my-namespace
```

### デプロイメントの作成
```bash
kubectl create deployment my-deployment --image=my-image
```

### リソースの削除
```bash
kubectl delete pod my-pod
```

### YAML ファイルからリソースを適用
```bash
kubectl apply -f my-deployment.yaml
```

## Tips
- `kubectl` コマンドを頻繁に使用する場合は、エイリアスを設定して短縮することを検討してください。
- `kubectl get` コマンドに `-o wide` オプションを追加すると、より詳細な情報が表示されます。
- リソースの状態を確認するために、`kubectl describe` コマンドを使用すると便利です。