# [리눅스] Bash htop 사용법: 시스템 모니터링 도구

## Overview
htop은 시스템의 프로세스와 리소스 사용량을 실시간으로 모니터링할 수 있는 대화형 프로세스 뷰어입니다. htop은 기본적인 top 명령어보다 더 많은 기능과 사용자 친화적인 인터페이스를 제공합니다.

## Usage
htop의 기본 구문은 다음과 같습니다:

```bash
htop [options] [arguments]
```

## Common Options
- `-h`, `--help`: 도움말을 표시합니다.
- `-v`, `--version`: htop의 버전을 표시합니다.
- `-C`, `--no-color`: 색상을 비활성화합니다.
- `-p`, `--pid`: 특정 프로세스 ID를 모니터링합니다.

## Common Examples
- 기본 htop 실행:
  ```bash
  htop
  ```

- 특정 프로세스 ID 모니터링:
  ```bash
  htop -p 1234
  ```

- 도움말 보기:
  ```bash
  htop --help
  ```

- 버전 확인:
  ```bash
  htop --version
  ```

## Tips
- htop에서 프로세스를 종료하려면, 해당 프로세스를 선택한 후 `F9` 키를 눌러 종료 신호를 보낼 수 있습니다.
- `F2` 키를 눌러 설정 메뉴에 접근하여 다양한 옵션을 조정할 수 있습니다.
- CPU, 메모리 사용량을 시각적으로 확인할 수 있는 그래프를 활용하여 시스템 상태를 쉽게 파악하세요.