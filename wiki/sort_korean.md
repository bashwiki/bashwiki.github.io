# [리눅스] Bash sort 사용법: 파일 내용을 정렬합니다.

## Overview
`sort` 명령어는 파일이나 표준 입력으로부터 데이터를 읽어들여, 그 내용을 정렬된 형태로 출력하는 데 사용됩니다. 이 명령어는 텍스트 파일의 내용을 정렬할 때 매우 유용합니다.

## Usage
기본 구문은 다음과 같습니다.
```bash
sort [options] [arguments]
```

## Common Options
- `-r`: 역순으로 정렬합니다.
- `-n`: 숫자 기준으로 정렬합니다.
- `-k`: 특정 키를 기준으로 정렬합니다.
- `-u`: 중복된 줄을 제거합니다.
- `-o`: 결과를 지정한 파일에 저장합니다.

## Common Examples
1. 기본 정렬:
   ```bash
   sort filename.txt
   ```

2. 역순 정렬:
   ```bash
   sort -r filename.txt
   ```

3. 숫자 기준 정렬:
   ```bash
   sort -n numbers.txt
   ```

4. 특정 키로 정렬 (예: 두 번째 열 기준):
   ```bash
   sort -k2 filename.txt
   ```

5. 중복 제거 후 정렬:
   ```bash
   sort -u filename.txt
   ```

6. 결과를 파일에 저장:
   ```bash
   sort filename.txt -o sorted.txt
   ```

## Tips
- 정렬할 파일이 클 경우, 메모리 사용량을 고려하여 적절한 옵션을 선택하세요.
- `-k` 옵션을 사용하여 복잡한 데이터 구조를 정렬할 수 있습니다.
- 파이프(`|`)와 함께 사용하여 다른 명령어와 결합할 수 있습니다. 예를 들어, `cat filename.txt | sort`와 같이 사용할 수 있습니다.