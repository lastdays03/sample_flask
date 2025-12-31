# 구현 계획서: 메인 페이지 디자인 적용 (Main Page Design)

**상태**: ✅ 완료 (Complete)
**시작일**: 2025-12-24
**최종 수정일**: 2025-12-24
**완료일**: 2025-12-24

---

## 📋 개요 (Overview)

### 기능 설명
참조 프로젝트(`flask-property`)의 메인 대시보드 디자인과 레이아웃을 현재 프로젝트에 적용합니다. 
Bootstrap 5 기반의 `base.html` 레이아웃을 구축하고, 메인 대시보드(`index.html`)의 UI 요소를 이식합니다. 
아직 백엔드 로직(데이터 분석, 예측)이 없으므로, **Mock API**를 제공하여 대시보드가 시각적으로 정상 동작하도록 구현합니다.

### 성공 기준 (Success Criteria)
- [ ] `base.html`이 적용되어 상단 네비게이션과 푸터가 모든 페이지에 표시된다.
- [ ] 인증 페이지(로그인/회원가입)가 `base.html` 스타일을 따른다.
- [ ] 메인 페이지 접속 시 차트와 테이블이 포함된 대시보드가 렌더링된다.
- [ ] 차트와 테이블에 (샘플) 데이터가 표시되며 콘솔 에러가 없다.
- [ ] 정적 파일(CSS)이 올바르게 로드된다.

---

## 🏗️ 아키텍처 결정 (Architecture Decisions)

| 결정 사항 | 근거 (Rationale) |
|---|---|
| **Mock API 구현** | 메인 페이지 JS가 백엔드 API를 호출하므로, UI 확인을 위해 더미 데이터를 반환하는 엔드포인트를 임시로 `main` 블루프린트에 구현합니다. |
| **CDN 활용** | 참조 프로젝트와 동일하게 Bootstrap과 Chart.js는 CDN을 통해 로드합니다. |

---

## 🧪 테스트 전략 (Test Strategy)

### 테스트 피라미드
| 테스트 유형 | 목표 | 방법 |
|---|---|---|
| **Integration Tests** | 페이지 렌더링 확인 | `templates` 폴더 내 파일 존재 여부 및 응답 코드 200 확인 |
| **E2E Tests** | UI 요소 확인 | 실제 브라우저 렌더링 대신, HTML 응답 내 주요 태그(`canvas`, `table`) 존재 여부 확인 |

---

## 🚀 구현 단계 (Implementation Phases)

### Phase 1: 기본 레이아웃 및 정적 자원 설정 🎨
**목표**: `base.html`과 `style.css`를 이식하고 기존 페이지에 적용합니다.

#### Tasks
- [x] **Task 1.1**: `app/static/css/style.css` 생성 (참조 코드 복사)
- [x] **Task 1.2**: `app/templates/base.html` 생성 (참조 코드 복사, Navbar 링크 수정)
- [x] **Task 1.3**: `app/templates/auth/`의 `login.html`, `register.html`이 `base.html`을 상속받도록 수정
- [x] **Integration Test**: 로그인/회원가입 페이지가 정상적으로 렌더링(`base.html` 포함)되는지 검증

### Phase 2: 메인 대시보드 UI 이식 📊
**목표**: 메인 페이지(`index.html`)를 생성하고 차트 라이브러리를 연동합니다.

#### Tasks
- [x] **Task 2.1**: `app/templates/main/index.html` 생성 (참조 코드 복사)
- [x] **Task 2.2**: `app/main/__init__.py`의 `index` 라우트가 `main/index.html`을 렌더링하도록 수정
- [x] **Task 2.3**: `index.html` 내 불필요한 JS 로직(존재하지 않는 API 호출)을 안전하게 처리하거나 주석 처리 (Phase 3 대비)
- [x] **Integration Test**: 메인 페이지 접속 시 200 OK 및 캔버스 요소 확인

### Phase 3: Mock 데이터 연동 🔗
**목표**: 대시보드 차트가 작동하도록 가짜(Mock) API를 만듭니다.

#### Tasks
- [x] **Task 3.1**: `app/main/routes.py` (또는 `__init__.py`)에 Mock API 엔드포인트 구현
  - POST `/district` (자치구 데이터)
  - POST `/building` (건물 데이터)
  - POST `/predict/location` (법정동 데이터 - 라우트 경로 주의)
- [x] **Task 3.2**: `index.html`의 JS가 위 Mock API를 호출하도록 경로 확인/수정
- [x] **Integration Test**: Mock API 호출 시 JSON 응답 확인
- [x] **Validation**: 브라우저(또는 시뮬레이션)에서 차트 렌더링 확인

---

## ⚠️ 리스크 평가

| 리스크 | 완화 전략 |
|---|---|
| **API 경로 충돌** | Mock API는 나중에 실제 서비스로 교체하기 쉽게 별도 파일이나 명확한 주석으로 표시합니다. |
| **JS 라이브러리 버전** | 참조 프로젝트와 동일한 CDN 버전을 사용하여 호환성 문제를 방지합니다. |

---

## 🔄 롤백 전략

### Phase 1 실패 시
- `base.html` 삭제, Auth 템플릿 원복

### Phase 2/3 실패 시
- `app/templates/main/index.html` 삭제
- `app/main` 변경 사항 롤백
