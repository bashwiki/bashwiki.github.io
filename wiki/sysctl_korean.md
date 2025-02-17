# [리눅스] Bash sysctl 사용법: 커널 매개변수 조정

## Overview
`sysctl` 명령어는 리눅스 커널의 매개변수를 런타임에 조정하고 조회하는 데 사용됩니다. 이를 통해 시스템 성능을 최적화하거나 특정 기능을 활성화 또는 비활성화할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
sysctl [options] [arguments]
```

## Common Options
- `-a`: 모든 커널 매개변수와 그 값을 나열합니다.
- `-w`: 특정 커널 매개변수의 값을 설정합니다.
- `-n`: 매개변수의 값을 출력하되, 이름은 출력하지 않습니다.
- `-e`: 오류 메시지를 무시합니다.

## Common Examples
- 모든 커널 매개변수 나열하기:
```bash
sysctl -a
```

- 특정 매개변수의 값 조회하기 (예: `vm.swappiness`):
```bash
sysctl vm.swappiness
```

- 커널 매개변수 값 설정하기 (예: `vm.swappiness`를 10으로 설정):
```bash
sysctl -w vm.swappiness=10
```

- 매개변수 값만 출력하기 (예: `net.ipv4.ip_forward`):
```bash
sysctl -n net.ipv4.ip_forward
```

## Tips
- `sysctl` 명령어를 사용하여 시스템의 성능을 조정할 때는 변경 사항이 즉시 적용되지만, 재부팅 후에도 유지되도록 하려면 `/etc/sysctl.conf` 파일에 설정을 추가해야 합니다.
- 변경하기 전에 현재 값을 확인하고, 필요시 백업을 해두는 것이 좋습니다.
- 시스템의 특정 요구 사항에 맞게 매개변수를 조정할 때는 신중하게 테스트하여 안정성을 유지하세요.