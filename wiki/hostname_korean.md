# [리눅스] Bash hostname 사용법: 호스트 이름 표시 및 설정

## Overview
`hostname` 명령어는 현재 시스템의 호스트 이름을 표시하거나 변경하는 데 사용됩니다. 이 명령어를 통해 네트워크에서 시스템을 식별할 수 있는 이름을 관리할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
hostname [options] [arguments]
```

## Common Options
- `-f`, `--fqdn`: 완전한 도메인 이름(FQDN)을 표시합니다.
- `-i`, `--ip-address`: 호스트 이름에 대한 IP 주소를 표시합니다.
- `-s`, `--short`: 짧은 호스트 이름만 표시합니다.
- `-V`, `--version`: 버전 정보를 표시합니다.

## Common Examples
1. 현재 호스트 이름 표시하기:
   ```bash
   hostname
   ```

2. 완전한 도메인 이름(FQDN) 표시하기:
   ```bash
   hostname -f
   ```

3. 호스트의 IP 주소 표시하기:
   ```bash
   hostname -i
   ```

4. 짧은 호스트 이름 표시하기:
   ```bash
   hostname -s
   ```

5. 호스트 이름 변경하기 (관리자 권한 필요):
   ```bash
   sudo hostname new-hostname
   ```

## Tips
- 호스트 이름을 변경한 후에는 시스템을 재부팅하거나 네트워크 서비스를 재시작해야 변경 사항이 적용될 수 있습니다.
- 호스트 이름은 네트워크에서 시스템을 식별하는 중요한 요소이므로, 의미 있는 이름으로 설정하는 것이 좋습니다.
- `hostname` 명령어는 스크립트에서 시스템의 이름을 확인하거나 변경할 때 유용하게 사용될 수 있습니다.