# [리눅스] Bash trap 사용법: 신호를 처리하는 방법

## Overview
`trap` 명령어는 Bash 스크립트에서 특정 신호를 처리하는 데 사용됩니다. 이 명령어를 통해 스크립트가 종료되거나 중단될 때 특정 작업을 수행할 수 있습니다. 예를 들어, 스크립트가 종료될 때 파일을 정리하거나 로그를 기록하는 등의 작업을 설정할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
trap [options] [commands] [signals]
```

## Common Options
- `-l`: 사용 가능한 신호 목록을 표시합니다.
- `-p`: 현재 설정된 trap을 출력합니다.
- `SIGINT`: 인터럽트 신호(예: Ctrl+C)에 대한 처리.
- `EXIT`: 스크립트 종료 시 실행할 명령어 설정.

## Common Examples

1. **인터럽트 신호 처리하기**
   ```bash
   trap 'echo "스크립트가 중단되었습니다."' SIGINT
   while true; do
       sleep 1
   done
   ```

2. **스크립트 종료 시 정리 작업 수행하기**
   ```bash
   trap 'rm -f /tmp/tempfile; echo "정리 완료"' EXIT
   touch /tmp/tempfile
   echo "작업 중..."
   ```

3. **다수의 신호 처리하기**
   ```bash
   trap 'echo "SIGTERM 신호 수신"' SIGTERM
   trap 'echo "SIGQUIT 신호 수신"' SIGQUIT
   while true; do
       sleep 1
   done
   ```

## Tips
- 항상 `trap`을 사용하여 스크립트가 예기치 않게 종료될 때 필요한 정리 작업을 수행하도록 설정하세요.
- 신호를 처리할 때는 명령어가 간단하고 빠르게 실행되도록 하여 스크립트의 성능에 영향을 주지 않도록 합니다.
- 여러 신호를 동시에 처리할 수 있으므로, 필요한 경우 적절히 설정하여 유연한 스크립트를 작성하세요.