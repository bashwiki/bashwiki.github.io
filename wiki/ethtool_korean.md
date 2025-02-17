# [리눅스] Bash ethtool 사용법: 네트워크 인터페이스 정보 조회 및 설정

## Overview
`ethtool` 명령어는 리눅스 시스템에서 네트워크 인터페이스 카드(NIC)의 설정 및 상태를 조회하고 조정하는 데 사용됩니다. 이 명령어를 통해 NIC의 속도, 듀플렉스 모드, 링크 상태 등을 확인할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
ethtool [옵션] [인수]
```

## Common Options
- `-s`: NIC의 설정을 변경합니다.
- `-i`: 드라이버 정보를 표시합니다.
- `-d`: NIC의 디버그 정보를 출력합니다.
- `-p`: NIC의 링크 상태를 확인합니다.
- `-a`: 자동 협상 상태를 확인합니다.

## Common Examples
1. NIC의 기본 정보 조회:
   ```bash
   ethtool eth0
   ```

2. NIC의 드라이버 정보 확인:
   ```bash
   ethtool -i eth0
   ```

3. NIC의 속도 및 듀플렉스 모드 설정:
   ```bash
   ethtool -s eth0 speed 100 duplex full
   ```

4. NIC의 링크 상태 확인:
   ```bash
   ethtool -p eth0
   ```

5. NIC의 자동 협상 상태 확인:
   ```bash
   ethtool -a eth0
   ```

## Tips
- `ethtool`을 사용할 때는 관리자 권한이 필요할 수 있으므로, `sudo`를 사용하여 명령어를 실행하는 것이 좋습니다.
- NIC의 설정을 변경하기 전에 현재 설정을 확인하는 것이 좋습니다.
- `ethtool`의 출력 결과를 잘 이해하면 네트워크 문제를 진단하는 데 큰 도움이 됩니다.