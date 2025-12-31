---
description: 개발 환경(폴더 구조, README)을 신속하게 초기화하는 Dev 전용 워크플로우입니다.
---

# Dev Init Workflow

개발 또는 학습을 위한 프로젝트 환경을 초기화합니다.
에이전트 설정은 이미 복사되어 있다고 가정하며, **디렉토리 구조**와 **기본 문서(README)** 생성에 집중합니다.

### 1단계: 프로젝트 정의 (Project Definition)
1.  **Context Check**:
    *   현재 디렉토리가 비어있는지, 혹은 초기화하려는 프로젝트 루트가 맞는지 확인합니다.
2.  **Metadata Input**:
    *   프로젝트 이름(Name)과 유형(Type: Study/Dev)을 입력받습니다.

### 2단계: 스캐폴딩 (Scaffolding)
1.  **Tech Stack & Structure**:
    *   "어떤 언어나 프레임워크를 사용하시나요?"라고 묻습니다. (예: Python, Node.js, React, Simple Study 등)
    *   선택된 스택에 맞춰 적절한 폴더 구조를 제안하고 생성합니다.
        *   *Python*: `src/`, `tests/`, `docs/`, `scripts/`
        *   *Web/Frontend*: `public/`, `src/components`, `src/pages` (혹은 프레임워크 CLI 사용 제안)
        *   *Study*: `notebooks/`, `data/`, `references/`
    *   **User Confirmation**: 생성 전에 구조가 괜찮은지 사용자에게 확인합니다.
2.  **Git Setup** (Optional):
    *   `.gitignore` 파일이 없다면 생성을 제안합니다. (Python/Node 등 언어에 맞춰 내용 추천).
    *   **Crucial**: `.agent/` 디렉토리는 Git에 포함되어야 하므로, **`.gitignore`에 추가하지 않도록 주의**합니다.

### 3단계: 문서 생성 (Documentation)
1.  **README Generation**:
    *   프로젝트 루트에 `README.md`를 생성합니다.
    *   Obsidian과 연동하기 좋은 메타데이터 형식을 포함합니다.

    ```markdown
    # {Project_Name}

    > **Status**: Active
    > **Type**: {Type}
    > **Created**: {Date}

    ## 📖 Overview
    [프로젝트의 목표와 주요 내용을 간단히 작성하세요.]

    ## 🏗️ Structure
    [위 스캐폴딩 단계에서 생성된 폴더 구조를 자동으로 반영하여 작성합니다.]
    - `src/`: ...
    - `docs/`: ...
    (생성된 실제 폴더에 맞춰 설명을 추가)
    ```

### 4단계: 마무리 (Finalize)
1.  **Completion Message**:
    *   "개발 환경 초기화가 완료되었습니다."
    *   "`src/` 폴더에서 코딩을 시작하거나, `docs/`에 계획을 작성하세요." 안내.
