# [리눅스] Bash cmake 사용법: 소프트웨어 빌드 시스템 생성

## Overview
`cmake`는 소프트웨어 프로젝트의 빌드 프로세스를 관리하는 도구입니다. 주로 C/C++ 프로젝트에서 사용되며, 다양한 플랫폼에서 일관된 빌드 환경을 제공합니다. `CMakeLists.txt` 파일을 기반으로 소스 코드를 컴파일하고, 라이브러리를 링크하며, 실행 파일을 생성하는 과정을 자동화합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
cmake [options] [arguments]
```

## Common Options
- `-S <path>`: 소스 디렉토리 경로를 지정합니다.
- `-B <path>`: 빌드 디렉토리 경로를 지정합니다.
- `-G <generator>`: 사용할 빌드 시스템 생성기를 지정합니다 (예: "Unix Makefiles", "Ninja").
- `-D <var>=<value>`: CMake 변수에 값을 설정합니다.
- `--build <path>`: 지정한 경로에서 빌드를 수행합니다.

## Common Examples
- **기본 빌드 설정**:
  ```bash
  cmake -S . -B build
  ```
  현재 디렉토리의 소스를 사용하여 `build`라는 디렉토리에 빌드 설정을 생성합니다.

- **특정 생성기 사용**:
  ```bash
  cmake -S . -B build -G "Unix Makefiles"
  ```
  Unix Makefiles 생성기를 사용하여 빌드 설정을 생성합니다.

- **변수 설정**:
  ```bash
  cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
  ```
  빌드 타입을 Release로 설정하여 최적화된 빌드를 생성합니다.

- **빌드 실행**:
  ```bash
  cmake --build build
  ```
  `build` 디렉토리에서 실제 빌드를 수행합니다.

## Tips
- CMakeLists.txt 파일을 잘 구조화하여 프로젝트의 유지보수성을 높이세요.
- 다양한 플랫폼에서의 호환성을 고려하여 CMake 변수를 적절히 설정하세요.
- 빌드 디렉토리는 항상 소스 디렉토리와 분리하여 관리하는 것이 좋습니다.