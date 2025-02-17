# [리눅스] Bash virsh 사용법: 가상 머신 관리

## Overview
virsh는 KVM, QEMU와 같은 가상화 기술을 사용하는 시스템에서 가상 머신을 관리하기 위한 명령줄 도구입니다. 이 명령어를 사용하면 가상 머신의 생성, 시작, 중지, 삭제 및 상태 확인 등을 수행할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```
virsh [options] [arguments]
```

## Common Options
- `list`: 현재 실행 중인 가상 머신의 목록을 표시합니다.
- `start <vm-name>`: 지정한 가상 머신을 시작합니다.
- `shutdown <vm-name>`: 지정한 가상 머신을 정상적으로 종료합니다.
- `destroy <vm-name>`: 지정한 가상 머신을 강제로 종료합니다.
- `define <xml-file>`: XML 파일을 사용하여 가상 머신을 정의합니다.

## Common Examples
- 실행 중인 가상 머신 목록 보기:
  ```bash
  virsh list
  ```

- 가상 머신 시작하기:
  ```bash
  virsh start my-vm
  ```

- 가상 머신 정상 종료하기:
  ```bash
  virsh shutdown my-vm
  ```

- 가상 머신 강제 종료하기:
  ```bash
  virsh destroy my-vm
  ```

- 새로운 가상 머신 정의하기:
  ```bash
  virsh define /path/to/vm.xml
  ```

## Tips
- 가상 머신의 상태를 확인할 때 `virsh list --all` 옵션을 사용하면 모든 가상 머신의 상태를 볼 수 있습니다.
- XML 파일을 사용하여 가상 머신을 정의할 때, 정확한 구문을 유지하는 것이 중요합니다.
- 가상 머신을 시작하거나 종료할 때, 필요한 권한이 있는지 확인하세요.