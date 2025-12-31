# 구현 계획서: 프론트엔드 에러 처리 및 표준화 (Frontend Error Handling)

**상태**: ✅ 완료 (Completed)
**시작일**: 2025-12-24
**완료 예정일**: 2025-12-24
**최종 수정일**: 2025-12-24

---

**⚠️ 중요 지침**: 각 단계(Phase) 완료 후 Check & Quality Gate 검증 필수.

---

## 📋 개요 (Overview)

### 기능 설명
현재 백엔드 에러 핸들러(`app/errors.py`)는 `{"error": message}` 형태의 비표준 JSON을 반환합니다. 이를 `app/utils.error_response`를 사용하여 `{ "status": "error", "message": ... }` 표준 포맷으로 통일합니다.
또한, 프론트엔드(`index.html`)에서 API 호출 실패 시 이 표준 포맷을 파싱하여 사용자에게 친절한 에러 메시지(Alert/Modal)를 보여주도록 개선합니다.

### 성공 기준
- [ ] `app/errors.py`가 `error_response` 유틸리티를 사용해야 함.
- [ ] API 호출 에러 발생 시(예: 400, 500), 프론트엔드에서 JS Alert 또는 UI 메시지가 표시되어야 함.
- [ ] 기존 에러 처리 테스트(`test_auth_exception.py` 등)가 변경된 JSON 스키마를 검증해야 함.

### 사용자 영향
- **사용자 경험**: 에러 발생 시 "알 수 없는 오류" 대신 구체적인(그러나 보안상 안전한) 메시지를 볼 수 있음.

---

## 🏗️ 아키텍처 결정사항

| 결정 항목 | 근거 | 트레이드오프 |
|----------|-----------|------------|
| **에러 포맷** | `{ "status": "error", "message": "...", "payload": ... }` | 기존 API 표준화(`PLAN_standardize_mock_api`)와 일치 |
| **JSON 감지** | `request.is_json` 활용 | `fetch` 호출 시 `Content-Type: application/json` 필수화 |

---

## 📦 의존성 (Dependencies)

- 없음

---

## 🧪 테스트 전략

### 테스트 접근 방식
- **Existing Test Update**: `tests/integration/test_auth_exception.py`와 `test_auth_csrf.py`에서 JSON 에러 응답 구조(`status`, `message`)를 검증하도록 수정합니다.
- **Frontend Verification**: 강제로 에러를 발생시키는(예: 잘못된 URL 또는 서버 에러 모사) 상황에서 UI 확인.

---

## 🚀 구현 단계 (Implementation Phases)

### Phase 1: 백엔드 에러 응답 표준화 🛠️
**목표**: 서버 에러 응답을 표준 포맷으로 변경하고 테스트를 수정합니다.
**예상 소요 시간**: 30분

#### Tasks

**🔴 RED: 실패하는 테스트 업데이트**
- [x] **Test 1.1**: `test_auth_csrf.py` (CSRF 실패 시 JSON 응답 검증 추가)
- [x] **Test 1.2**: `test_auth_exception.py` (로그인 실패 등 예외 발생 시 JSON 응답 구조 변경 반영)

**🟢 GREEN: 에러 핸들러 리팩토링**
- [x] **Task 1.3**: `app/errors.py` 리팩토링
  - `jsonify(...)` 대신 `error_response(...)` 사용
  - `CSRFError` 핸들러 추가 (Flask-WTF CSRF 에러도 JSON 반환 보장)

**🔵 REFACTOR: 검증**
- [x] **Task 1.4**: `make test` 실행

### Phase 2: 프론트엔드 연동 🎨
**목표**: 프론트엔드에서 표준 에러 응답을 처리합니다.
**예상 소요 시간**: 30분

#### Tasks

- [x] **Task 2.1**: `app/templates/main/index.html` JS 수정
  - `postData` 함수 내에서 `response.status !== 'success'` 체크
  - 에러 발생 시 `alert(response.message)` 실행 (추후 Modal로 고도화 가능)

#### Quality Gate ✋
- [x] `make test` 통과
- [x] 강제 에러 발생(예: 500 에러) 시 Alert 뜨는지 확인

---

## 📊 진행 상황 추적

### 완료 상태
- **Phase 1**: ✅ 100%
- **Phase 2**: ✅ 100%

**전체 진행률**: 100% 완료
