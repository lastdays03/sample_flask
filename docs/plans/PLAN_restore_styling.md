# Implementation Plan: Style Restoration & Premium UI Upgrade

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
최근 적용된 `Flask-Talisman`의 강력한 **Content Security Policy (CSP)**로 인해, 외부 CDN(Bootstrap, FontAwesome 등)에서 스타일시트를 불러오지 못해 UI가 깨지는 현상이 발생했습니다. 또한 현재 `style.css`는 단순한 MVP 수준으로, 사용자가 요구하는 "Premium Aesthetic" 기준에 미달합니다. 본 계획은 CSP 문제를 해결하고 UI를 프리미엄 수준으로 고도화하는 것을 목표로 합니다.

### Success Criteria
- [ ] **CSP Fix**: CDN(Bootstrap, FontAwesome, Chart.js) 리소스가 정상적으로 로드되어야 함 (콘솔 에러 없음).
- [ ] **Premium Design**: Gradient, Glassmorphism, Micro-animations가 적용된 "Wow" 포인트가 있어야 함.
- [ ] **Responsive**: 모바일 및 데스크탑에서 레이아웃이 깨지지 않아야 함.

### User Impact
- 사용자는 깨진 UI 대신 정상적이고 아름다운 인터페이스를 경험하게 됨.
- 프리미엄 디자인(가독성, 미학)을 통해 서비스 신뢰도 및 사용자 만족도 향상.

---

## 🏗️ Architecture Decisions

| Decision                      | Rationale                                                                                                  | Trade-offs                                                   |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Allow CDNs in CSP**         | 로컬에 벤더 파일을 모두 저장하는 것보다 빠르고 간편하며 캐싱 이점이 있음.                                  | 외부 CDN 장애 시 스타일 깨질 위험 있음 (허용 가능한 리스크). |
| **Custom CSS Over Bootstrap** | Bootstrap은 그리드/레이아웃 용도로만 사용하고, 비주얼 스타일은 Custom CSS로 덮어씌워 유니크한 브랜딩 적용. | CSS 작성 공수가 다소 듦.                                     |
| **Modular CSS Variables**     | CSS Variables(Root)를 사용하여 테마(Color, Font, Spacing) 관리를 용이하게 함.                              | IE 지원 불가 (본 프로젝트 범위 아님).                        |

---

## 🛡️ Exception Handling Strategy

| Scenario             | Unexpected Behavior                | Handling Strategy                                                     | User Feedback              |
| -------------------- | ---------------------------------- | --------------------------------------------------------------------- | -------------------------- |
| **CDN Load Failure** | 외부 CDN 다운/차단시 스타일 미적용 | (Future) 로컬 Fallback 또는 에러 페이지 고려. 현재는 CSP 리포팅 확인. | 스타일 깨짐 (현재는 감수). |
| **CSP Violation**    | 브라우저 콘솔에 CSP 에러 로그      | `report_uri` 설정 또는 개발자 도구 확인 후 정책 조정.                 | 없음 (콘솔 로그).          |
| **Global**           | Unhandled Exceptions               | Log stack trace & Alert                                               | Generic error page         |

---

## 📦 Dependencies

### Required Before Starting
- [x] Existing Flask App Structure
- [x] `flask-talisman` (Installed)

### External Dependencies
- **CDNs**:
  - Bootstrap 5.2.3
  - FontAwesome 6.3.0
  - Chart.js 2.8.0
- **Google Fonts**: Inter, Outfit

---

## 🧪 Test Strategy

### Testing Approach
**TDD Principle**: 스타일 관련 작업이지만, **Selenium/Playwright** 같은 E2E 도구가 없는 환경이므로 `browser_subagent`를 활용한 시각적 검증(Browser Verification)과 **Integration Test(헤더 검사)**를 TDD 방식으로 수행합니다.

### Test Pyramid for This Feature
| Test Type             | Coverage Target  | Purpose                                          |
| --------------------- | ---------------- | ------------------------------------------------ |
| **Unit Tests**        | N/A              | CSS 스타일링은 단위 테스트 대상 아님.            |
| **Integration Tests** | Security Headers | CSP 헤더에 허용된 도메인이 포함되어 있는지 검증. |
| **Manual/Browser**    | Visual Check     | `browser_subagent`를 통해 실제 렌더링 확인.      |

### Test File Organization
```
test/
├── integration/
│   └── test_security.py  # CSP 헤더 검증 로직 추가
```

### Coverage Requirements by Phase
- **Phase 1 (CSP Fix)**: Integration Test (CSP Header Check) Pass
- **Phase 2 (Premium Design)**: Visual Verification via Browser Agent

---

## 🚀 Implementation Phases

### Phase 1: CSP Configuration Fix
**Goal**: Bootstrap 및 외부 라이브러리 로딩 정상화.
**Estimated Time**: 0.5 hours
**Status**: ⏳ Pending | 🔄 In Progress | ✅ Complete

#### Tasks

**🔴 RED: Write Failing Tests First**
- [ ] **Test 1.1**: CSP 헤더 검증 테스트 작성
  - File(s): `tests/integration/test_security.py`
  - Expected: Tests FAIL (red) - 현재 설정에는 특정 CDN 도메인이 명시되어 있지 않거나 차단됨.
  - Details: `Content-Security-Policy` 헤더 내용을 파싱하여 `cdn.jsdelivr.net` 등이 포함되어 있는지 확인.

**🟢 GREEN: Implement to Make Tests Pass**
- [ ] **Task 1.2**: `app/__init__.py` Talisman 설정 업데이트
  - File(s): `app/__init__.py`
  - Goal: CSP 정책에 Style/Script/Font 소스(CDN 도메인)를 화이트리스트로 추가.
  - Details:
    ```python
    csp = {
        'default-src': "'self'",
        'style-src': ["'self'", "cdn.jsdelivr.net", "fonts.googleapis.com"],
        'script-src': ["'self'", "cdn.jsdelivr.net", "use.fontawesome.com", "cdnjs.cloudflare.com"],
        'font-src': ["'self'", "fonts.gstatic.com", "use.fontawesome.com"],
        # ...
    }
    ```

**🔵 REFACTOR: Clean Up Code**
- [ ] **Task 1.3**: 설정 코드를 `config.py` 또는 별도 상수 파일로 분리 고려 (선택 사항).

#### Quality Gate ✋

**⚠️ STOP: Do NOT proceed to Phase 2 until ALL checks pass**

**TDD Compliance** (CRITICAL):
- [ ] **Red Phase**: Tests were written FIRST and initially failed
- [ ] **Green Phase**: Production code written to make tests pass
- [ ] **Refactor Phase**: Code improved while tests still pass

**Manual & Browser Testing**:
- [ ] **Agent Browser Verification**:
    - [ ] `browser_subagent` used to visit page(s)
    - [ ] Visual rendering confirmed (Console errors gone)
    - [ ] Screenshot captured for walkthrough

---

### Phase 2: Premium Design Integration
**Goal**: "Wow" 할 수 있는 세련된 Modern Web App 디자인 적용.
**Estimated Time**: 1.5 hours
**Status**: ⏳ Pending | 🔄 In Progress | ✅ Complete

#### Tasks

**🔴 RED: Write Failing Tests First**
- [ ] **Visual Check Pre-condition**: 현재 디자인이 "Premium" 기준에 미달함을 확인 (Task 2.1 수행 전 스크린샷).

**🟢 GREEN: Implement to Make Tests Pass**
- [ ] **Task 2.1**: `app/static/css/style.css` 전면 개편
  - File(s): `app/static/css/style.css`
  - Goal: HSL 변수, Glassmorphism, Gradient 적용.
  - Details:
    - Root Variables: Colors (Primary, Surface, Text), Spacing.
    - Global Reset & Typography (Google Fonts).
    - Components: `.card`, `.navbar`, `.btn-primary` (Gradient).
- [ ] **Task 2.2**: `app/templates/base.html`에 Google Fonts 링크 추가
- [ ] **Task 2.3**: `app/templates/main/index.html` 대시보드 구조 개선 (Card Grid)

**🔵 REFACTOR: Clean Up Code**
- [ ] **Task 2.4**: 불필요한 CSS 클래스 제거 및 주석 추가.

#### Quality Gate ✋

**⚠️ STOP: Do NOT proceed until ALL checks pass**

**Manual & Browser Testing**:
- [ ] **Agent Browser Verification**:
    - [ ] `browser_subagent` used to visit page(s)
    - [ ] Visual rendering confirmed:
        - [ ] Navbar Glass Effect
        - [ ] Soft Shadows on Cards
        - [ ] Proper Typography (Inter/Outfit)
    - [ ] Screenshot captured for walkthrough

---

## ⚠️ Risk Assessment

| Risk                     | Probability | Impact | Mitigation Strategy                                                                        |
| ------------------------ | ----------- | ------ | ------------------------------------------------------------------------------------------ |
| **CSP Misconfiguration** | Medium      | High   | `report_uri`나 브라우저 콘솔을 통해 차단되는 리소스를 정확히 파악하여 화이트리스트에 추가. |
| **CSS Override Issues**  | Low         | Medium | Bootstrap의 `!important` 등을 고려하여 CSS 우선순위(Specificity) 관리.                     |

---

## 🔄 Rollback Strategy

### If Phase 1 Fails
**Steps to revert**:
- `app/__init__.py`: Talisman 설정에서 `content_security_policy` 제거 (기본값 복귀) 또는 `force_https=False`로 변경.

### If Phase 2 Fails
**Steps to revert**:
- `git checkout -- app/static/css/style.css` (또는 이전 버전 내용 복원).
- `app/templates` 변경 사항 롤백.

---

## 📊 Progress Tracking

### Completion Status
- **Phase 1**: ⏳ 0% | 🔄 50% | ✅ 100%
- **Phase 2**: ⏳ 0% | 🔄 50% | ✅ 100%

**Overall Progress**: 100% complete

---

## 📝 Notes & Learnings

### Implementation Notes
- [Add insights discovered during implementation]

### Blockers Encountered
- **Blocker 1**: [Description] → [Resolution]

---

## ✅ Final Checklist

**Before marking plan as COMPLETE**:
- [ ] All phases completed with quality gates passed
- [ ] Full integration testing performed
- [ ] Documentation updated
- [ ] Security review completed
- [ ] Plan document archived for future reference

---
