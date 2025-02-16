# [台灣] Bash kubectl 用法: 管理 Kubernetes 叢集

## Overview
`kubectl` 是 Kubernetes 的命令行工具，讓使用者可以與 Kubernetes 叢集進行互動。透過 `kubectl`，使用者可以執行各種操作，例如部署應用程式、檢查叢集狀態、管理資源等。

## Usage
基本語法如下：
```
kubectl [options] [arguments]
```

## Common Options
- `get`: 獲取資源的列表或詳細資訊。
- `apply`: 應用配置變更到資源。
- `delete`: 刪除指定的資源。
- `describe`: 顯示資源的詳細資訊。
- `logs`: 查看 Pod 的日誌。

## Common Examples
以下是一些常見的 `kubectl` 使用範例：

1. 獲取所有 Pod 的列表：
   ```bash
   kubectl get pods
   ```

2. 應用配置檔案：
   ```bash
   kubectl apply -f deployment.yaml
   ```

3. 刪除特定的 Pod：
   ```bash
   kubectl delete pod my-pod
   ```

4. 顯示 Pod 的詳細資訊：
   ```bash
   kubectl describe pod my-pod
   ```

5. 查看 Pod 的日誌：
   ```bash
   kubectl logs my-pod
   ```

## Tips
- 使用 `kubectl get all` 可以一次性獲取叢集中的所有資源。
- 在進行大規模變更前，建議先使用 `kubectl apply --dry-run=client -f <file>` 來檢查配置的正確性。
- 利用 `kubectl config` 命令來管理多個 Kubernetes 叢集的上下文，方便切換。