# [리눅스] Bash timeout 사용법: 명령어 실행 시간 제한

## Overview
`timeout` 명령어는 지정된 시간 동안 실행되는 명령어를 제한하는 데 사용됩니다. 만약 명령어가 설정된 시간 내에 완료되지 않으면, `timeout`은 해당 프로세스를 종료합니다. 이 기능은 장시간 실행되는 작업을 제어하고 시스템 자원을 효율적으로 관리하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
timeout [옵션] [시간] [명령어] [인수]
```

## Common Options
- `-s, --signal`: 종료할 때 보낼 신호를 지정합니다. 기본값은 `TERM`입니다.
- `-k, --kill-after`: 지정된 시간 후에도 프로세스가 종료되지 않으면 강제로 종료할 시간을 설정합니다.
- `--preserve-status`: 종료된 명령어의 종료 상태를 유지합니다.

## Common Examples
1. **기본 사용법**: 5초 후에 종료되는 `sleep` 명령어 실행
   ```bash
   timeout 5s sleep 10
   ```

2. **신호 지정**: 3초 후에 `kill` 신호를 보내는 예제
   ```bash
   timeout -s KILL 3s sleep 10
   ```

3. **강제 종료**: 2초 후에 강제로 종료하는 예제
   ```bash
   timeout -k 1s 2s sleep 10
   ```

4. **상태 유지**: 명령어의 종료 상태를 유지하는 예제
   ```bash
   timeout --preserve-status 5s false
   echo $?  # false의 종료 상태 출력
   ```

## Tips
- `timeout`을 사용할 때는 적절한 시간 설정이 중요합니다. 너무 짧게 설정하면 필요한 작업이 완료되지 않을 수 있습니다.
- 스크립트에서 `timeout`을 사용하여 무한 루프나 장시간 실행되는 작업을 방지하는 것이 좋습니다.
- `timeout` 명령어는 다양한 프로세스에 적용할 수 있으므로, 필요에 따라 유연하게 사용할 수 있습니다.