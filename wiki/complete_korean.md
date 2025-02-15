# [리눅스] Bash complete 사용법

## Overview
`complete` 명령어는 Bash에서 사용자 정의 자동 완성을 설정하는 데 사용됩니다. 이 명령어는 특정 명령어에 대해 자동 완성 기능을 추가하거나 수정할 수 있게 해 주며, 사용자가 입력하는 동안 적절한 옵션이나 인수를 제안하여 작업 효율성을 높이는 데 도움을 줍니다.

## Usage
`complete` 명령어의 기본 구문은 다음과 같습니다:

```bash
complete [옵션] [명령어]
```

### 일반 옵션
- `-o`: 자동 완성의 동작을 지정하는 옵션입니다. 예를 들어, `-o nospace`는 자동 완성 후에 공백을 추가하지 않도록 설정합니다.
- `-A`: 특정 유형의 인수를 자동 완성하도록 지정합니다. 예를 들어, `-A command`는 명령어 이름을 자동 완성합니다.
- `-F`: 사용자 정의 함수 이름을 지정하여 자동 완성을 구현합니다.

## Examples
### 예제 1: 기본 자동 완성 설정
다음 명령어는 `mycmd`라는 사용자 정의 명령어에 대해 자동 완성을 설정합니다.

```bash
complete -o nospace -W "start stop restart" mycmd
```
이렇게 설정하면 `mycmd`를 입력한 후 Tab 키를 누르면 `start`, `stop`, `restart` 중 하나를 선택할 수 있습니다.

### 예제 2: 사용자 정의 함수 사용
사용자 정의 함수를 사용하여 더 복잡한 자동 완성을 설정할 수 있습니다. 다음은 `mycmd`에 대해 사용자 정의 함수를 사용하는 예입니다.

```bash
_mycmd_completions() {
    local commands="start stop restart"
    COMPREPLY=($(compgen -W "$commands" -- "${COMP_WORDS[1]}"))
}
complete -F _mycmd_completions mycmd
```
이 예제에서는 `_mycmd_completions`라는 함수를 정의하고, `mycmd`에 대해 이 함수를 자동 완성으로 설정합니다.

## Tips
- 자동 완성을 설정할 때는 명령어의 사용 패턴을 고려하여 가장 자주 사용되는 인수나 옵션을 포함하는 것이 좋습니다.
- 사용자 정의 함수를 사용할 때는 `compgen`을 활용하여 동적으로 인수를 생성할 수 있습니다.
- 자동 완성 기능을 테스트할 때는 Bash 세션을 새로 시작하거나 `source` 명령어를 사용하여 변경 사항을 적용해야 합니다.