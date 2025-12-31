---
description: 데이터 기반으로 한 주를 회고하고, 인박스 제로 및 액션 아이템 추출을 자동화하는 주간 리뷰 워크플로우입니다.
---

# Expert Weekly Review Workflow

단순한 회고가 아닌, **데이터 기반의 시스템 점검**과 **다음 주 계획 수립**을 완벽하게 지원합니다.

### 1단계: 데이터 수집 및 현황 파악 (Data Aggregation)
1.  **Inbox Audit**:
    *   `00_Inbox`의 파일 개수를 카운트하고 목록을 보여줍니다.
    *   "이번 주에 들어온 {N}개의 메모가 처리되지 않았습니다."
2.  **Activity Log**:
    *   지난 7일간 수정된 파일(`list_dir` with time filter or `grep`)을 분석하여 "이번 주의 주요 활동"을 요약합니다.
    *   "이번 주에는 주로 `10_Projects/Alpha` 프로젝트에 집중하셨네요."

### 2단계: 시스템 정리 (System Cleanup)
1.  **Inbox Zero Challenge**:
    *   인박스 파일들을 하나씩 제시하며 `Active Project`, `Learning`, `Archive`, `Delete` 중 선택하게 하여 이동시킵니다.
2.  **Orphaned Note Check**:
    *   `20_Learning` 폴더에서 연결이 없는(백링크 0) 노트를 찾아 연결을 제안합니다.

### 3단계: 회고 및 계획 (Review & Plan)
1.  **Weekly Note Synthesis**:
    *   `30_Journal/Weekly/{YYYY-Www}.md` 생성.
    *   지난 Daily Note들에서 `- [x]` (완료된 일)와 `TIL` 섹션을 추출하여 회고 노트에 자동 삽입합니다.
2.  **Action Item Extraction**:
    *   지난 노트들에서 완료되지 않은 할 일(`- [ ]`)을 검색하여 "이번 주로 이관하시겠습니까?" 묻습니다.
    *   승인 시 `30_Journal/Weekly/{This_Week}.md` 또는 `task.md`로 복사합니다.

### 4단계: 마무리 (Closing)
1.  **Next Week Goal**:
    *   다음 주의 핵심 목표(One Thing)를 묻고 Weekly Note 상단에 대문짝만하게 기록합니다.
