# 구현 계획서: 메인 테스트 통합 및 커버리지 확대 (Refactor Main Tests)

**상태**: ✅ 완료 (Completed)
**시작일**: 2025-12-24
**완료 예정일**: 2025-12-24
**최종 수정일**: 2025-12-24

---

**⚠️ 중요 지침**: 각 단계(Phase) 완료 후 Check & Quality Gate 검증 필수.

---

## 📋 개요 (Overview)

### 기능 설명
현재 Main Blueprint의 테스트가 `test_main_routes.py`(페이지 렌더링)와 `test_mock_api.py`(API 데이터)로 파편화되어 있습니다.
이를 `test_main_routes.py` 하나로 통합하고, API 엔드포인트에 대한 추가적인 엣지 케이스(예: 잘못된 메서드 호출) 테스트를 추가하여 커버리지를 100%로 확실히 다집니다.

### 성공 기준
- [ ] `test_mock_api.py`의 내용이 `test_main_routes.py`로 이동되어야 함.
- [ ] `test_mock_api.py` 파일 삭제.
- [ ] `POST` 전용 API 엔드포인트에 `GET` 요청 시 405 Method Not Allowed 확인 테스트 추가.
- [ ] `make test` 전체 통과.

### 사용자 영향
- **유지보수성**: 테스트 파일 구조가 간결해짐.

---

## 🏗️ 아키텍처 결정사항

| 결정 항목 | 근거 | 트레이드오프 |
|----------|-----------|------------|
| **테스트 통합** | `test_main_routes.py` | 블루프린트 단위로 테스트 파일 관리 |

---

## 📦 의존성 (Dependencies)

- 없음

---

## 🧪 테스트 전략

### 테스트 접근 방식
- **Consolidation**: 기존 테스트 코드를 복사하되, 함수명이나 구조를 깔끔하게 정리.
- **Negative Testing**: 허용되지 않은 HTTP Method 테스트 추가.

---

## 🚀 구현 단계 (Implementation Phases)

### Phase 1: 테스트 통합 및 확장 🛠️
**목표**: 테스트 파일을 합치고 삭제합니다.
**예상 소요 시간**: 20분

#### Tasks

**Task 1.1**: 테스트 코드 이동
- [x] `test_mock_api.py`의 `test_mock_api_endpoints` 함수를 `test_main_routes.py`로 이동.
- [x] 이동 시 함수명을 `test_main_api_endpoints`로 변경.

**Task 1.2**: 엣지 케이스 추가
- [x] `test_main_routes.py`에 `test_api_method_not_allowed` 함수 추가.
  - `/district` 엔드포인트에 `GET` 요청 시 405 상태 코드 검증.

**Task 1.3**: 파일 정리
- [x] `test_mock_api.py` 삭제.

#### Quality Gate ✋
- [x] `make test` 통과

---

## 📊 진행 상황 추적

### 완료 상태
- **Phase 1**: ✅ 100%

**전체 진행률**: 100% 완료
