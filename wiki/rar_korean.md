# [리눅스] Bash rar 사용법: 압축 및 압축 해제

## Overview
`rar` 명령어는 파일 및 디렉토리를 압축하고 압축 해제하는 데 사용되는 유틸리티입니다. RAR 포맷은 높은 압축률과 빠른 속도로 잘 알려져 있으며, 여러 파일을 하나의 아카이브로 묶을 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
rar [options] [arguments]
```

## Common Options
- `a`: 파일을 아카이브에 추가합니다.
- `x`: 아카이브에서 파일을 추출합니다.
- `t`: 아카이브의 무결성을 테스트합니다.
- `v`: 압축 진행 상황을 자세히 표시합니다.
- `m`: 압축 수준을 설정합니다 (0-5, 기본값은 3).

## Common Examples
1. **파일 압축하기**
   ```bash
   rar a archive.rar file1.txt file2.txt
   ```
   위 명령어는 `file1.txt`와 `file2.txt`를 `archive.rar`라는 이름의 아카이브로 압축합니다.

2. **디렉토리 압축하기**
   ```bash
   rar a archive.rar /path/to/directory/
   ```
   지정한 디렉토리를 `archive.rar`로 압축합니다.

3. **파일 추출하기**
   ```bash
   rar x archive.rar
   ```
   현재 디렉토리에서 `archive.rar` 파일을 추출합니다.

4. **압축 무결성 테스트**
   ```bash
   rar t archive.rar
   ```
   `archive.rar`의 무결성을 검사합니다.

5. **압축 수준 설정하기**
   ```bash
   rar a -m5 archive.rar file1.txt
   ```
   `file1.txt`를 최대 압축 수준으로 `archive.rar`에 추가합니다.

## Tips
- 압축할 파일의 수가 많을 경우, 디렉토리 전체를 압축하는 것이 효율적입니다.
- 압축 해제 시 `x` 옵션을 사용하면 원래의 디렉토리 구조를 유지할 수 있습니다.
- RAR 파일의 무결성을 정기적으로 검사하여 데이터 손실을 방지하세요.