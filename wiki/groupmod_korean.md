# [리눅스] Bash groupmod 사용법: 그룹 수정

## Overview
`groupmod` 명령어는 기존 그룹의 속성을 수정하는 데 사용됩니다. 이 명령어를 통해 그룹 이름이나 GID(그룹 ID)를 변경할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
groupmod [options] [arguments]
```

## Common Options
- `-n, --new-name`: 그룹의 새 이름을 지정합니다.
- `-g, --gid`: 그룹의 새 GID를 지정합니다.
- `-h, --help`: 사용법 정보를 표시합니다.
- `-o, --non-unique`: 중복 GID를 허용합니다.

## Common Examples
1. 그룹 이름 변경:
   ```bash
   groupmod -n newgroup oldgroup
   ```
   이 명령어는 `oldgroup`이라는 그룹의 이름을 `newgroup`으로 변경합니다.

2. GID 변경:
   ```bash
   groupmod -g 1001 groupname
   ```
   이 명령어는 `groupname` 그룹의 GID를 1001로 변경합니다.

3. 중복 GID 허용:
   ```bash
   groupmod -o -g 1001 groupname
   ```
   이 명령어는 `groupname` 그룹의 GID를 1001로 변경하되, 이미 존재하는 GID와 중복될 수 있도록 허용합니다.

## Tips
- 그룹 이름이나 GID를 변경할 때는 해당 그룹에 속한 사용자에게 영향을 미칠 수 있으므로 주의해야 합니다.
- 변경 후에는 관련된 파일의 그룹 소유권을 확인하고 필요에 따라 수정하세요.
- `groupmod` 명령어를 사용하기 전에 현재 그룹 정보를 확인하려면 `getent group` 명령어를 사용할 수 있습니다.