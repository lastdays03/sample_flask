# 구현 계획서: 사용자 인증 시스템 (User Authentication)

**상태**: ✅ 완료 (Complete)
**시작일**: 2025-12-24
**최종 수정일**: 2025-12-24
**완료일**: 2025-12-24

---

**⚠️ 중요 지침 (CRITICAL INSTRUCTIONS)**: 각 단계(Phase) 완료 후 반드시 다음을 수행하십시오:
1. ✅ 완료된 작업의 체크박스 표시
2. 🧪 모든 품질 게이트(Quality Gate) 검증 명령어 실행
3. ⚠️ 모든 품질 기준이 통과되었는지 확인
4. 📅 상단의 "최종 수정일" 업데이트
5. 📝 "노트 및 교훈" 섹션에 특이사항 기록
6. ➡️ 그 후 다음 단계로 진행

⛔ **품질 게이트를 통과하지 못한 상태에서 절대 다음 단계로 넘어가지 마십시오.**

---

## 📋 개요 (Overview)

### 기능 설명
기존 `flask-property` 앱을 참조하여, 새로운 프로젝트 구조에서 **Flask-Login**과 **SQLAlchemy**를 활용한 견고한 사용자 인증 시스템을 구축합니다.  
이 시스템은 사용자 등록(비밀번호 해싱 포함), 로그인, 로그아웃 기능을 포함하며, **엄격한 TDD(테스트 주도 개발)** 방식을 따릅니다.

### 성공 기준 (Success Criteria)
- [ ] 사용자는 고유한 이메일로 가입할 수 있어야 한다.
- [ ] 비밀번호는 DB 저장 전 반드시 안전하게 해싱되어야 한다. (평문 저장 금지)
- [ ] 사용자는 로그인하여 세션을 발급받고, 로그아웃하여 세션을 파기할 수 있어야 한다.
- [ ] 인증되지 않은 사용자는 보호된 라우트에 접근할 수 없다.
- [ ] **테스트 커버리지 80% 이상**을 달성해야 한다.

### 사용자 영향 (User Impact)
개인화된 부동산 관리 기능을 제공하기 위한 보안 기초를 마련하며, 사용자 데이터의 안전을 보장합니다.

---

## 🏗️ 아키텍처 결정 (Architecture Decisions)

| 결정 사항 | 근거 (Rationale) | 트레이드오프 (Trade-offs) |
|---|---|---|
| **새로운 프로젝트 구조** | 기존 레거시 코드와 분리하여 클린 아키텍처 적용 | 초기 설정 비용 발생 (`flask-property` 참조 필요) |
| **Flask-Login** | Flask 생태계의 표준 세션 관리 라이브러리 | 별도 라이브러리 의존성 추가 |
| **Werkzeug Security** | 검증된 내장 비밀번호 해싱 알고리즘 사용 | 별도 암호화 라이브러리 불필요 |
| **Pytest** | `unittest`보다 강력하고 간결한 테스트 프레임워크 | `conftest.py` 등 초기 설정 필요 |

---

## 📦 의존성 (Dependencies)

### 시작 전 요구사항
- [ ] 가상환경 및 기본 패키지 설치 구조 마련 (루트 경로)
- [ ] `docs/plans` 디렉토리 생성 (완료)

### 외부 라이브러리
- `Flask`
- `Flask-Login`
- `Flask-SQLAlchemy`
- `Flask-Migrate`
- `pytest`
- `pytest-flask`

---

## 🧪 테스트 전략 (Test Strategy)

### 테스트 접근 방식
**TDD 원칙**: 실패하는 테스트를 **먼저** 작성하고(Red), 이를 통과시키는 최소한의 코드를 작성(Green)한 후, 리팩토링(Refactor)합니다.

### 테스트 피라미드
| 테스트 유형 | 목표 커버리지 | 목적 |
|---|---|---|
| **Unit Tests** | ≥80% | User 모델(해싱 로직), 인증 유틸리티 검증 |
| **Integration Tests** | 주요 경로 | 로그인/회원가입 라우트 및 DB 연동 검증 |
| **E2E Tests** | 핵심 시나리오 | 전체 로그인 흐름 검증 (Test Client 활용) |

### 테스트 파일 구조
```
tests/
├── conftest.py          # App Fixture, DB 설정
├── unit/
│   └── test_models.py   # 모델 단위 테스트
└── integration/
    └── test_auth.py     # 인증 라우트 통합 테스트
```

---

## 🚀 구현 단계 (Implementation Phases)

### Phase 1: 테스트 인프라 및 의존성 설정 🏗️
**목표**: 현재 워크스페이스 루트에서 프로젝트를 초기화하고 테스트 환경을 구축합니다.
**예상 시간**: 1시간

#### Tasks

**🔴 RED: 실패하는 테스트 먼저 작성**
- [x] **Test 1.1**: `tests/unit/test_app_config.py` 작성
  - 내용: 앱이 생성되고 설정이 올바르게 로드되는지 확인
  - 예상 결과: 앱 팩토리가 아직 없으므로 실패

**🟢 GREEN: 테스트 통과를 위한 구현**
- [x] **Task 1.2**: 루트 경로에 `requirements.txt` 작성 (`Flask`, `pytest` 등 포함)
- [x] **Task 1.3**: 패키지 설치
- [x] **Task 1.4**: `app/__init__.py` (App Factory), `config.py` 기본 구현
- [x] **Task 1.5**: `tests/conftest.py`에 `app`, `client` fixture 구현
- [x] **Task 1.6**: Test 1.1 통과 확인

**🔵 REFACTOR: 코드 개선**
- [x] **Task 1.7**: `create_app` 구조가 확장에 용이한지 점검

#### Quality Gate ✋
- [x] `pytest` 실행 시 1개 이상의 테스트 통과
- [x] 가상환경에 모든 의존성이 설치됨

---

### Phase 2: 사용자 모델 및 보안(해싱) 구현 👤
**목표**: 비밀번호 해싱 기능이 포함된 User 모델을 구현합니다.
**예상 시간**: 1시간

#### Tasks

**🔴 RED: 실패하는 테스트 먼저 작성**
- [x] **Test 2.1**: `tests/unit/test_models.py` 작성
  - `User` 인스턴스 생성 테스트
  - `password` 속성 읽기 시도 시 에러 발생 확인 (보안)
  - `password` 설정 시 `password_hash` 자동 생성 확인
  - `verify_password` 메서드 동작 확인

**🟢 GREEN: 테스트 통과를 위한 구현**
- [x] **Task 2.2**: `app/models.py` 생성 및 `User` 클래스 구현
  - `db`, `UserMixin` 상속
  - `password` setter/property 구현 (Werkzeug security 활용)
- [x] **Task 2.3**: `flask db init/migrate/upgrade` 실행하여 DB 테이블 생성

**🔵 REFACTOR: 코드 개선**
- [x] **Task 2.4**: 모델 필드 타입 힌팅 추가 및 문서화

#### Quality Gate ✋
- [x] 모델 단위 테스트 통과
- [x] 로컬 DB(`local.sqlite`)에 users 테이블 생성 확인

---

### Phase 3: 인증 로직 및 라우트 구현 🔐
**목표**: 실제 로그인/회원가입 웹 인터페이스와 라우트를 구현합니다.
**예상 시간**: 2시간

#### Tasks

**🔴 RED: 실패하는 테스트 먼저 작성**
- [x] **Test 3.1**: `tests/integration/test_auth_routes.py` 작성
  - `/auth/register` POST 요청 (유저 생성 확인)
  - `/auth/login` POST 요청 (세션 생성 확인)
  - `/auth/logout` 요청 (세션 종료 확인)

**🟢 GREEN: 테스트 통과를 위한 구현**
- [x] **Task 3.2**: `app/auth/` 블루프린트 생성 및 등록
- [x] **Task 3.3**: `LoginManager` 설정 (`app/__init__.py`) 및 `user_loader` 구현
- [x] **Task 3.4**: 로그인/회원가입 템플릿(HTML) 작성 (기존 앱 참조하되 간소화)
- [x] **Task 3.5**: 라우트 로직 구현 (`login`, `register`, `logout`)

**🔵 REFACTOR: 코드 개선**
- [x] **Task 3.6**: 폼 검증 로직 분리 (필요 시)
- [x] **Task 3.7**: 중복된 라우트 코드 정리

#### Quality Gate ✋
- [x] 모든 통합 테스트 통과
- [x] 브라우저 등을 통한 수동 검증 시 로그인 성공

---

## ⚠️ 리스크 평가 (Risk Assessment)

| 리스크 | 확률 | 영향도 | 완화 전략 |
|---|---|---|---|
| **기존 코드 참조 오류** | 중간 | 중간 | 기존 앱(`flask-property`) 코드를 단순히 복사하지 않고, 현재 구조에 맞게 재작성하며 테스트로 검증 |
| **DB 마이그레이션 충돌** | 낮음 | 높음 | 새 프로젝트이므로 초기 마이그레이션을 신중하게 생성 (`flask db init` 부터 시작) |

---

## 🔄 롤백 전략 (Rollback Strategy)

### Phase 1 실패 시
- 생성된 `flask-property-refactored` 디렉토리 삭제 후 재시도

### Phase 2 실패 시
- `migrations` 폴더 삭제 및 DB 파일 삭제 후 `flask db init` 재수행
- `models.py` 변경 사항 롤백

### Phase 3 실패 시
- `app/auth` 디렉토리 제거
- `app/__init__.py`에서 블루프린트 등록 해제
