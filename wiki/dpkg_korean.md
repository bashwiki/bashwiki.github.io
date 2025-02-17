# [리눅스] Bash dpkg 사용법: 패키지 관리 명령어

## Overview
`dpkg`는 Debian 기반의 리눅스 배포판에서 소프트웨어 패키지를 설치, 제거 및 관리하는 데 사용되는 기본 명령어입니다. 이 명령어는 패키지 파일(.deb)을 직접 다루며, 시스템에 설치된 패키지의 상태를 확인할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
dpkg [options] [arguments]
```

## Common Options
- `-i`, `--install`: 지정한 패키지를 설치합니다.
- `-r`, `--remove`: 지정한 패키지를 제거합니다.
- `-l`, `--list`: 설치된 패키지 목록을 표시합니다.
- `-s`, `--status`: 지정한 패키지의 상태 정보를 보여줍니다.
- `-P`, `--purge`: 패키지를 완전히 제거하고 관련 설정 파일도 삭제합니다.

## Common Examples
- 패키지 설치하기:
  ```bash
  dpkg -i package.deb
  ```

- 패키지 제거하기:
  ```bash
  dpkg -r package_name
  ```

- 설치된 패키지 목록 보기:
  ```bash
  dpkg -l
  ```

- 특정 패키지 상태 확인하기:
  ```bash
  dpkg -s package_name
  ```

- 패키지 완전 제거하기:
  ```bash
  dpkg -P package_name
  ```

## Tips
- `dpkg` 명령어는 패키지 의존성을 자동으로 처리하지 않으므로, 패키지를 설치할 때 의존성 문제를 주의해야 합니다.
- `dpkg`를 사용할 때는 `apt`와 같은 고급 패키지 관리 도구와 함께 사용하는 것이 좋습니다. `apt`는 의존성 해결을 자동으로 처리해줍니다.
- 패키지 설치 후에는 `dpkg --configure -a` 명령어를 사용하여 미완료된 설치를 완료할 수 있습니다.