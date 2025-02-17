# [리눅스] Bash basename 사용법: 파일 경로에서 파일 이름 추출

## Overview
`basename` 명령어는 주어진 경로에서 파일 이름만을 추출하는 데 사용됩니다. 이 명령어는 파일 경로에서 디렉토리 부분을 제거하고, 순수한 파일 이름을 반환합니다.

## Usage
기본 구문은 다음과 같습니다:
```
basename [옵션] [인수]
```

## Common Options
- `-a`: 여러 파일 이름을 한 번에 처리합니다.
- `-s`: 지정한 접미사를 제거합니다.

## Common Examples
1. 기본 사용법:
   ```bash
   basename /home/user/document.txt
   ```
   출력: `document.txt`

2. 접미사 제거:
   ```bash
   basename /home/user/document.txt .txt
   ```
   출력: `document`

3. 여러 파일 이름 처리:
   ```bash
   basename -a /home/user/file1.txt /home/user/file2.txt
   ```
   출력:
   ```
   file1.txt
   file2.txt
   ```

4. 접미사 제거와 여러 파일 처리:
   ```bash
   basename -a -s .txt /home/user/file1.txt /home/user/file2.txt
   ```
   출력:
   ```
   file1
   file2
   ```

## Tips
- `basename` 명령어는 스크립트에서 파일 이름을 처리할 때 유용합니다.
- 여러 파일을 한 번에 처리할 때는 `-a` 옵션을 사용하여 효율성을 높일 수 있습니다.
- 접미사를 제거할 때는 정확한 접미사를 지정해야 원하는 결과를 얻을 수 있습니다.