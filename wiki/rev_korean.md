# [리눅스] Bash rev 사용법: 문자열을 뒤집기

## Overview
`rev` 명령어는 입력된 각 줄의 문자를 뒤집어 출력하는 간단한 도구입니다. 주로 텍스트 파일의 내용을 변형하거나 특정 문자열을 뒤집어야 할 때 유용하게 사용됩니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
rev [options] [arguments]
```

## Common Options
- `-o, --output=FILE` : 결과를 지정한 파일에 저장합니다.
- `-h, --help` : 사용법에 대한 도움말을 출력합니다.
- `-V, --version` : 버전 정보를 출력합니다.

## Common Examples
1. **기본 사용법**: 문자열을 뒤집어 출력합니다.
   ```bash
   echo "hello" | rev
   ```
   출력:
   ```
   olleh
   ```

2. **파일의 내용을 뒤집기**: 파일의 각 줄을 뒤집어 출력합니다.
   ```bash
   rev myfile.txt
   ```

3. **출력을 파일에 저장하기**: 뒤집은 내용을 새로운 파일에 저장합니다.
   ```bash
   rev myfile.txt -o reversed.txt
   ```

4. **여러 줄의 문자열 뒤집기**: 여러 줄을 입력하여 각각의 줄을 뒤집습니다.
   ```bash
   echo -e "hello\nworld" | rev
   ```
   출력:
   ```
   olleh
   dlrow
   ```

## Tips
- `rev` 명령어는 파이프와 함께 사용하여 다른 명령어의 출력을 쉽게 변형할 수 있습니다.
- 대량의 데이터를 처리할 때는 결과를 파일로 저장하는 것이 좋습니다.
- `rev`는 각 줄을 독립적으로 처리하므로, 여러 줄의 데이터를 한 번에 뒤집을 수 있습니다.