# [리눅스] Bash chmod 사용법: 파일 및 디렉토리 권한 변경

## Overview
`chmod` 명령어는 파일 및 디렉토리의 접근 권한을 변경하는 데 사용됩니다. 이 명령어를 통해 사용자, 그룹, 기타 사용자에 대한 읽기, 쓰기 및 실행 권한을 설정할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
chmod [options] [arguments]
```

## Common Options
- `-R`: 하위 디렉토리와 파일에 대해 재귀적으로 권한을 변경합니다.
- `-v`: 변경된 권한을 자세히 출력합니다.
- `-c`: 변경된 권한에 대한 간단한 보고서를 출력합니다.

## Common Examples
1. 파일에 읽기 및 쓰기 권한 부여:
   ```bash
   chmod u+rw filename.txt
   ```

2. 모든 사용자에게 실행 권한 부여:
   ```bash
   chmod a+x script.sh
   ```

3. 디렉토리와 그 하위 파일에 대해 재귀적으로 권한 변경:
   ```bash
   chmod -R 755 /path/to/directory
   ```

4. 특정 사용자에게만 쓰기 권한 제거:
   ```bash
   chmod u-w filename.txt
   ```

## Tips
- 권한을 설정할 때는 항상 현재 권한을 확인하고 변경 사항을 적용하세요.
- `chmod` 명령어를 사용할 때는 숫자 모드(예: 755)와 기호 모드(예: u+x)를 혼합하여 사용할 수 있습니다.
- 중요한 시스템 파일에 대해 권한을 변경할 때는 주의가 필요합니다.