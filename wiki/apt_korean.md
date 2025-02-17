# [리눅스] Bash apt 사용법: 패키지 관리 명령어

## Overview
`apt`는 Debian 및 Ubuntu 기반의 리눅스 배포판에서 소프트웨어 패키지를 설치, 업데이트 및 제거하는 데 사용되는 명령어입니다. 이 명령어는 패키지 관리 시스템의 일환으로, 사용자에게 간편한 패키지 관리 기능을 제공합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
apt [options] [arguments]
```

## Common Options
- `update`: 패키지 목록을 업데이트합니다.
- `upgrade`: 설치된 모든 패키지를 최신 버전으로 업그레이드합니다.
- `install <package>`: 특정 패키지를 설치합니다.
- `remove <package>`: 특정 패키지를 제거합니다.
- `search <package>`: 패키지 이름이나 설명을 검색합니다.
- `show <package>`: 특정 패키지에 대한 정보를 표시합니다.

## Common Examples
- 패키지 목록 업데이트:
  ```bash
  sudo apt update
  ```

- 모든 패키지 업그레이드:
  ```bash
  sudo apt upgrade
  ```

- 특정 패키지 설치 (예: `curl`):
  ```bash
  sudo apt install curl
  ```

- 특정 패키지 제거 (예: `curl`):
  ```bash
  sudo apt remove curl
  ```

- 패키지 검색 (예: `vim`):
  ```bash
  apt search vim
  ```

- 패키지 정보 표시 (예: `curl`):
  ```bash
  apt show curl
  ```

## Tips
- `sudo`를 사용하여 관리자 권한으로 명령어를 실행해야 합니다.
- `apt` 명령어를 사용할 때는 항상 `update`를 먼저 실행하여 최신 패키지 목록을 가져오는 것이 좋습니다.
- `apt` 대신 `apt-get`을 사용할 수 있지만, `apt`는 더 간단하고 사용자 친화적인 인터페이스를 제공합니다.