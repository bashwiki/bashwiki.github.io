# [리눅스] Bash vagrant 사용법

## Overview
`vagrant`는 개발 환경을 자동화하고 관리하기 위한 도구입니다. 주로 가상 머신을 생성하고 설정하는 데 사용되며, 다양한 운영 체제와 소프트웨어 스택을 손쉽게 배포할 수 있도록 도와줍니다. Vagrant는 개발자들이 일관된 환경에서 작업할 수 있도록 하여, "내 컴퓨터에서는 잘 되는데"라는 문제를 줄여줍니다.

## Usage
기본적인 `vagrant` 명령어의 구문은 다음과 같습니다:

```
vagrant [옵션] [명령어]
```

일반적으로 사용되는 몇 가지 옵션은 다음과 같습니다:

- `init`: 새로운 Vagrant 프로젝트를 초기화합니다.
- `up`: Vagrantfile에 정의된 가상 머신을 시작합니다.
- `halt`: 실행 중인 가상 머신을 중지합니다.
- `destroy`: 가상 머신을 삭제합니다.
- `ssh`: 가상 머신에 SSH로 접속합니다.

## Examples
1. 새로운 Vagrant 프로젝트를 초기화하고 Ubuntu 가상 머신을 설정하는 예시:

```bash
vagrant init ubuntu/bionic64
```

2. 가상 머신을 시작하고 SSH로 접속하는 예시:

```bash
vagrant up
vagrant ssh
```

3. 가상 머신을 중지하고 삭제하는 예시:

```bash
vagrant halt
vagrant destroy
```

## Tips
- Vagrantfile을 사용하여 가상 머신의 설정을 관리할 수 있습니다. 이 파일을 통해 네트워크 설정, 프로비저닝 스크립트 등을 정의할 수 있습니다.
- Vagrant의 다양한 플러그인을 활용하여 기능을 확장할 수 있습니다. 예를 들어, `vagrant-vbguest` 플러그인은 VirtualBox 게스트 추가 기능을 자동으로 설치해줍니다.
- 가상 머신의 상태를 관리하기 위해 `vagrant status` 명령어를 사용하여 현재 상태를 확인하세요.
- Vagrant를 사용하여 팀원들과 동일한 개발 환경을 공유하면 협업이 더 원활해집니다.