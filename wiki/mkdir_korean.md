# [리눅스] Bash mkdir 사용법: 디렉토리 생성

## Overview
`mkdir` 명령어는 새로운 디렉토리를 생성하는 데 사용됩니다. 이 명령어를 통해 사용자는 원하는 위치에 빈 디렉토리를 만들 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
mkdir [옵션] [인수]
```

## Common Options
- `-p`: 부모 디렉토리가 없는 경우에도 함께 생성합니다.
- `-v`: 생성된 디렉토리의 이름을 출력합니다.
- `-m`: 생성할 디렉토리의 권한을 설정합니다.

## Common Examples
- 기본 디렉토리 생성:
```bash
mkdir my_directory
```

- 여러 개의 디렉토리 한 번에 생성:
```bash
mkdir dir1 dir2 dir3
```

- 부모 디렉토리와 함께 생성:
```bash
mkdir -p parent_dir/child_dir
```

- 생성된 디렉토리 이름 출력:
```bash
mkdir -v new_directory
```

- 특정 권한으로 디렉토리 생성:
```bash
mkdir -m 755 my_secure_directory
```

## Tips
- 디렉토리를 생성하기 전에 해당 경로에 이미 동일한 이름의 디렉토리가 있는지 확인하세요.
- `-p` 옵션을 사용하면 중첩된 디렉토리를 쉽게 생성할 수 있어 유용합니다.
- 권한 설정이 필요한 경우 `-m` 옵션을 활용하여 보안성을 높일 수 있습니다.