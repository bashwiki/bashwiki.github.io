# [리눅스] Bash netstat 사용법: 네트워크 연결 및 상태 확인

## Overview
`netstat` 명령어는 네트워크 연결, 라우팅 테이블, 인터페이스 통계 및 기타 네트워크 관련 정보를 표시하는 데 사용됩니다. 이 명령어는 시스템의 네트워크 상태를 진단하고 모니터링하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
netstat [옵션] [인수]
```

## Common Options
- `-a`: 모든 연결 및 수신 대기 포트를 표시합니다.
- `-t`: TCP 연결만 표시합니다.
- `-u`: UDP 연결만 표시합니다.
- `-n`: 호스트 이름 대신 IP 주소를 숫자로 표시합니다.
- `-p`: 각 연결에 대한 프로세스 ID와 프로그램 이름을 표시합니다.

## Common Examples
- 모든 네트워크 연결과 수신 대기 포트를 표시:
  ```bash
  netstat -a
  ```

- TCP 연결만 표시:
  ```bash
  netstat -t
  ```

- UDP 연결만 표시:
  ```bash
  netstat -u
  ```

- 숫자 형식으로 IP 주소와 포트 표시:
  ```bash
  netstat -n
  ```

- 각 연결에 대한 프로세스 정보 표시:
  ```bash
  netstat -p
  ```

- 모든 정보를 함께 표시:
  ```bash
  netstat -antup
  ```

## Tips
- `netstat` 명령어는 루트 권한으로 실행할 때 더 많은 정보를 제공할 수 있습니다.
- 주기적으로 `netstat`를 사용하여 비정상적인 연결을 모니터링하는 것이 좋습니다.
- `netstat`의 출력 결과를 파일로 저장하여 나중에 분석할 수 있습니다:
  ```bash
  netstat -antup > netstat_output.txt
  ```