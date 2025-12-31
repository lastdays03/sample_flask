# 구현 계획서: 인증 모듈 리팩토링 (Auth Refactoring)

**상태**: ✅ 완료 (Completed)
**시작일**: 2025-12-24
**완료 예정일**: 2025-12-24
**최종 수정일**: 2025-12-24

---

**⚠️ 중요 지침**: 각 단계(Phase) 완료 후 다음을 수행하십시오:
1. ✅ 완료된 태스크 체크박스 표시
2. 🧪 모든 품질 게이트(Quality Gate) 검증 명령어 실행
3. ⚠️ 모든 품질 게이트 항목이 통과하는지 확인
4. 📅 상단의 "최종 수정일" 업데이트
5. 📝 "노트 및 배운 점" 섹션에 기록
6. ➡️ 그 후 다음 단계로 진행

⛔ **품질 게이트를 건너뛰거나 실패한 상태로 진행하지 마십시오.**

---

## 📋 개요 (Overview)

### 기능 설명
현재 수동으로 폼 데이터를 처리(`request.form`)하고 단순 `flash` 메시지로 에러를 처리하는 인증(Auth) 모듈을 리팩토링합니다.
`Flask-WTF`를 도입하여 폼 검증을 자동화 및 강화하고, 인프라 단계에서 구축한 **표준 예외 시스템(`BusinessException`)**을 전면 적용하여 코드의 일관성과 안정성을 높입니다.

### 성공 기준
- [ ] `Flask-WTF` (`LoginForm`, `RegistrationForm`)가 구현되고 뷰에 적용되어야 함.
- [ ] 모든 입력 값 검증(Validation)이 폼 클래스 내부에서 처리되어야 함.
- [ ] `views.py` 내의 `flash()` 직접 호출이 제거되고 `BusinessException` 또는 `form.errors`로 대체되어야 함.
- [ ] CSRF 보호가 모든 인증 폼에 적용되어야 함.
- [ ] 관련 테스트(`test_auth_routes.py`)가 리팩토링된 로직에 맞춰 업데이트되고 통과해야 함.

### 사용자 영향
- **보안 강화**: CSRF 공격 방지 및 엄격한 입력값 검증.
- **UX 개선**: 폼 입력 오류 시 필드별 상세 피드백 제공 가능 (템플릿 수정 시).

---

## 🏗️ 아키텍처 결정사항

| 결정 항목 | 근거 | 트레이드오프 |
|----------|-----------|------------|
| **Flask-WTF 도입** | Flask의 표준 폼 처리 라이브러리. CSRF 보호 자동화 및 유효성 검사 로직 캡슐화. | 새로운 의존성 추가 필요, 기존 템플릿 수정 필요. |
| **예외 처리 표준화** | 비즈니스 로직(로그인 실패 등) 오류를 `BusinessException`으로 통일하여 전역 핸들러에서 로깅 및 응답 처리. | 단순 `flash`보다 코드가 약간 길어질 수 있으나 유지보수성 향상. |

---

## 🛡️ 예외 처리 전략

| 시나리오 | 예상치 못한 동작 | 처리 전략 | 사용자 피드백 |
|----------|---------------------|-------------------|---------------|
| **폼 검증 실패** | 필수 값 누락, 형식 오류 | `form.validate_on_submit()` 실패 -> 폼 에러 노출 | 필드 옆 또는 상단에 구체적인 검증 에러 메시지 표시 |
| **로그인 실패** | 아이디/비번 불일치 | `BusinessException("Invalid email or password")` 발생 | 전역 핸들러가 Catch -> Flash 메시지 및 로그인 페이지 리다이렉트 (또는 에러 페이지) |
| **중복 가입 시도** | 이미 존재하는 이메일/사용자명 | `BusinessException("Email already registered")` 발생 | Flash 메시지 및 회원가입 페이지 리다이렉트 |

---

## 📦 의존성 (Dependencies)

### 외부 라이브러리 추가
- `Flask-WTF`
- `email_validator` (WTForms 이메일 검증용)

---

## 🧪 테스트 전략

### 테스트 접근 방식
- **Unit Test**: `forms.py`의 폼 클래스 단위 테스트 (유효/무효 데이터 주입).
- **Integration Test**: CSRF 토큰을 포함한 폼 전송 테스트.

### 커버리지 목표
- `app/auth/forms.py`: 100%
- `app/auth/views.py`: ≥ 80%

---

## 🚀 구현 단계 (Implementation Phases)

### Phase 1: 폼 클래스 구현 및 의존성 추가 📝
**목표**: `Flask-WTF` 설치 및 `forms.py` 구현, 단위 테스트 작성.
**예상 소요 시간**: 2시간
**상태**: ⏳ 대기 중

#### Tasks

**🔴 RED: 실패하는 테스트 작성**
- [x] **Test 1.1**: `tests/unit/test_auth_forms.py` 작성
  - `LoginForm`, `RegistrationForm` 임포트 시도 (실패 예상)
  - 유효하지 않은 데이터(이메일 형식 오류 등)로 폼 검증 실패 테스트

**🟢 GREEN: 테스트 통과를 위한 구현**
- [x] **Task 1.2**: 의존성 설치
  - `requirements.txt`에 `Flask-WTF`, `email_validator` 추가 및 설치
- [x] **Task 1.3**: `app/auth/forms.py` 구현
  - `LoginForm`: email, password, remember_me
  - `RegistrationForm`: email, username, password, Django 식 유효성 검사(선택)

**🔵 REFACTOR: 코드 개선**
- [x] **Task 1.4**: 폼 클래스 코드 정리 및 타입 힌트 추가
  - (이미 초기 구현 시 적용됨)

#### Quality Gate ✋
- [x] `make test` 통과 (폼 단위 테스트)
- [x] `make lint` 통과

---

### Phase 2: 뷰(View) 및 템플릿 리팩토링 🔄
**목표**: `views.py`에 폼 및 예외 처리 적용, `request.form` 제거.
**예상 소요 시간**: 3시간
**상태**: ⏳ 대기 중

#### Tasks

**🔴 RED: 실패하는 테스트 작성**
- [x] **Test 2.1**: 기존 통합 테스트(`test_auth_routes.py`) 실행 시 실패 확인 (CSRF 토큰 누락 때문)
- [x] **Test 2.2**: 중복 가입 시나리오 테스트 업데이트 (Exception 발생 확인)

**🟢 GREEN: 테스트 통과를 위한 구현**
- [x] **Task 2.3**: `Config`에 `SECRET_KEY` 확인 (CSRF에 필수)
- [x] **Task 2.4**: 템플릿(`login.html`, `register.html`) 수정
  - `form.hidden_tag()` 추가 (CSRF 토큰)
  - HTML input 대신 WTForms 필드 렌더링으로 교체
- [x] **Task 2.5**: `app/auth/views.py` 리팩토링
  - `request.form` -> `form.validate_on_submit()`
  - 에러 상황에서 `flash()` -> `BusinessException` (또는 폼 에러 활용)
    * *Note: 폼 검증 에러는 form.errors로 처리하고, 비즈니스 에러(로그인 실패 등)는 Exception으로 처리*

**🔵 REFACTOR: 코드 개선**
- [x] **Task 2.6**: 테스트 코드 업데이트
  - 클라이언트 요청 시 CSRF 토큰 포함하도록 `conftest.py`나 테스트 유틸 보강
  - (CSRF 테스트 별도 추가 완료)

#### Quality Gate ✋
- [x] 통합 테스트(`test_auth_routes.py`) 통과
- [x] 수동 테스트: 로그인/회원가입 정상 작동 확인

---

### Phase 3: 예외 처리 검증 및 마무리 ✅
**목표**: 리팩토링된 코드가 표준 예외 시스템과 잘 맞물리는지 확인.
**예상 소요 시간**: 1시간
**상태**: ⏳ 대기 중

#### Tasks

- [x] **Task 3.1**: 중복 가입 등의 엣지 케이스 로직 검토
  - `User.query.filter...` 로직을 서비스 레이어로 분리할지 결정 (이번엔 View 유지, 추후 분리)
- [x] **Test 3.2**: 예외 발생 시 로그 기록 확인 (Phase 2 인프라 활용)
  - (이미 `test_auth_routes.py` 로그 확인 완료)

#### Quality Gate ✋
- [x] `make all` 전체 통과

---

## 📊 진행 상황 추적

### 완료 상태
- **Phase 1**: ✅ 100%
- **Phase 2**: ✅ 100%
- **Phase 3**: ✅ 100%

**전체 진행률**: 100% 완료
