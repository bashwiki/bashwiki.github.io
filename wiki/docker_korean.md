# [리눅스] Bash docker 사용법: 컨테이너 관리

## Overview
Docker는 소프트웨어를 컨테이너라는 독립적인 환경에서 실행할 수 있도록 해주는 플랫폼입니다. 이를 통해 애플리케이션과 그 의존성을 패키징하고 배포할 수 있으며, 다양한 환경에서 일관된 실행을 보장합니다.

## Usage
Docker 명령어의 기본 구문은 다음과 같습니다.

```bash
docker [options] [arguments]
```

## Common Options
- `run`: 새로운 컨테이너를 생성하고 실행합니다.
- `ps`: 현재 실행 중인 컨테이너 목록을 표시합니다.
- `stop`: 실행 중인 컨테이너를 중지합니다.
- `rm`: 중지된 컨테이너를 삭제합니다.
- `images`: 로컬에 저장된 이미지 목록을 표시합니다.

## Common Examples
- 새로운 컨테이너 실행하기:
```bash
docker run hello-world
```

- 실행 중인 컨테이너 목록 보기:
```bash
docker ps
```

- 특정 컨테이너 중지하기:
```bash
docker stop <컨테이너_ID>
```

- 중지된 컨테이너 삭제하기:
```bash
docker rm <컨테이너_ID>
```

- 로컬 이미지 목록 보기:
```bash
docker images
```

## Tips
- 컨테이너를 실행할 때 `-d` 옵션을 사용하면 백그라운드에서 실행할 수 있습니다.
- `--rm` 옵션을 사용하면 컨테이너가 종료될 때 자동으로 삭제됩니다.
- Dockerfile을 사용하여 이미지 빌드를 자동화하면 효율성을 높일 수 있습니다.