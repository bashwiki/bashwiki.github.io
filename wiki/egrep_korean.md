# [리눅스] Bash egrep 사용법: 정규 표현식으로 텍스트 검색

## Overview
`egrep` 명령어는 정규 표현식을 사용하여 파일이나 입력 스트림에서 텍스트를 검색하는 데 사용됩니다. `grep`의 확장 버전으로, 더 복잡한 패턴을 지원합니다.

## Usage
기본 구문은 다음과 같습니다:

```
egrep [options] [arguments]
```

## Common Options
- `-i`: 대소문자를 구분하지 않고 검색합니다.
- `-v`: 패턴에 일치하지 않는 행을 출력합니다.
- `-c`: 패턴에 일치하는 행의 수를 출력합니다.
- `-n`: 일치하는 행의 번호를 함께 출력합니다.
- `-r`: 하위 디렉토리까지 재귀적으로 검색합니다.

## Common Examples
1. 특정 단어가 포함된 행 찾기:
   ```bash
   egrep "hello" filename.txt
   ```

2. 대소문자 구분 없이 검색하기:
   ```bash
   egrep -i "hello" filename.txt
   ```

3. 특정 패턴이 포함되지 않은 행 찾기:
   ```bash
   egrep -v "hello" filename.txt
   ```

4. 일치하는 행의 수 세기:
   ```bash
   egrep -c "hello" filename.txt
   ```

5. 하위 디렉토리까지 검색하기:
   ```bash
   egrep -r "hello" /path/to/directory
   ```

## Tips
- 정규 표현식을 잘 활용하면 복잡한 검색도 쉽게 할 수 있습니다.
- 검색 결과를 다른 명령어와 파이프하여 추가적인 처리를 할 수 있습니다.
- 대량의 데이터에서 검색할 때는 성능을 고려하여 필요한 옵션만 사용하는 것이 좋습니다.