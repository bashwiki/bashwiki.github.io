# [리눅스] Bash kubectl 사용법: Kubernetes 클러스터 관리

## Overview
`kubectl`은 Kubernetes 클러스터를 관리하기 위한 명령줄 도구입니다. 이 명령어를 사용하여 클러스터의 상태를 확인하고, 리소스를 생성, 업데이트, 삭제할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
kubectl [options] [arguments]
```

## Common Options
- `get`: 리소스 목록을 조회합니다.
- `describe`: 특정 리소스에 대한 상세 정보를 제공합니다.
- `apply`: 리소스를 생성하거나 업데이트합니다.
- `delete`: 리소스를 삭제합니다.
- `logs`: 특정 파드의 로그를 조회합니다.

## Common Examples
- 모든 파드 목록 조회:
  ```bash
  kubectl get pods
  ```

- 특정 네임스페이스의 서비스 목록 조회:
  ```bash
  kubectl get services -n my-namespace
  ```

- 파드의 상세 정보 조회:
  ```bash
  kubectl describe pod my-pod
  ```

- YAML 파일을 사용하여 리소스 생성 또는 업데이트:
  ```bash
  kubectl apply -f my-resource.yaml
  ```

- 특정 파드의 로그 조회:
  ```bash
  kubectl logs my-pod
  ```

- 특정 리소스 삭제:
  ```bash
  kubectl delete pod my-pod
  ```

## Tips
- `kubectl` 명령어에 `-o wide` 옵션을 추가하면 추가적인 정보를 함께 조회할 수 있습니다.
- 자주 사용하는 명령어는 별도의 스크립트로 저장하여 빠르게 실행할 수 있습니다.
- `kubectl`의 `--help` 옵션을 사용하여 각 명령어의 사용법을 확인할 수 있습니다.