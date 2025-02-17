# [리눅스] Bash dirname 사용법: 경로에서 디렉토리 이름 추출

## Overview
`dirname` 명령어는 주어진 경로에서 디렉토리 이름을 추출하는 데 사용됩니다. 이 명령어는 파일 경로를 분석하여 해당 파일이 위치한 디렉토리의 경로를 반환합니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
dirname [options] [arguments]
```

## Common Options
`dirname` 명령어는 특별한 옵션이 필요하지 않지만, 일반적으로 사용되는 몇 가지 사항은 다음과 같습니다:
- `-z`: 입력 경로가 비어 있는 경우에도 출력을 제공합니다.

## Common Examples
다음은 `dirname` 명령어의 몇 가지 실용적인 예입니다:

1. 기본 사용법:
   ```bash
   dirname /home/user/file.txt
   ```
   출력:
   ```
   /home/user
   ```

2. 상대 경로 사용:
   ```bash
   dirname ./documents/report.pdf
   ```
   출력:
   ```
   ./documents
   ```

3. 디렉토리 경로에서 사용:
   ```bash
   dirname /var/log/syslog
   ```
   출력:
   ```
   /var/log
   ```

4. 비어 있는 경로 처리:
   ```bash
   dirname ""
   ```
   출력:
   ```
   .
   ```

## Tips
- `dirname` 명령어는 스크립트에서 파일 경로를 처리할 때 유용하게 사용될 수 있습니다.
- 여러 파일 경로를 한 번에 처리하려면, `xargs`와 함께 사용할 수 있습니다.
- 경로가 상대적일 경우, 현재 작업 디렉토리에 따라 결과가 달라질 수 있으므로 주의하세요.