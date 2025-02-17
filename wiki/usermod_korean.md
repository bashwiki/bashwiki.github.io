# [리눅스] Bash usermod 사용법: 사용자 계정 수정

## Overview
`usermod` 명령은 리눅스 시스템에서 사용자 계정의 속성을 수정하는 데 사용됩니다. 이 명령을 통해 사용자의 그룹, 홈 디렉토리, 로그인 셸 등을 변경할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
usermod [옵션] [사용자 이름]
```

## Common Options
- `-aG`: 사용자를 추가 그룹에 추가합니다.
- `-d`: 사용자의 홈 디렉토리를 변경합니다.
- `-l`: 사용자의 로그인 이름을 변경합니다.
- `-s`: 사용자의 로그인 셸을 변경합니다.
- `-u`: 사용자의 UID를 변경합니다.

## Common Examples
- 사용자를 그룹에 추가하기:
```bash
usermod -aG sudo username
```

- 사용자의 홈 디렉토리 변경하기:
```bash
usermod -d /new/home/directory username
```

- 사용자의 로그인 이름 변경하기:
```bash
usermod -l newusername oldusername
```

- 사용자의 로그인 셸 변경하기:
```bash
usermod -s /bin/zsh username
```

- 사용자의 UID 변경하기:
```bash
usermod -u 1001 username
```

## Tips
- `usermod` 명령을 사용하기 전에 항상 백업을 해두는 것이 좋습니다.
- 변경 사항이 즉시 반영되지 않을 수 있으니, 시스템에 재로그인하거나 재부팅이 필요할 수 있습니다.
- 사용자 계정을 수정할 때는 적절한 권한이 필요하므로, 일반적으로 `sudo`를 사용해야 합니다.