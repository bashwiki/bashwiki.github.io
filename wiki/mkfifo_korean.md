# [리눅스] Bash mkfifo 사용법: FIFO(명명된 파이프) 생성

## Overview
`mkfifo` 명령어는 리눅스 및 유닉스 시스템에서 FIFO(명명된 파이프)를 생성하는 데 사용됩니다. FIFO는 프로세스 간 통신을 가능하게 하며, 데이터를 한 프로세스에서 다른 프로세스로 전송할 수 있도록 합니다.

## Usage
기본 구문은 다음과 같습니다:
```
mkfifo [옵션] [파일명]
```

## Common Options
- `-m, --mode`: 생성할 FIFO의 파일 권한을 설정합니다.
- `-Z, --context`: SELinux 보안 컨텍스트를 설정합니다.

## Common Examples
다음은 `mkfifo` 명령어의 몇 가지 일반적인 사용 예입니다.

1. 기본 FIFO 생성:
   ```bash
   mkfifo myfifo
   ```

2. 특정 권한으로 FIFO 생성:
   ```bash
   mkfifo -m 644 myfifo
   ```

3. SELinux 보안 컨텍스트를 지정하여 FIFO 생성:
   ```bash
   mkfifo -Z myfifo
   ```

## Tips
- FIFO 파일은 프로세스 간의 데이터 전송을 위해 사용되므로, 데이터를 읽고 쓰는 프로세스가 동시에 존재해야 합니다.
- FIFO를 사용할 때는 항상 읽기와 쓰기 프로세스가 적절히 동기화되어야 합니다.
- FIFO 파일은 일반 파일처럼 삭제할 수 있으며, 더 이상 필요하지 않을 경우 `rm` 명령어로 삭제할 수 있습니다.