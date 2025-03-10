# [리눅스] Bash disown 사용법: 백그라운드 작업을 분리하기

## Overview
`disown` 명령어는 현재 쉘 세션에서 실행 중인 작업을 분리하여, 해당 작업이 쉘 종료 시에도 계속 실행될 수 있도록 합니다. 이를 통해 사용자는 백그라운드에서 작업을 계속 진행하면서 쉘을 안전하게 종료할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
disown [options] [jobspec]
```

## Common Options
- `-h`: 지정된 작업을 중단하지 않고, 해당 작업이 종료될 때까지 기다리지 않도록 합니다.
- `-a`: 모든 작업을 대상으로 합니다.
- `-r`: 실행 중인 작업만 대상으로 합니다.

## Common Examples
1. **특정 작업 분리하기**
   ```bash
   disown %1
   ```
   위 명령어는 첫 번째 작업을 분리합니다.

2. **모든 작업 분리하기**
   ```bash
   disown -a
   ```
   현재 쉘에서 실행 중인 모든 작업을 분리합니다.

3. **실행 중인 작업만 분리하기**
   ```bash
   disown -r
   ```
   실행 중인 모든 작업을 분리합니다.

## Tips
- `disown` 명령어를 사용하기 전에 작업을 백그라운드로 실행하려면 `&`를 사용하세요.
- `jobs` 명령어를 사용하여 현재 실행 중인 작업 목록을 확인한 후, 원하는 작업을 선택하여 분리할 수 있습니다.
- `disown` 명령어를 사용하면 작업이 종료될 때까지 기다리지 않고 쉘을 종료할 수 있어 유용합니다.