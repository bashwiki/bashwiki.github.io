# [리눅스] Bash bash 사용법: 셸 스크립트 및 명령어 실행

## Overview
Bash는 유닉스 셸의 일종으로, 명령어를 입력하고 실행할 수 있는 환경을 제공합니다. 사용자는 다양한 명령어를 통해 시스템과 상호작용하고, 스크립트를 작성하여 자동화 작업을 수행할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
bash [options] [arguments]
```

## Common Options
- `-c`: 주어진 문자열을 명령어로 실행합니다.
- `-i`: 대화형 모드로 실행합니다.
- `-l`: 로그인 셸로 실행합니다.
- `-s`: 표준 입력에서 명령어를 읽어 실행합니다.

## Common Examples
1. **스크립트 실행하기**
   ```bash
   bash myscript.sh
   ```

2. **명령어 문자열 실행하기**
   ```bash
   bash -c 'echo "Hello, World!"'
   ```

3. **대화형 셸 시작하기**
   ```bash
   bash -i
   ```

4. **표준 입력에서 명령어 실행하기**
   ```bash
   echo 'echo "Hello from stdin"' | bash -s
   ```

## Tips
- 스크립트를 작성할 때는 첫 줄에 `#!/bin/bash`를 추가하여 Bash 셸에서 실행되도록 지정하세요.
- 스크립트에 실행 권한을 부여하려면 `chmod +x myscript.sh` 명령어를 사용하세요.
- Bash의 내장 명령어와 함수들을 활용하여 스크립트를 더욱 효율적으로 작성할 수 있습니다.