# 구현 계획서: Mock 데이터 분리 (Separate Mock Data)

**상태**: ✅ 완료 (Completed)
**시작일**: 2025-12-24
**완료 예정일**: 2025-12-24
**최종 수정일**: 2025-12-24

---

**⚠️ 중요 지침**: 각 단계(Phase) 완료 후 Check & Quality Gate 검증 필수.

---

## 📋 개요 (Overview)

### 기능 설명
현재 `app/main/__init__.py` 뷰 함수 내부에 하드코딩된 모의 데이터(District, Building, Predict)를 별도의 데이터 모듈(`app/main/mock_data.py`)로 분리합니다.
이를 통해 뷰 로직(`views.py`)과 데이터(`data`)를 분리하여 코드 가독성과 유지보수성을 향상시킵니다.

### 성공 기준
- [ ] `app/main/mock_data.py` 파일 생성 및 데이터 이동 완료.
- [ ] `app/main/__init__.py`는 `mock_data`를 임포트하여 사용해야 함.
- [ ] 기존 통합 테스트(`test_mock_api.py`)가 변경 없이 통과해야 함 (Refactoring).

### 사용자 영향
- **내부 개선**: 기능적 변화는 없음 (Refactoring).

---

## 🏗️ 아키텍처 결정사항

| 결정 항목 | 근거 | 트레이드오프 |
|----------|-----------|------------|
| **데이터 위치** | `app/main/mock_data.py` | 모듈 응집도 유지 (Main 모듈 전용 데이터) |
| **변수 네이밍** | `DISTRICT_DATA`, `BUILDING_DATA`, `PREDICT_DATA` | 상수 형태(대문자)로 정의하여 불변 데이터임 명시 |

---

## 📦 의존성 (Dependencies)

- 없음

---

## 🧪 테스트 전략

### 테스트 접근 방식
- **Regression Test**: 기존 `tests/integration/test_mock_api.py`가 리팩토링 후에도 여전히 통과하는지 확인합니다. 이는 데이터 구조나 값이 변하지 않았음을 보장합니다.

---

## 🚀 구현 단계 (Implementation Phases)

### Phase 1: 데이터 분리 및 리팩토링 🛠️
**목표**: 데이터를 이동시키고 뷰를 정리합니다.
**예상 소요 시간**: 30분

#### Tasks

**🔴 RED: (생략 - 리팩토링이므로 기존 테스트 활용)**
- 기존 `test_mock_api.py` 실행하여 Pass 상태 확인.

**🟢 GREEN: 데이터 분리**
- [x] **Task 1.1**: `app/main/mock_data.py` 생성
  - `DISTRICT_DATA`, `BUILDING_DATA`, `PREDICT_DATA` 정의
- [x] **Task 1.2**: `app/main/__init__.py` 리팩토링
  - 하드코딩 데이터 제거 및 `mock_data` 임포트 사용

**🔵 REFACTOR: 안정성 검증**
- [x] **Task 1.3**: 리팩토링 후 테스트 재실행

#### Quality Gate ✋
- [x] `make test` 통과

---

## 📊 진행 상황 추적

### 완료 상태
- **Phase 1**: ✅ 100%

**전체 진행률**: 100% 완료
