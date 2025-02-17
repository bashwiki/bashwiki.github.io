# [리눅스] Bash groupadd 사용법: 새로운 그룹 추가하기

## Overview
`groupadd` 명령어는 리눅스 시스템에서 새로운 사용자 그룹을 생성하는 데 사용됩니다. 이 명령어를 통해 시스템 관리자는 사용자 계정을 그룹으로 묶어 관리할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
groupadd [options] [group_name]
```

## Common Options
- `-g, --gid GID`: 그룹 ID(GID)를 지정합니다.
- `-r, --system`: 시스템 그룹을 생성합니다. 시스템 그룹은 일반적으로 낮은 GID를 가집니다.
- `-f, --force`: 이미 존재하는 그룹 이름을 사용하려고 할 때 오류를 발생시키지 않습니다.

## Common Examples
1. 기본 그룹 추가:
   ```bash
   groupadd developers
   ```

2. 특정 GID로 그룹 추가:
   ```bash
   groupadd -g 1001 designers
   ```

3. 시스템 그룹 추가:
   ```bash
   groupadd -r sysadmins
   ```

4. 그룹이 이미 존재할 경우 오류 방지:
   ```bash
   groupadd -f developers
   ```

## Tips
- 그룹을 추가한 후, 해당 그룹에 사용자를 추가하려면 `usermod` 명령어를 사용하세요.
- 그룹 이름은 시스템에서 고유해야 하므로, 이미 존재하는 그룹 이름을 사용하지 않도록 주의하세요.
- 시스템 그룹은 일반 사용자 그룹과 구분되므로, 필요에 따라 적절한 옵션을 선택하여 사용하세요.