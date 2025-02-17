# [리눅스] Bash dnf 사용법: 패키지 관리 명령어

## Overview
`dnf`는 Fedora 및 RHEL 계열의 리눅스 배포판에서 패키지를 설치, 업데이트 및 제거하는 데 사용되는 패키지 관리 도구입니다. `dnf`는 `yum`의 후속 버전으로, 더 나은 성능과 의존성 해결 기능을 제공합니다.

## Usage
기본 구문은 다음과 같습니다:
```
dnf [options] [arguments]
```

## Common Options
- `install`: 패키지를 설치합니다.
- `remove`: 패키지를 제거합니다.
- `update`: 설치된 패키지를 업데이트합니다.
- `search`: 패키지를 검색합니다.
- `info`: 패키지에 대한 정보를 표시합니다.
- `list`: 설치된 패키지 목록을 표시합니다.

## Common Examples
- 패키지 설치:
  ```bash
  dnf install 패키지명
  ```
- 패키지 제거:
  ```bash
  dnf remove 패키지명
  ```
- 패키지 업데이트:
  ```bash
  dnf update
  ```
- 특정 패키지 정보 확인:
  ```bash
  dnf info 패키지명
  ```
- 설치된 패키지 목록 보기:
  ```bash
  dnf list installed
  ```

## Tips
- `dnf` 명령어를 사용할 때는 항상 최신 패키지를 설치하기 위해 `dnf update`를 먼저 실행하는 것이 좋습니다.
- `dnf`의 `--assumeyes` 옵션을 사용하면 모든 질문에 자동으로 '예'라고 답할 수 있습니다.
- 패키지 설치 후에는 `dnf clean all` 명령어를 사용하여 캐시를 정리하여 디스크 공간을 확보할 수 있습니다.