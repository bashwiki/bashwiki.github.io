# [리눅스] Bash gcc 사용법: C/C++ 프로그램 컴파일

## Overview
`gcc`는 GNU Compiler Collection의 약자로, 주로 C 및 C++ 프로그래밍 언어를 컴파일하는 데 사용됩니다. 이 명령어는 소스 코드를 기계어로 변환하여 실행 가능한 프로그램을 생성합니다.

## Usage
기본 구문은 다음과 같습니다.
```bash
gcc [options] [arguments]
```

## Common Options
- `-o <파일명>`: 생성할 실행 파일의 이름을 지정합니다.
- `-Wall`: 모든 경고 메시지를 활성화합니다.
- `-g`: 디버깅 정보를 포함하여 컴파일합니다.
- `-O2`: 최적화 수준을 설정합니다 (여기서는 2단계 최적화).
- `-I<디렉토리>`: 헤더 파일을 찾을 추가 디렉토리를 지정합니다.

## Common Examples
- 기본 C 프로그램 컴파일:
```bash
gcc hello.c -o hello
```

- 경고 메시지 활성화하여 컴파일:
```bash
gcc -Wall hello.c -o hello
```

- 디버깅 정보 포함하여 컴파일:
```bash
gcc -g hello.c -o hello
```

- 최적화된 실행 파일 생성:
```bash
gcc -O2 hello.c -o hello
```

- 여러 소스 파일을 컴파일하여 하나의 실행 파일 생성:
```bash
gcc file1.c file2.c -o myprogram
```

## Tips
- 컴파일 시 `-Wall` 옵션을 사용하여 가능한 모든 경고를 확인하는 것이 좋습니다.
- 디버깅을 위해 `-g` 옵션을 사용하면, gdb와 같은 디버거를 사용할 때 유용합니다.
- 소스 코드가 변경될 때마다 컴파일을 반복하는 대신, Makefile을 사용하여 빌드를 자동화하는 것을 고려해보세요.