# [리눅스] Bash awk 사용법: 텍스트 처리 및 데이터 추출

## Overview
`awk`는 텍스트 파일을 처리하고 데이터를 추출하는 데 사용되는 강력한 프로그래밍 언어이자 도구입니다. 주로 필드 기반의 데이터 처리에 적합하며, 패턴 매칭과 텍스트 조작을 통해 다양한 작업을 수행할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
awk [options] [arguments]
```

## Common Options
- `-F`: 필드 구분자를 지정합니다. 기본값은 공백입니다.
- `-v`: 변수를 정의합니다.
- `-f`: awk 스크립트를 파일에서 읽어옵니다.
- `-W`: 경고 메시지를 제어합니다.

## Common Examples
1. **파일의 모든 행 출력하기**
   ```bash
   awk '{print}' filename.txt
   ```

2. **특정 필드 출력하기 (예: 두 번째 필드)**
   ```bash
   awk '{print $2}' filename.txt
   ```

3. **필드 구분자 지정하기 (예: 콤마)**
   ```bash
   awk -F, '{print $1}' filename.csv
   ```

4. **조건에 따라 행 필터링하기 (예: 첫 번째 필드가 'A'인 행)**
   ```bash
   awk '$1 == "A" {print}' filename.txt
   ```

5. **변수 사용하기 (예: 총합 계산)**
   ```bash
   awk '{sum += $1} END {print sum}' filename.txt
   ```

## Tips
- `awk`는 대소문자를 구분하므로, 필요에 따라 `tolower()` 또는 `toupper()` 함수를 사용하여 변환할 수 있습니다.
- 복잡한 스크립트는 파일에 저장하고 `-f` 옵션으로 실행하면 관리가 용이합니다.
- `awk`의 패턴 매칭 기능을 활용하여 특정 조건에 맞는 데이터만 추출하는 것이 효율적입니다.