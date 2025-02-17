# [리눅스] Bash fgrep 사용법: 고정 문자열 검색

## Overview
fgrep 명령어는 파일 내에서 고정된 문자열을 검색하는 데 사용됩니다. 일반적인 grep 명령어와 달리, fgrep은 정규 표현식을 사용하지 않고 문자열을 그대로 검색합니다. 이로 인해 검색 속도가 빠르고, 특정 문자열을 찾는 데 유용합니다.

## Usage
fgrep 명령어의 기본 구문은 다음과 같습니다.

```bash
fgrep [옵션] [인수]
```

## Common Options
- `-i`: 대소문자를 구분하지 않고 검색합니다.
- `-v`: 검색 결과에서 일치하지 않는 행을 출력합니다.
- `-c`: 일치하는 행의 개수를 출력합니다.
- `-n`: 일치하는 행의 번호를 함께 출력합니다.
- `-r`: 하위 디렉토리까지 재귀적으로 검색합니다.

## Common Examples
다음은 fgrep 명령어의 몇 가지 실용적인 예입니다.

1. 특정 문자열 검색:
   ```bash
   fgrep "hello" filename.txt
   ```

2. 대소문자 구분 없이 검색:
   ```bash
   fgrep -i "hello" filename.txt
   ```

3. 일치하지 않는 행 출력:
   ```bash
   fgrep -v "hello" filename.txt
   ```

4. 일치하는 행의 개수 출력:
   ```bash
   fgrep -c "hello" filename.txt
   ```

5. 하위 디렉토리까지 검색:
   ```bash
   fgrep -r "hello" /path/to/directory
   ```

## Tips
- fgrep은 고정 문자열 검색에 최적화되어 있으므로, 정규 표현식이 필요 없는 경우에 사용하세요.
- 대량의 데이터에서 빠른 검색이 필요할 때 fgrep을 활용하면 성능이 개선됩니다.
- 검색할 문자열에 공백이 포함된 경우, 문자열을 따옴표로 감싸는 것을 잊지 마세요.