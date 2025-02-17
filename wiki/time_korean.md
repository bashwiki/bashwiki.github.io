# [리눅스] Bash time 사용법: 명령어 실행 시간 측정

## Overview
`time` 명령어는 특정 명령어를 실행하는 데 소요된 시간을 측정하는 데 사용됩니다. 이 명령어는 프로세스의 실행 시간, 사용자 CPU 시간, 시스템 CPU 시간 등의 정보를 제공합니다.

## Usage
기본 구문은 다음과 같습니다:
```
time [options] [arguments]
```

## Common Options
- `-p`: POSIX 형식으로 출력합니다.
- `-o FILE`: 결과를 지정한 파일에 저장합니다.
- `-a`: 결과를 파일에 추가합니다 (기존 내용에 덮어쓰지 않음).

## Common Examples
1. 기본 사용법:
   ```bash
   time ls -l
   ```

2. 결과를 파일에 저장:
   ```bash
   time -o output.txt ls -l
   ```

3. 결과를 파일에 추가:
   ```bash
   time -a -o output.txt sleep 2
   ```

4. POSIX 형식으로 출력:
   ```bash
   time -p sleep 3
   ```

## Tips
- `time` 명령어를 사용할 때, 실행 시간 외에도 CPU 사용량을 확인하여 성능 분석에 활용할 수 있습니다.
- 스크립트에서 `time`을 사용하여 특정 작업의 성능을 모니터링하면, 최적화할 부분을 쉽게 찾을 수 있습니다.
- `time` 명령어는 다른 명령어와 함께 사용할 수 있으므로, 복잡한 작업의 성능을 측정하는 데 유용합니다.