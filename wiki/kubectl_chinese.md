# [Linux] Bash kubectl 使用方法: 管理 Kubernetes 集群

## 概述
`kubectl` 是 Kubernetes 的命令行工具，用于与 Kubernetes 集群进行交互。它允许用户部署应用、管理集群资源、查看日志和调试等。

## 用法
基本语法如下：
```bash
kubectl [options] [arguments]
```

## 常用选项
- `get`：获取资源信息。
- `apply`：应用配置文件中的更改。
- `delete`：删除指定的资源。
- `describe`：显示资源的详细信息。
- `logs`：查看 Pod 的日志。

## 常见示例
1. 获取所有 Pod 的列表：
   ```bash
   kubectl get pods
   ```

2. 应用配置文件：
   ```bash
   kubectl apply -f deployment.yaml
   ```

3. 删除指定的 Pod：
   ```bash
   kubectl delete pod my-pod
   ```

4. 查看特定 Pod 的详细信息：
   ```bash
   kubectl describe pod my-pod
   ```

5. 查看某个 Pod 的日志：
   ```bash
   kubectl logs my-pod
   ```

## 小贴士
- 使用 `kubectl get all` 可以快速查看所有资源的状态。
- 在执行 `kubectl apply` 前，使用 `kubectl diff -f <file>` 可以查看将要应用的更改。
- 定期使用 `kubectl cluster-info` 检查集群状态，确保一切正常。