# [리눅스] Bash export 사용법: 환경 변수 설정

## Overview
`export` 명령어는 셸에서 환경 변수를 설정하고 이를 자식 프로세스에 전달하는 데 사용됩니다. 이를 통해 특정 변수의 값을 다른 프로그램이나 스크립트에서 사용할 수 있도록 할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
export [options] [arguments]
```

## Common Options
- `-p`: 현재 환경 변수 목록을 출력합니다.
- `-n`: 지정한 변수를 export 목록에서 제거합니다.
- `-f`: 함수도 export할 수 있도록 합니다.

## Common Examples
1. **환경 변수 설정하기**
   ```bash
   export MY_VARIABLE="Hello, World!"
   ```

2. **환경 변수 확인하기**
   ```bash
   echo $MY_VARIABLE
   ```

3. **변수 목록 출력하기**
   ```bash
   export -p
   ```

4. **변수 제거하기**
   ```bash
   export -n MY_VARIABLE
   ```

5. **함수 export하기**
   ```bash
   my_function() {
       echo "This is a function"
   }
   export -f my_function
   ```

## Tips
- 환경 변수를 설정한 후에는 해당 변수를 사용하는 프로그램을 실행하기 전에 export 명령어를 사용해야 합니다.
- 스크립트 내에서 변수를 설정할 때는 스크립트의 시작 부분에 export를 사용하는 것이 좋습니다.
- 변수를 영구적으로 설정하려면 `~/.bashrc` 또는 `~/.bash_profile` 파일에 export 명령어를 추가하세요.