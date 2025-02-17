# [리눅스] Bash uuidgen 사용법: 고유 식별자 생성

## Overview
`uuidgen` 명령은 고유 식별자(UUID)를 생성하는 데 사용됩니다. UUID는 분산 시스템에서 객체를 고유하게 식별하기 위해 널리 사용됩니다. 이 명령은 랜덤하게 생성된 UUID를 출력하여 다양한 애플리케이션에서 사용할 수 있도록 합니다.

## Usage
기본 구문은 다음과 같습니다:
```
uuidgen [options] [arguments]
```

## Common Options
- `-r`, `--random`: 랜덤 UUID를 생성합니다.
- `-v`, `--version`: UUID의 버전을 지정합니다. (1, 3, 4, 5 중 선택)
- `-h`, `--help`: 사용법을 출력합니다.

## Common Examples
- 기본 UUID 생성:
  ```bash
  uuidgen
  ```

- 랜덤 UUID 생성:
  ```bash
  uuidgen -r
  ```

- 특정 버전의 UUID 생성 (예: 버전 4):
  ```bash
  uuidgen -v 4
  ```

## Tips
- UUID는 데이터베이스의 기본 키로 사용하기에 적합합니다.
- UUID를 파일 이름에 포함시켜 고유성을 보장할 수 있습니다.
- UUID를 생성할 때는 필요에 따라 랜덤 또는 특정 버전을 선택하세요.