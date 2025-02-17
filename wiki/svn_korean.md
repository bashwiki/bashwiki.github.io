# [리눅스] Bash svn 사용법: 버전 관리 시스템을 위한 명령어

## Overview
`svn` 명령어는 Subversion(SVN)이라는 버전 관리 시스템을 사용하여 파일과 디렉토리의 변경 사항을 추적하고 관리하는 데 사용됩니다. 주로 소스 코드 관리에 활용되며, 여러 사용자가 동시에 작업할 수 있도록 도와줍니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
svn [options] [arguments]
```

## Common Options
- `checkout`: 원격 저장소에서 파일을 다운로드하여 로컬 작업 복사본을 만듭니다.
- `commit`: 로컬 변경 사항을 원격 저장소에 반영합니다.
- `update`: 원격 저장소의 변경 사항을 로컬 작업 복사본에 적용합니다.
- `add`: 새로운 파일 또는 디렉토리를 버전 관리에 추가합니다.
- `delete`: 버전 관리에서 파일 또는 디렉토리를 삭제합니다.
- `status`: 현재 작업 복사본의 상태를 확인합니다.

## Common Examples
- 원격 저장소에서 파일을 체크아웃할 때:
```bash
svn checkout https://example.com/svn/repo/trunk
```

- 로컬 변경 사항을 커밋할 때:
```bash
svn commit -m "수정 사항 반영"
```

- 원격 저장소의 최신 변경 사항을 업데이트할 때:
```bash
svn update
```

- 새로운 파일을 버전 관리에 추가할 때:
```bash
svn add newfile.txt
```

- 파일을 버전 관리에서 삭제할 때:
```bash
svn delete oldfile.txt
```

- 현재 작업 복사본의 상태를 확인할 때:
```bash
svn status
```

## Tips
- 커밋 메시지는 간결하고 명확하게 작성하여 변경 사항을 쉽게 이해할 수 있도록 하세요.
- 자주 업데이트하여 로컬 작업 복사본이 최신 상태를 유지하도록 하세요.
- 변경 사항을 커밋하기 전에 항상 `svn status`를 사용하여 현재 상태를 확인하세요.