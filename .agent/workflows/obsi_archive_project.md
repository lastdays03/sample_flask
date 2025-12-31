---
description: 완료된 프로젝트를 검증(Dependency Check), 정리(Cleanup) 후 안전하게 연도별 아카이브로 이동시킵니다.
---

# Expert Archive Project Workflow

프로젝트를 단순히 옮기는 것이 아니라, **종료 절차(Closing Ritual)**를 수행하여 시스템 무결성을 유지합니다.

### 1단계: 대상 선정 및 의존성 분석 (Analysis)
1.  **Selection**: `10_Projects` 목록에서 아카이빙할 프로젝트 선택.
2.  **Dependency Scan** (Pre-flight):
    *   해당 프로젝트 폴더 외부에서 이 프로젝트를 링크(`[[Project_Name]]`)하고 있는 문서가 있는지 `grep`으로 확인합니다.
    *   외부 링크가 있다면: "다른 문서에서 이 프로젝트를 참조 중입니다. 링크를 유지하시겠습니까?" 확인.

### 2단계: 프로젝트 정리 (Cleanup)
1.  **Status Tag Update**:
    *   모든 `.md` 파일의 `#status/active` 태그를 `#status/done`으로 일괄 변경 제안.
2.  **Junk Removal**:
    *   `.DS_Store`, 빈 폴더, 임시 파일 등이 있는지 검사하고 삭제를 제안합니다.
3.  **Unfinished Tasks**:
    *   프로젝트 내에 완료되지 않은 할 일(`- [ ]`)이 남아있는지 확인하고, "취소 처리"할지 "다른 곳으로 옮길지" 묻습니다.

### 3단계: 지식 수확 (Knowledge Harvesting)
1.  **Asset Identification**:
    *   프로젝트 내에 `notes/` 폴더가 있는지 확인합니다.
    *   *Prompt*: "이 프로젝트의 `notes`를 지식 베이스(`20_Learning`)로 이동하시겠습니까?"
2.  **Migration**:
    *   `obsi_knowledge_harvester` 워크플로우를 호출하여 가치 있는 문서를 지식 베이스로 보냅니다.

### 4단계: 이관 및 기록 (Move & Log)
1.  **Archive Destination**:
    *   `90_Archives/Projects/{YYYY}/` 경로 확보.
2.  **Move Operation**:
    *   폴더 이동 실행.
3.  **Manifest Creation**:
    *   이동된 폴더 내에 `_archive_meta.md` 파일을 생성하여 아카이빙 일시, 이유, 최종 상태를 기록합니다.

### 4단계: 인덱스 갱신 (Update Index)
1.  **Project List Update**:
    *   `10_Projects/README.md` 목록에서 해당 프로젝트를 제거하고 `90_Archives/README.md` 목록에 추가합니다.