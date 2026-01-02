# Implementation Plan: Flask Template Refinement

**Status**: ✅ Complete
**Started**: 2026-01-02
**Last Updated**: 2026-01-02
**Estimated Completion**: 2026-01-02

---

**⚠️ CRITICAL INSTRUCTIONS**: After completing each phase:
1. ✅ Check off completed task checkboxes
2. 🧪 Run all quality gate validation commands
3. ⚠️ Verify ALL quality gate items pass
4. 📅 Update "Last Updated" date above
5. 📝 Document learnings in Notes section
6. ➡️ Only then proceed to next phase

⛔ **DO NOT skip quality gates or proceed with failing checks**

---

## 📋 Overview

### Feature Description
본 프로젝트를 "Flask Standard Template"으로 격상시키기 위해, 엔터프라이즈급 애플리케이션에 필수적인 **API 문서화자동화**, **구조적 로깅(Observability)**, **보안 강화(Security Hardening)** 기능을 추가합니다.

### Success Criteria
- [ ] Swagger UI(`/api/docs`)를 통해 API 명세를 확인하고 테스트할 수 있어야 함 using `flask-smorest` or `flasgger`.
- [ ] 운영 환경(Production)에서 로그가 JSON 포맷으로 출력되고, 모든 로그에 `request_id`가 포함되어야 함.
- [ ] HTTP 보안 헤더(HSTS, CSP 등)가 적용되고, API 엔드포인트에 Rate Limiting이 적용되어야 함.

### User Impact
- 개발자는 스웨거를 통해 쉽게 API를 파악하고 연동할 수 있음.
- 운영자는 로그를 통해 문제 상황을 빠르게 추적(Tracing)할 수 있음.
- 사용자는 보안 위협으로부터 더 안전한 서비스를 제공받음.

---

## 🏗️ Architecture Decisions

| Decision                      | Rationale                                                                     | Trade-offs                                                                          |
| ----------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Use `flask-smorest`**       | Marshmallow 기반의 Validation과 OpenAPI 스펙 자동 생성을 강력하게 지원함.     | `flasgger`보다 러닝커브가 약간 있으나, 모델 정의가 더 깔끔함.                       |
| **JSON Logging**              | ELK 스택이나 Cloudwatch 등 로그 수집기에서의 파싱 효율성을 위해 필수.         | 로컬 개발 시 가독성이 떨어질 수 있으므로 Dev 환경에선 일반 텍스트로 분기 처리 필요. |
| **Middleware for Request ID** | `before_request`, `after_request` 훅을 사용하여 모든 로그 컨텍스트에 ID 주입. | Flask `g` 객체 사용에 따른 오버헤드는 미미함.                                       |

---

## 🛡️ Exception Handling Strategy

| Scenario                | Unexpected Behavior    | Handling Strategy                                      | User Feedback         |
| ----------------------- | ---------------------- | ------------------------------------------------------ | --------------------- |
| **Validation Error**    | API 요청 스키마 불일치 | `422 Unprocessable Entity` 반환 및 상세 에러 필드 명시 | JSON 에러 응답        |
| **Rate Limit Exceeded** | 과도한 API 요청        | `429 Too Many Requests`                                | Retry-After 헤더 포함 |
| **Security Violation**  | CSRF/XSS 공격 시도     | `400 Bad Request` or `403 Forbidden`                   | 보안 위반 경고        |

---

## 📦 Dependencies

### Required Before Starting
- [x] Existing Flask App Structure (Confirmed)
- [x] Test Suite (Confirmed)

### External Dependencies
- `flask-smorest`: API 문서화 및 검증
- `marshmallow`: 데이터 스키마 정의
- `python-json-logger`: JSON 로그 포맷팅
- `flask-talisman`: 보안 헤더 설정
- `flask-limiter`: Rate Limiting

---

## 🧪 Test Strategy

### Testing Approach
**TDD Principle**: 각 기능 추가 전, 해당 기능의 부재를 확인하는 테스트를 먼저 작성(Red)하고 구현(Green)합니다.

### Test Pyramid for This Feature
| Test Type             | Coverage Target | Purpose                                                      |
| --------------------- | --------------- | ------------------------------------------------------------ |
| **Unit Tests**        | ≥90%            | 로그 포맷터, Request ID 생성 로직, 스키마 검증 로직 테스트   |
| **Integration Tests** | Critical paths  | Swagger UI 접근성, 보안 헤더 적용 여부, Rate Limit 동작 확인 |

---

## 🚀 Implementation Phases

### Phase 1: API Documentation (Swagger/OpenAPI)
**Goal**: `flask-smorest`를 도입하여 API 문서화 기반 마련 및 예시 Blueprint 적용.
**Estimated Time**: 2 hours

#### Tasks

**🔴 RED: Write Failing Tests First**
- [ ] **Test 1.1**: Swagger UI Endpoint 접근 테스트
  - File: `tests/integration/test_api_docs.py`
  - Expected: 404 Not Found (아직 설정 안됨)
- [ ] **Test 1.2**: API Schema Validation 테스트 (Mock Endpoint)
  - File: `tests/unit/test_api_schema.py`

**🟢 GREEN: Implement to Make Tests Pass**
- [ ] **Task 1.3**: `flask-smorest` 의존성 추가 및 `Config` 설정 업데이트
- [ ] **Task 1.4**: `Api` 객체 초기화 및 `app/__init__.py` 등록
- [ ] **Task 1.5**: 예시 API Blueprint (`app/api/example.py`) 생성 및 등록

**🔵 REFACTOR: Clean Up Code**
- [ ] **Task 1.6**: 기존 `errors.py`의 JSON 응답 로직을 `flask-smorest` 에러 핸들러와 통합 고려
- [ ] **Task 1.7**: API 관련 설정을 `config.py`로 이동

#### Quality Gate ✋
- [ ] **Build**: `make test` 통과
- [ ] **Docs**: `/api/docs` 접속 시 Swagger UI 정상 출력 확인

---

### Phase 2: Observability (Structured Logging & Request ID)
**Goal**: 운영 환경에서의 디버깅 편의성을 위해 로그 구조화 및 추적 ID 도입.
**Estimated Time**: 2 hours

#### Tasks

**🔴 RED: Write Failing Tests First**
- [ ] **Test 2.1**: 로그 포맷 검증 테스트 (Dev: Text, Prod: JSON)
  - File: `tests/unit/test_logging.py`
- [ ] **Test 2.2**: Request ID 주입 및 Response Header 확인 테스트
  - File: `tests/integration/test_request_id.py`

**🟢 GREEN: Implement to Make Tests Pass**
- [ ] **Task 2.3**: `RequestIDMiddleware` 구현 (utils 또는 middlewares 패키지)
- [ ] **Task 2.4**: `python-json-logger` 설정 및 `app/__init__.py` 로깅 설정 고도화

**🔵 REFACTOR: Clean Up Code**
- [ ] **Task 2.5**: 중복 로깅 설정 제거 및 `logging` 모듈 설정 중앙화

#### Quality Gate ✋
- [ ] **Verification**: 로컬 실행 후 로그 파일(`logs/antigravity.log`)에 JSON 로그와 `request_id`가 찍히는지 확인.

---

### Phase 3: Security Hardening
**Goal**: 웹 보안 취약점 방어를 위한 기본 헤더 및 제한 설정.
**Estimated Time**: 1.5 hours

#### Tasks

**🔴 RED: Write Failing Tests First**
- [ ] **Test 3.1**: Security Headers (Content-Security-Policy, X-Frame-Options 등) 확인 테스트
  - File: `tests/integration/test_security.py`
- [ ] **Test 3.2**: Rate Limiting 동작 테스트 (임계치 초과 요청 시 429 확인)
  - File: `tests/integration/test_ratelimit.py`

**🟢 GREEN: Implement to Make Tests Pass**
- [ ] **Task 3.3**: `Flask-Talisman` 적용 (HTTPS 강제, 헤더 설정)
- [ ] **Task 3.4**: `Flask-Limiter` 적용 및 기본 정책 설정

**🔵 REFACTOR: Clean Up Code**
- [ ] **Task 3.5**: 환경별(Test 환경 등) Rate Limit 비활성화 옵션 확인

#### Quality Gate ✋
- [ ] **Security**: `curl -I` 명령어로 헤더 확인 시 보안 헤더 존재 여부 검증.

---

## ⚠️ Risk Assessment

| Risk                       | Probability | Impact | Mitigation Strategy                                                          |
| -------------------------- | ----------- | ------ | ---------------------------------------------------------------------------- |
| **Dependency Conflict**    | Low         | Medium | `requirements.txt` 버전 고정 및 가상환경 격리 철저                           |
| **Log Volume Increase**    | Medium      | Low    | JSON 포맷팅으로 인한 용량 증가는 `RotatingFileHandler` 설정으로 관리         |
| **Strict Security Checks** | Medium      | High   | 개발 환경(DevelopmentConfig)에서는 HTTPS 강제 등을 완화하여 개발 편의성 유지 |

---

## 🔄 Rollback Strategy

### If Phase 1 Fails
- `app/__init__.py`에서 `Api` 초기화 코드 제거
- `flask-smorest` 패키지 제거

### If Phase 2 Fails
- `app/__init__.py` 로깅 설정을 이전 상태로 복구

### If Phase 3 Fails
- `Flask-Talisman`, `Flask-Limiter` 초기화 코드 주석 처리

---
