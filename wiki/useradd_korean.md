# [리눅스] Bash useradd 사용법: 사용자 계정 생성

## Overview
`useradd` 명령어는 리눅스 시스템에서 새로운 사용자 계정을 생성하는 데 사용됩니다. 이 명령어를 통해 시스템에 새로운 사용자를 추가하고, 해당 사용자의 기본 설정을 구성할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
useradd [옵션] [사용자 이름]
```

## Common Options
- `-m`: 사용자의 홈 디렉토리를 생성합니다.
- `-s`: 사용자의 로그인 셸을 지정합니다.
- `-G`: 사용자를 추가할 그룹을 지정합니다.
- `-c`: 사용자의 설명을 추가합니다.
- `-d`: 사용자의 홈 디렉토리 경로를 지정합니다.

## Common Examples
- 기본 사용자 추가:
  ```bash
  useradd newuser
  ```

- 홈 디렉토리 생성과 함께 사용자 추가:
  ```bash
  useradd -m newuser
  ```

- 특정 로그인 셸을 가진 사용자 추가:
  ```bash
  useradd -s /bin/bash newuser
  ```

- 특정 그룹에 사용자를 추가하며 홈 디렉토리 생성:
  ```bash
  useradd -m -G sudo newuser
  ```

- 사용자 설명 추가:
  ```bash
  useradd -c "New User Account" newuser
  ```

## Tips
- 사용자 계정을 추가한 후, `passwd` 명령어를 사용하여 비밀번호를 설정하는 것을 잊지 마세요.
- 사용자 계정 생성 시 필요한 옵션을 미리 계획하여 명령어를 효율적으로 사용하세요.
- 그룹 관리가 필요한 경우, `usermod` 명령어를 사용하여 기존 사용자 계정을 수정할 수 있습니다.