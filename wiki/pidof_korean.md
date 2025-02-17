# [리눅스] Bash pidof 사용법: 프로세스 ID 찾기

## Overview
`pidof` 명령은 지정된 프로세스 이름에 대한 프로세스 ID(PID)를 찾는 데 사용됩니다. 이 명령은 주로 시스템에서 실행 중인 프로세스를 관리하거나 모니터링할 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
pidof [options] [arguments]
```

## Common Options
- `-s`: 프로세스 ID를 공백으로 구분하여 출력합니다. 
- `-o`: 지정한 프로세스를 제외하고 PID를 출력합니다.
- `-c`: PID가 실행 중인 커널의 컨텍스트를 출력합니다.

## Common Examples
1. 특정 프로세스의 PID 찾기:
   ```bash
   pidof bash
   ```

2. 여러 프로세스의 PID 찾기:
   ```bash
   pidof firefox chrome
   ```

3. PID를 공백으로 구분하여 출력하기:
   ```bash
   pidof -s bash
   ```

4. 특정 프로세스를 제외하고 PID 찾기:
   ```bash
   pidof -o bash firefox
   ```

## Tips
- `pidof` 명령은 대소문자를 구분하므로, 프로세스 이름을 정확하게 입력해야 합니다.
- 여러 프로세스를 한 번에 찾을 수 있어, 시스템 모니터링 시 유용합니다.
- PID를 사용하여 `kill` 명령과 함께 프로세스를 종료할 수 있습니다.