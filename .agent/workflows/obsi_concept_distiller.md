---
description: AI를 활용해 핵심 개념을 추출하고, 문맥을 분석하여 지식 베이스(20_Learning)와 양방향으로 연결합니다.
---

# Expert Concept Distiller Workflow

단순한 노트 생성을 넘어, **지식의 연결성(Connectivity)**을 강화하는 워크플로우입니다.

### 1단계: 문맥 분석 및 추출 (Context Analysis)
1.  **Source Input**: 원본 텍스트나 파일 경로 입력.
2.  **AI Extraction**:
    *   내용을 분석하여 "가장 가치 있는 핵심 키워드(Concept)" 1~3개를 추출합니다.
    *   *Criterion*: 재사용 가능한 지식인가? 범용적인 개념인가?

### 2단계: 중복 방지 및 연결 (De-duplication)
1.  **Existence Check**:
    *   추출된 키워드가 `20_Learning` 내에 이미 존재하는지 `find_by_name`으로 확인합니다.
    *   *Exist*: "이미 존재하는 개념입니다. 해당 노트에 내용을 추가(Append)하시겠습니까?"
    *   *New*: 새로운 개념 생성을 진행합니다.

### 3단계: 지식 노트 생성 (Creation)
1.  **Category Suggestion**:
    *   개념의 성격에 따라 **`20_Learning/00_Concepts/{Category}`** 경로를 제안합니다.
    *   *Categories*: `Tech_Stack`, `CS_Concepts`, `Domain`.
2.  **Drafting**:
    *   표준 템플릿(Definition, Usage, Example)에 맞춰 초안을 작성합니다.
    *   **Source Link**: `Data Source: [[Original_File]]` 백링크를 최상단에 자동 삽입합니다.

### 4단계: 생태계 연결 (Ecosystem Linking)
1.  **Bidirectional Update**:
    *   원본 파일(Source File)로 돌아가서, 해당 키워드가 언급된 부분을 찾아 `[[Concept]]` 링크로 치환(Replace)할지 묻습니다.
    *   이로써 원본과 지식 노트가 서로를 가리키게 됩니다.
