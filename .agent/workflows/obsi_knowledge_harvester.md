---
description: 프로젝트나 인박스에 있는 실전 노트(Topic Note)를 지식 베이스(20_Learning)로 이관하고 연결성을 유지합니다.
---

# Expert Knowledge Harvester Workflow

`/obsi_concept_distiller`가 **"원자적 개념(Atomic Concept)"**을 추출한다면, 이 워크플로우는 **"실전 지식(Topic Note)"** 덩어리를 수확합니다.

### 1단계: 수확 대상 선정 (Selection)
1.  **Source Identification**:
    *   가치 있는 정보가 담긴 폴더를 선택합니다.
    *   예: `10_Projects/{Project}/notes` 또는 `99_Inbox`.
2.  **Filtering**:
    *   이관할 가치가 있는 파일(`High Value`)과 버릴 파일(`Junk`)을 구분합니다.

### 2단계: 최적 위치 선정 (Mapping)
1.  **Category Matching**:
    *   **`20_Learning/10_Topics/{Category}`** 구조를 스캔하여 가장 적합한 위치를 찾습니다.
    *   *Rules*:
        *   기술 스택 -> `Tech_Stack/{Technology}`
        *   일반 지식 -> `Domain/{Field}`
        *   없는 경우 -> 새로운 카테고리 폴더 생성 제안.

### 3단계: 이관 및 리팩토링 (Migration & Refactoring)
1.  **Physical Move**:
    *   파일을 물리적으로 이동시킵니다.
    *   *Naming Convention*: 필요 시 파일명 앞에 순서(`01_`)나 태그를 붙여 정렬을 돕습니다.
2.  **Metadata Update**:
    *   파일 상단(Frontmatter)에 `Source: [[Project_Name]]` 링크를 추가하여 출처를 명시합니다.
    *   `#project/note` 태그를 제거하고 `#knowledge/topic` 태그로 교체합니다.

### 4단계: 연결 유지 (Link Maintenance)
1.  **Update Backlinks**:
    *   이동된 파일을 링크하고 있던 기존 문서(Plan, Overview 등)들의 링크 경로를 자동으로 업데이트합니다. (옵시디언이 자동 처리하지만, 워크플로우에서 확인).
2.  **Leave Trace** (Optional):
    *   원래 위치에 "이 노트는 지식 베이스로 이동되었습니다"라는 안내 문구(Placeholder)를 남길지 묻습니다.
