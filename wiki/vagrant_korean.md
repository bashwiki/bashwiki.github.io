# [리눅스] Bash vagrant 사용법: 가상 개발 환경 관리

## Overview
Vagrant는 개발 환경을 쉽게 설정하고 관리할 수 있도록 도와주는 도구입니다. 가상 머신을 사용하여 다양한 운영 체제에서 일관된 개발 환경을 제공하며, 팀원 간의 환경 차이를 줄이는 데 유용합니다.

## Usage
Vagrant의 기본 구문은 다음과 같습니다:

```bash
vagrant [options] [arguments]
```

## Common Options
- `init`: 새로운 Vagrant 프로젝트를 초기화합니다.
- `up`: Vagrantfile에 정의된 가상 머신을 시작합니다.
- `halt`: 실행 중인 가상 머신을 중지합니다.
- `destroy`: 가상 머신을 삭제합니다.
- `ssh`: 가상 머신에 SSH로 접속합니다.

## Common Examples
- 새로운 Vagrant 프로젝트 초기화:
  ```bash
  vagrant init
  ```

- 가상 머신 시작:
  ```bash
  vagrant up
  ```

- 가상 머신 중지:
  ```bash
  vagrant halt
  ```

- 가상 머신 삭제:
  ```bash
  vagrant destroy
  ```

- 가상 머신에 SSH로 접속:
  ```bash
  vagrant ssh
  ```

## Tips
- Vagrantfile을 잘 관리하여 팀원들이 동일한 환경을 쉽게 설정할 수 있도록 하세요.
- 가상 머신의 상태를 주기적으로 확인하고 필요 없는 가상 머신은 삭제하여 시스템 자원을 절약하세요.
- 다양한 플러그인을 활용하여 Vagrant의 기능을 확장할 수 있습니다.