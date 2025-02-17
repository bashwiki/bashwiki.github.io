# [리눅스] Bash realpath 사용법: 파일의 절대 경로를 반환합니다.

## Overview
`realpath` 명령어는 주어진 파일이나 디렉토리의 절대 경로를 반환합니다. 상대 경로를 절대 경로로 변환하여, 파일 시스템 내에서의 정확한 위치를 확인하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
realpath [options] [arguments]
```

## Common Options
- `-m`, `--canonicalize-missing`: 존재하지 않는 경로에 대해서도 절대 경로를 반환합니다.
- `-q`, `--quiet`: 오류 메시지를 출력하지 않습니다.
- `-s`, `--strip`: 경로에서 심볼릭 링크를 제거합니다.

## Common Examples
1. **상대 경로를 절대 경로로 변환하기**
   ```bash
   realpath ./example.txt
   ```

2. **존재하지 않는 파일의 절대 경로 얻기**
   ```bash
   realpath -m ./nonexistent_file.txt
   ```

3. **심볼릭 링크가 있는 경로의 절대 경로 얻기**
   ```bash
   realpath -s /path/to/symlink
   ```

4. **여러 파일의 절대 경로 얻기**
   ```bash
   realpath file1.txt file2.txt
   ```

## Tips
- 상대 경로를 사용할 때, 현재 작업 디렉토리를 기준으로 절대 경로를 확인할 수 있습니다.
- 스크립트에서 파일의 존재 여부를 확인하고 싶다면 `realpath -m` 옵션을 활용하세요.
- 심볼릭 링크를 다룰 때는 `-s` 옵션을 사용하여 실제 파일 경로를 확인하는 것이 좋습니다.