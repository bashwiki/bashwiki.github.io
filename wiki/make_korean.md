# [리눅스] Bash make 사용법: 프로그램 빌드를 자동화합니다.

## Overview
`make` 명령은 소스 코드 파일을 컴파일하고 프로그램을 빌드하는 데 사용되는 도구입니다. 주로 소프트웨어 개발에서 사용되며, Makefile이라는 설정 파일을 통해 빌드 프로세스를 자동화합니다.

## Usage
기본 구문은 다음과 같습니다:
```
make [options] [arguments]
```

## Common Options
- `-f <file>`: 사용할 Makefile의 이름을 지정합니다.
- `-j <jobs>`: 동시에 실행할 작업의 수를 지정합니다.
- `-k`: 오류가 발생해도 가능한 한 많은 작업을 계속 수행합니다.
- `-B`: 모든 목표를 강제로 재빌드합니다.

## Common Examples
1. 기본 빌드 실행:
   ```bash
   make
   ```

2. 특정 Makefile 사용:
   ```bash
   make -f MyMakefile
   ```

3. 병렬 빌드 실행 (4개의 작업):
   ```bash
   make -j4
   ```

4. 모든 목표 강제 재빌드:
   ```bash
   make -B
   ```

5. 특정 목표 빌드:
   ```bash
   make clean
   ```

## Tips
- Makefile을 작성할 때 주석을 활용하여 각 목표의 목적을 설명하세요.
- 종속성을 명확하게 정의하여 불필요한 재빌드를 방지하세요.
- `make -n` 명령을 사용하여 실제로 실행하지 않고 어떤 작업이 수행될지를 미리 확인할 수 있습니다.