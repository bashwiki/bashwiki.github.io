# [리눅스] Bash rmdir 사용법: 빈 디렉토리 삭제

## Overview
`rmdir` 명령어는 빈 디렉토리를 삭제하는 데 사용됩니다. 이 명령어는 지정된 디렉토리가 비어 있을 때만 작동하며, 디렉토리에 파일이나 다른 디렉토리가 존재할 경우 삭제되지 않습니다.

## Usage
기본 구문은 다음과 같습니다:

```
rmdir [옵션] [인수]
```

## Common Options
- `-p`: 상위 디렉토리도 함께 삭제합니다. 상위 디렉토리가 비어 있어야만 삭제됩니다.
- `--ignore-fail-on-non-empty`: 비어 있지 않은 디렉토리를 삭제하려고 시도할 때 오류 메시지를 무시합니다.

## Common Examples
1. 빈 디렉토리 삭제하기:
   ```bash
   rmdir my_empty_directory
   ```

2. 여러 빈 디렉토리 한 번에 삭제하기:
   ```bash
   rmdir dir1 dir2 dir3
   ```

3. 상위 디렉토리와 함께 삭제하기:
   ```bash
   rmdir -p parent_directory/child_directory
   ```

4. 비어 있지 않은 디렉토리에서 오류 무시하기:
   ```bash
   rmdir --ignore-fail-on-non-empty non_empty_directory
   ```

## Tips
- `rmdir`를 사용하기 전에 삭제할 디렉토리가 정말 비어 있는지 확인하세요.
- 디렉토리를 삭제하기 전에 중요한 파일이 없는지 다시 한 번 점검하는 것이 좋습니다.
- `rmdir` 명령어는 복구할 수 없으므로 신중하게 사용해야 합니다.