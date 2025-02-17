# [리눅스] Bash iptables 사용법: 네트워크 트래픽 필터링

## Overview
iptables는 리눅스에서 네트워크 트래픽을 필터링하고 관리하는 데 사용되는 강력한 도구입니다. 방화벽 규칙을 설정하여 들어오고 나가는 패킷을 제어할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
iptables [options] [arguments]
```

## Common Options
- `-A` : 규칙을 체인에 추가합니다.
- `-D` : 규칙을 체인에서 삭제합니다.
- `-I` : 규칙을 체인의 맨 앞에 삽입합니다.
- `-L` : 현재 규칙 목록을 표시합니다.
- `-F` : 모든 규칙을 삭제합니다.
- `-P` : 체인의 기본 정책을 설정합니다.

## Common Examples
- 모든 트래픽을 차단하는 기본 정책 설정:
```bash
iptables -P INPUT DROP
```

- 특정 IP 주소에서 오는 트래픽 허용:
```bash
iptables -A INPUT -s 192.168.1.10 -j ACCEPT
```

- 포트 80(HTTP)으로 오는 트래픽 허용:
```bash
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

- 현재 규칙 목록 보기:
```bash
iptables -L
```

- 모든 규칙 삭제:
```bash
iptables -F
```

## Tips
- 규칙을 설정하기 전에 현재 규칙을 백업하는 것이 좋습니다.
- 변경 사항을 적용한 후에는 항상 규칙 목록을 확인하여 올바르게 설정되었는지 확인하세요.
- iptables는 시스템 부팅 시 규칙을 유지하지 않으므로, 필요한 경우 규칙을 저장하고 복원하는 방법을 설정해야 합니다.