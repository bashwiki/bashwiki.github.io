# [리눅스] Bash inotifywait 사용법: 파일 시스템 이벤트 모니터링

## Overview
inotifywait 명령어는 리눅스 파일 시스템에서 발생하는 이벤트를 모니터링하는 데 사용됩니다. 이 명령어는 특정 파일이나 디렉토리에서 변경 사항을 감지하고, 이러한 변경 사항이 발생할 때까지 대기합니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
inotifywait [옵션] [인수]
```

## Common Options
- `-m`: 지속적으로 모니터링합니다. 이벤트가 발생할 때마다 계속 출력합니다.
- `-r`: 하위 디렉토리도 재귀적으로 모니터링합니다.
- `-e`: 감지할 이벤트 유형을 지정합니다. 예: `modify`, `create`, `delete` 등.
- `--format`: 출력 형식을 지정합니다.

## Common Examples
1. 특정 디렉토리에서 파일 생성 이벤트 모니터링:
   ```bash
   inotifywait -m -e create /path/to/directory
   ```

2. 파일 수정 이벤트 모니터링:
   ```bash
   inotifywait -m -e modify /path/to/file.txt
   ```

3. 하위 디렉토리 포함하여 모든 이벤트 모니터링:
   ```bash
   inotifywait -m -r /path/to/directory
   ```

4. 여러 이벤트를 동시에 모니터링:
   ```bash
   inotifywait -m -e modify,delete /path/to/directory
   ```

5. 특정 형식으로 출력하기:
   ```bash
   inotifywait -m --format '%w%f %e' -e modify /path/to/directory
   ```

## Tips
- inotifywait를 사용할 때는 `-m` 옵션을 사용하여 지속적으로 모니터링하면 유용합니다.
- 이벤트가 발생할 때마다 스크립트를 실행하도록 설정하면 자동화된 작업을 수행할 수 있습니다.
- 감시할 파일이나 디렉토리가 많을 경우, 성능에 영향을 줄 수 있으므로 필요한 것만 모니터링하는 것이 좋습니다.