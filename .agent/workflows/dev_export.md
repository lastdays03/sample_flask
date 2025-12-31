---
description: 개발/학습 산출물을 Obsidian Inbox로 단순 복사(Export)하는 Dev 전용 워크플로우입니다.
---

# Dev Export Workflow

복잡한 동기화 로직 없이, 현재 프로젝트의 문서나 노트를 **Obsidian(00_Inbox)**으로 빠르게 내보냅니다.
지식 정리는 Obsidian 내에서 나중에 수행한다고 가정합니다.

### 1단계: 타겟 설정 (Target Configuration)
1.  **Obsidian Path Input**:
    *   Obsidian Vault의 최상위 절대 경로를 입력받습니다. (예: `/Users/me/Obsidian`)
    *   *Tip*: 이전에 입력한 경로가 설정 파일 등에 있다면 자동 로드 시도.
2.  **Verify Target**:
    *   `[Obsidian_Path]/00_Inbox` 디렉토리가 존재하는지 확인합니다.
    *   없다면 에러 메시지 출력 후 중단.

### 2단계: 소스 선택 (Source Selection)
1.  **Scan for Documents**:
    *   현재 프로젝트 내의 `docs/`, `notes/`, `README.md` 등을 감지합니다.
2.  **Select Items**:
    *   사용자에게 내보낼 폴더나 파일을 선택하게 합니다. (기본값: `docs/` 전체).

### 3단계: 내보내기 (Export execution)
1.  **Prepare Destination**:
    *   타겟 경로: `[Obsidian_Path]/00_Inbox/{Project_Name}_Export`
    *   폴더 생성 (`mkdir -p`).
2.  **Copy Operation**:
    *   선택된 항목들을 `cp -R` 명령어로 복사합니다.
    *   *Overwrite Check*: 타겟에 이미 같은 파일이 있다면 덮어쓸지 묻습니다.
3.  **Result Log**:
    *   복사된 파일 목록이나 개수를 간단히 출력합니다.
    *   "Export Complete: Check your Obsidian Inbox."

### 4단계: 사후 안내 (Next Steps)
1.  **Obsidian Action**:
    *   "Obsidian을 열어 `00_Inbox/{Project_Name}_Export` 폴더를 확인하고, `obsi_knowledge_harvester` 등을 사용해 정리하세요."라고 안내합니다.
