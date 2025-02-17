# [리눅스] Bash unrar 사용법: RAR 파일 압축 해제

## Overview
`unrar` 명령어는 RAR 형식으로 압축된 파일을 해제하는 데 사용됩니다. 이 명령어는 RAR 파일의 내용을 추출하고, 사용자가 파일을 쉽게 접근할 수 있도록 도와줍니다.

## Usage
기본 구문은 다음과 같습니다:

```
unrar [options] [arguments]
```

## Common Options
- `x`: RAR 파일의 내용을 현재 디렉토리로 추출합니다.
- `e`: RAR 파일의 내용을 현재 디렉토리로 추출하되, 디렉토리 구조를 유지하지 않습니다.
- `l`: RAR 파일의 내용을 나열합니다.
- `v`: RAR 파일의 내용을 자세히 나열합니다.
- `t`: RAR 파일의 무결성을 검사합니다.

## Common Examples
다음은 `unrar` 명령어의 몇 가지 일반적인 사용 예입니다.

1. RAR 파일의 내용을 현재 디렉토리로 추출하기:
   ```bash
   unrar x archive.rar
   ```

2. RAR 파일의 내용을 현재 디렉토리로 추출하되, 디렉토리 구조를 유지하지 않기:
   ```bash
   unrar e archive.rar
   ```

3. RAR 파일의 내용을 나열하기:
   ```bash
   unrar l archive.rar
   ```

4. RAR 파일의 무결성 검사하기:
   ```bash
   unrar t archive.rar
   ```

## Tips
- RAR 파일을 추출할 때, 필요한 경우 `-o+` 옵션을 사용하여 기존 파일을 덮어쓸 수 있습니다.
- RAR 파일이 암호로 보호되어 있는 경우, `unrar` 명령어를 실행하면 암호를 입력하라는 메시지가 표시됩니다.
- 자주 사용하는 옵션을 스크립트로 작성하여 반복적인 작업을 자동화할 수 있습니다.