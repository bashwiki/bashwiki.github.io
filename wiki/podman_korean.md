# [리눅스] Bash podman 사용법: 컨테이너 관리 도구

## Overview
Podman은 컨테이너를 생성, 관리 및 실행할 수 있는 도구입니다. Docker와 유사하지만, 데몬이 필요 없고 루트 권한 없이도 사용할 수 있는 장점이 있습니다. Podman은 컨테이너를 쉽게 다룰 수 있도록 다양한 기능을 제공합니다.

## Usage
Podman의 기본 구문은 다음과 같습니다:

```bash
podman [options] [arguments]
```

## Common Options
- `run`: 새로운 컨테이너를 생성하고 실행합니다.
- `ps`: 현재 실행 중인 컨테이너 목록을 표시합니다.
- `images`: 로컬에 저장된 컨테이너 이미지를 나열합니다.
- `pull`: 원격 레지스트리에서 컨테이너 이미지를 다운로드합니다.
- `rm`: 중지된 컨테이너를 삭제합니다.

## Common Examples
- **컨테이너 실행하기**:
  ```bash
  podman run -d --name my-container nginx
  ```
  이 명령은 Nginx 웹 서버를 실행하는 새로운 컨테이너를 생성합니다.

- **실행 중인 컨테이너 목록 보기**:
  ```bash
  podman ps
  ```
  현재 실행 중인 모든 컨테이너의 목록을 보여줍니다.

- **이미지 목록 보기**:
  ```bash
  podman images
  ```
  로컬에 저장된 모든 컨테이너 이미지를 나열합니다.

- **이미지 다운로드**:
  ```bash
  podman pull ubuntu
  ```
  Ubuntu 이미지를 원격 레지스트리에서 다운로드합니다.

- **컨테이너 삭제**:
  ```bash
  podman rm my-container
  ```
  이름이 `my-container`인 중지된 컨테이너를 삭제합니다.

## Tips
- Podman은 기본적으로 루트 권한 없이 실행할 수 있으므로 보안에 유리합니다.
- 컨테이너를 실행할 때 `-d` 옵션을 사용하면 백그라운드에서 실행됩니다.
- `podman` 명령어에 `--help`를 추가하면 각 명령어에 대한 자세한 도움말을 볼 수 있습니다.