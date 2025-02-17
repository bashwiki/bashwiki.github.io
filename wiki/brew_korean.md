# [리눅스] Bash brew 사용법: 패키지 관리 도구

## Overview
`brew` 명령어는 macOS 및 Linux에서 소프트웨어 패키지를 관리하는 도구입니다. Homebrew를 통해 사용자는 다양한 소프트웨어를 쉽게 설치, 업데이트 및 제거할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
brew [options] [arguments]
```

## Common Options
- `install`: 지정한 패키지를 설치합니다.
- `uninstall`: 지정한 패키지를 제거합니다.
- `update`: Homebrew와 설치된 패키지 목록을 업데이트합니다.
- `upgrade`: 설치된 패키지를 최신 버전으로 업그레이드합니다.
- `list`: 설치된 모든 패키지의 목록을 표시합니다.

## Common Examples
- 패키지 설치:
  ```bash
  brew install wget
  ```

- 패키지 제거:
  ```bash
  brew uninstall wget
  ```

- 패키지 목록 업데이트:
  ```bash
  brew update
  ```

- 설치된 패키지 업그레이드:
  ```bash
  brew upgrade
  ```

- 설치된 패키지 목록 확인:
  ```bash
  brew list
  ```

## Tips
- Homebrew를 사용하기 전에 `brew update`를 실행하여 최신 정보를 유지하세요.
- 패키지를 설치하기 전에 `brew search [패키지명]`을 사용하여 해당 패키지가 존재하는지 확인할 수 있습니다.
- `brew info [패키지명]`을 사용하면 패키지에 대한 자세한 정보를 확인할 수 있습니다.