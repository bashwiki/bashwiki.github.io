# [리눅스] Bash su 사용법: 사용자 전환

## Overview
`su` 명령어는 "substitute user"의 약자로, 현재 사용자가 다른 사용자로 전환할 수 있게 해줍니다. 주로 시스템 관리자가 다른 사용자 계정으로 로그인할 때 사용됩니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
su [options] [username]
```

## Common Options
- `-l` 또는 `--login`: 로그인 셸을 시작하여 사용자의 환경을 초기화합니다.
- `-c`: 주어진 명령을 실행한 후 종료합니다.
- `-s`: 지정된 셸을 사용하여 로그인합니다.

## Common Examples
- 기본 사용자 전환:
```bash
su username
```
- 루트 사용자로 전환:
```bash
su -
```
- 특정 명령을 루트 사용자로 실행:
```bash
su -c 'apt update'
```
- 특정 셸로 전환:
```bash
su -s /bin/bash username
```

## Tips
- `su` 명령어를 사용할 때는 비밀번호를 입력해야 하므로, 비밀번호를 잘 기억해 두세요.
- `su -`를 사용하면 환경 변수가 초기화되어 더 안전하게 사용자 전환을 할 수 있습니다.
- 자주 사용하는 명령어는 스크립트로 만들어 두면 편리합니다.