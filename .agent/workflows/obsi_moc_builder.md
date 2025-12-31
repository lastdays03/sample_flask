---
description: 특정 폴더나 주제의 노트들을 분석하여 구조화된 MOC(Map of Content)를 자동 생성합니다.
---

# Expert MOC Builder Workflow

흩어진 노트들을 모아 **지도의 역할(Map)**을 하는 MOC 노트를 생성합니다.

### 1단계: 범위 설정 (Scoping)
1.  **Target Selection**:
    *   MOC를 만들 대상 **폴더**(예: `20_Learning/React`) 또는 **태그**(예: `#topic/ai`)를 선택하게 합니다.
2.  **File Gathering**:
    *   `list_dir` 또는 `grep`으로 해당 범위 내의 모든 `.md` 파일을 수집합니다.
    *   *Exclude*: 이미 MOC인 파일(`_MOC`, `Overview`)이나 첨부파일은 제외합니다.

### 2단계: 구조화 및 클러스터링 (Clustering)
1.  **Analysis**:
    *   수집된 파일들의 제목과 태그를 분석하여 **하위 주제(Sub-topics)**를 식별합니다.
    *   예: "React" 관련 파일들 -> `Hooks`, `Components`, `State Management` 등으로 그룹화.
2.  **Drafting**:
    *   MOC 파일명: `{Topic}_MOC.md`
    *   **Structure**:
        *   **Core Concepts**: 가장 중요하고 기본적인 노트 링크.
        *   **Topics**: 클러스터링된 그룹별 링크 목록.
        *   **Uncategorized**: 기타 노트.

### 3단계: 생성 및 연결 (Generation & Linking)
1.  **Create File**:
    *   구조화된 내용을 바탕으로 MOC 파일을 생성합니다.
    *   형식:
        ```markdown
        # {Topic} Map of Content
        **Last Updated**: YYYY-MM-DD
        **Tags**: #moc

        ## 🔑 Key Concepts
        - [[Note A]]
        - [[Note B]]

        ## 📂 By Topic
        ### {Sub_Topic 1}
        - [[Note C]]
        ...
        ```
2.  **Upward Linking** (Optional):
    *   포함된 하위 노트들에 `Up: [[{Topic}_MOC]]` 링크를 추가하여, 하위 노트에서 상위 지도로 갈 수 있게 할지 묻습니다.

### 4단계: 시각화 제안 (Visualization)
1.  **Graph View**:
    *   "이 MOC를 중심으로 한 로컬 그래프를 열어보시겠습니까?" 제안.
