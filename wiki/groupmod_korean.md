# [리눅스] Bash groupmod 사용법

## Overview
`groupmod` 명령어는 리눅스 시스템에서 기존 그룹의 속성을 수정하는 데 사용됩니다. 이 명령어를 통해 그룹 이름을 변경하거나 GID(그룹 ID)를 수정할 수 있습니다. 시스템 관리자나 개발자는 이 명령어를 사용하여 사용자 그룹을 효율적으로 관리할 수 있습니다.

## Usage
`groupmod` 명령어의 기본 구문은 다음과 같습니다:

```bash
groupmod [옵션] 그룹이름
```

### 일반적인 옵션
- `-n, --new-name NEW_GROUP`: 그룹의 이름을 NEW_GROUP으로 변경합니다.
- `-g, --gid GID`: 그룹의 GID를 GID로 변경합니다. 이 GID는 시스템 내에서 고유해야 합니다.

## Examples
### 예제 1: 그룹 이름 변경
기존 그룹의 이름을 `oldgroup`에서 `newgroup`으로 변경하려면 다음과 같이 입력합니다:

```bash
sudo groupmod -n newgroup oldgroup
```

### 예제 2: GID 변경
그룹의 GID를 1001로 변경하려면 다음과 같이 입력합니다:

```bash
sudo groupmod -g 1001 groupname
```

## Tips
- 그룹 이름을 변경할 때는 해당 그룹에 속한 사용자들의 설정 파일이나 권한이 영향을 받을 수 있으므로 주의해야 합니다.
- GID를 변경할 경우, 해당 GID를 사용하는 파일이나 디렉토리의 소유권도 변경될 수 있으므로, 변경 후에는 소유권을 확인하는 것이 좋습니다.
- `groupmod` 명령어를 사용할 때는 항상 `sudo`를 사용하여 관리자 권한으로 실행해야 합니다.