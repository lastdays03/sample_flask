---
description: 표준 구조(Overview, Plan 등)를 갖춘 새로운 프로젝트를 자동으로 생성하며, 중복 검사 및 템플릿 선택 기능을 포함합니다.
---

# Expert Project Kickoff Workflow

새로운 프로젝트를 시작할 때 이 워크플로우를 실행하세요. 단순 생성이 아닌, **검증된 절차**를 통해 프로젝트 환경을 완벽하게 구축합니다.

### 1단계: 프로젝트 정의 및 검증 (Discovery & Validation)
1.  **Project Name Input**:
    *   사용자에게 프로젝트 이름을 요청합니다. (Naming Convention: `PascalCase` or `snake_case` 권장)
2.  **Conflict Check** (Pre-flight):
    *   `10_Projects/{Project_Name}` 폴더가 이미 존재하는지 `find_by_name`으로 확인합니다.
    *   존재한다면: "이미 존재하는 프로젝트입니다. 다른 이름을 선택하거나 기존 프로젝트를 여시겠습니까?" 라고 묻고 중단하거나 안내합니다.

### 2단계: 유형 선택 및 템플릿 로드 (Template Selection)
1.  **Project Type**:
    *   "어떤 유형의 프로젝트인가요?" (1. **Study/Learning**, 2. **Development**, 3. **Writing**)
2.  **Config Loading**:
    *   선택된 유형에 따라 다른 폴더 구조와 초기 할 일을 준비합니다.
    *   **Study**: `docs/plans/` 폴더 생성, `dev_study_planner` 호출 제안.
    *   *Dev*: `src`, `docs` 폴더 구조 제안, Git Init 제안.

### 3단계: 실행 및 생성 (Execution)
1.  **Directory Creation**:
    *   `10_Projects/{Project_Name}` 및 하위 폴더(`resources`, `notes` 등) 생성.
2.  **MOC Generation**: `Overview.md` 생성
    ```markdown
    # {Project_Name} Overview
    **Status**: #status/active
    **Goal**: [목표 입력]
    **Tags**: #project/{type}

    ## 🗺️ Navigation
    - [[{Project_Name}_Plan]]
    - [[{Project_Name}_Log]]
    ```
3.  **Task Management**: `task.md` 생성
    *   초기 체크리스트에 "목표 설정", "자료 수집" 등을 자동 추가.

### 4단계: 사후 설정 (Post-flight)
1.  **Git Initialization** (Optional):
    *   개발 프로젝트인 경우, `git init` 실행 여부를 묻습니다.
2.  **Finalize**:
    *   생성된 `Overview.md` 파일 경로를 출력하고, 즉시 `view_file`로 내용을 보여줄지 묻습니다.
