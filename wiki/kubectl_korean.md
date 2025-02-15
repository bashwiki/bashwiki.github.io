# [리눅스] Bash kubectl 사용법

## Overview
`kubectl`은 Kubernetes 클러스터와 상호작용하기 위한 명령줄 도구입니다. 이 도구를 사용하면 클러스터의 리소스를 관리하고, 애플리케이션을 배포하며, 클러스터 상태를 모니터링할 수 있습니다. `kubectl`은 Kubernetes API 서버와 통신하여 다양한 작업을 수행하는 데 필요한 명령을 제공합니다.

## Usage
기본적인 `kubectl` 명령어 구문은 다음과 같습니다:

```
kubectl [command] [TYPE] [NAME] [flags]
```

- **command**: 수행할 작업 (예: `get`, `create`, `delete`, `apply` 등)
- **TYPE**: 리소스 유형 (예: `pods`, `services`, `deployments` 등)
- **NAME**: 리소스의 이름 (선택 사항)
- **flags**: 추가적인 옵션 (예: `--namespace`, `--output`, `--dry-run` 등)

### 일반적인 옵션
- `--namespace`: 특정 네임스페이스에서 작업을 수행합니다.
- `--output`: 출력 형식을 지정합니다 (예: `json`, `yaml`, `wide`).
- `--dry-run`: 실제로 변경을 적용하지 않고 명령을 시뮬레이션합니다.

## Examples
### 예제 1: 모든 파드 목록 가져오기
다음 명령어는 현재 네임스페이스에 있는 모든 파드의 목록을 가져옵니다.

```bash
kubectl get pods
```

### 예제 2: 새로운 디플로이먼트 생성
다음 명령어는 nginx 디플로이먼트를 생성합니다.

```bash
kubectl create deployment nginx --image=nginx
```

## Tips
- `kubectl` 명령어를 자주 사용할 경우, `kubectl config`를 통해 클러스터 설정을 관리하는 것이 좋습니다.
- `kubectl`의 `-h` 또는 `--help` 플래그를 사용하여 각 명령어에 대한 도움말을 확인할 수 있습니다.
- YAML 파일을 사용하여 리소스를 정의하고 `kubectl apply -f <파일명>` 명령어로 배포하는 것이 효율적입니다. 이를 통해 버전 관리와 재사용이 용이해집니다.