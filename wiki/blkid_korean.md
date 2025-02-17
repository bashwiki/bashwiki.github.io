# [리눅스] Bash blkid 사용법: 블록 장치의 UUID 및 파일 시스템 정보 조회

## Overview
`blkid` 명령어는 리눅스 시스템에서 블록 장치의 UUID, 파일 시스템 타입 및 기타 메타데이터를 조회하는 데 사용됩니다. 이 명령어는 주로 디스크 파티션의 정보를 확인할 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
blkid [options] [arguments]
```

## Common Options
- `-o`: 출력 형식을 지정합니다. 예를 들어, `-o value`는 값만 출력합니다.
- `-s`: 특정 속성만 조회합니다. 예를 들어, `-s UUID`는 UUID만 출력합니다.
- `-p`: 장치의 UUID를 확인할 때, 장치의 파일 시스템을 자동으로 감지합니다.

## Common Examples
다음은 `blkid` 명령어의 몇 가지 일반적인 사용 예입니다.

1. 모든 블록 장치 정보 조회:
   ```bash
   blkid
   ```

2. 특정 장치의 UUID 조회:
   ```bash
   blkid /dev/sda1
   ```

3. UUID만 출력하기:
   ```bash
   blkid -s UUID -o value /dev/sda1
   ```

4. 특정 파일 시스템 타입 조회:
   ```bash
   blkid -s TYPE /dev/sda1
   ```

## Tips
- `blkid` 명령어는 루트 권한이 필요할 수 있으므로, 필요한 경우 `sudo`를 사용하세요.
- 장치의 정보를 자주 확인해야 하는 경우, 스크립트를 작성하여 자동화할 수 있습니다.
- `blkid`의 출력 결과를 다른 명령어와 파이프하여 추가적인 처리를 할 수 있습니다.