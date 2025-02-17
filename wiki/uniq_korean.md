# [리눅스] Bash uniq 사용법: 중복된 줄 제거

## Overview
`uniq` 명령어는 입력된 파일이나 표준 입력에서 중복된 줄을 제거하는 데 사용됩니다. 주로 정렬된 데이터에서 중복된 항목을 필터링하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
uniq [options] [arguments]
```

## Common Options
- `-c`: 각 줄의 중복 횟수를 함께 출력합니다.
- `-d`: 중복된 줄만 출력합니다.
- `-u`: 중복되지 않은 줄만 출력합니다.
- `-i`: 대소문자를 구분하지 않고 비교합니다.
- `-w N`: 각 줄의 처음 N 문자만 비교합니다.

## Common Examples
중복된 줄을 제거하는 기본 예제:
```bash
sort input.txt | uniq
```

중복된 줄의 개수를 함께 출력하는 예제:
```bash
sort input.txt | uniq -c
```

중복된 줄만 출력하는 예제:
```bash
sort input.txt | uniq -d
```

중복되지 않은 줄만 출력하는 예제:
```bash
sort input.txt | uniq -u
```

대소문자를 구분하지 않고 중복 제거하는 예제:
```bash
sort input.txt | uniq -i
```

## Tips
- `uniq` 명령어는 입력이 정렬되어 있어야 제대로 작동하므로, `sort` 명령어와 함께 사용하는 것이 일반적입니다.
- 중복된 줄을 제거할 때, 원본 파일을 유지하고 결과를 새로운 파일로 저장하는 것이 좋습니다. 예를 들어:
  ```bash
  sort input.txt | uniq > output.txt
  ```
- 대량의 데이터에서 중복을 처리할 때는 성능을 고려하여 적절한 옵션을 선택하는 것이 중요합니다.