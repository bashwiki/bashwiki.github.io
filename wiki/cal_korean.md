# [리눅스] Bash cal 사용법: 달력을 표시합니다.

## Overview
`cal` 명령어는 지정된 연도와 월의 달력을 터미널에 출력하는 간단한 도구입니다. 기본적으로 현재 월의 달력을 보여주며, 특정 날짜를 지정하여 다른 달력을 볼 수도 있습니다.

## Usage
기본적인 구문은 다음과 같습니다:

```bash
cal [options] [arguments]
```

## Common Options
- `-y`: 현재 연도의 전체 달력을 표시합니다.
- `-m`: 월을 지정하여 해당 월의 달력을 표시합니다.
- `-3`: 현재 월과 이전 및 다음 월의 달력을 함께 표시합니다.
- `-j`: 각 날짜에 대해 연중 몇 번째 날인지 표시합니다.
- `-w`: 주 번호를 표시합니다.

## Common Examples
1. **현재 월의 달력 보기**:
   ```bash
   cal
   ```

2. **특정 연도의 전체 달력 보기**:
   ```bash
   cal 2023
   ```

3. **특정 월의 달력 보기 (예: 12월)**:
   ```bash
   cal 12 2023
   ```

4. **현재 월과 이전 및 다음 월의 달력 보기**:
   ```bash
   cal -3
   ```

5. **현재 연도의 각 날짜에 대한 번호 표시**:
   ```bash
   cal -j
   ```

## Tips
- `cal` 명령어는 간단하지만, 여러 옵션을 조합하여 유용하게 사용할 수 있습니다. 예를 들어, `cal -y -3`을 사용하면 현재 연도의 모든 달력을 한 번에 볼 수 있습니다.
- 달력을 출력할 때, 터미널의 크기에 따라 달력의 형식이 달라질 수 있으므로, 필요한 경우 터미널 크기를 조정해 보세요.
- `cal` 명령어는 스크립트에서 날짜 관련 작업을 자동화할 때 유용하게 사용될 수 있습니다.