# Flask Property Refactored 🏠

> **신입 개발자를 위한 온보딩 가이드가 포함된 부동산 추천 애플리케이션 리팩토링 프로젝트입니다.**
> 이 프로젝트는 레거시 코드를 **Clean Architecture**와 **TDD(Test-Driven Development)** 방법론을 적용하여 현대적으로 재구성했습니다.

---

## 📖 프로젝트 소개 (Introduction)

이 애플리케이션은 사용자의 위치와 예산에 맞는 **부동산(자치구/건물) 데이터를 분석하고 추천**해주는 서비스입니다.

### 핵심 기능
1.  **데이터 시각화**: 자치구별 변동률(Bar Chart)과 건물 용도별 평균 가격(Area Chart)을 시각적으로 제공합니다.
2.  **부동산 추천**: 사용자의 선호 위치에 기반한 맞춤형 부동산 예측 데이터를 테이블 형태로 보여줍니다.
3.  **사용자 관리**: 회원가입, 로그인, 로그아웃 등 안전한 인증 시스템을 갖추고 있습니다.

---

## 🏗️ 아키텍처 및 구조 (Architecture)

확장성과 유지보수를 위해 기능별로 모듈(Blueprint)을 분리했습니다.

### 디렉토리 구조
```plaintext
workspace_root/
├── app/                    # 📦 애플리케이션 핵심 로직
│   ├── __init__.py         # App Factory (앱 생성, 설정 로드, DB 연결)
│   ├── models.py           # 데이터베이스 모델 (User 등)
│   ├── utils.py            # 공통 유틸리티 (표준 API 응답 등)
│   ├── auth/               # [Blueprint] 인증 모듈 (로그인/가입)
│   └── main/               # [Blueprint] 메인 화면 및 데이터 API
├── tests/                  # 🧪 테스트 코드
│   ├── conftest.py         # 테스트 공통 설정 (Fixtures)
│   ├── unit/               # 단위 테스트 (모델, 유틸 등 개별 로직 검증)
│   └── integration/        # 통합 테스트 (API 엔드포인트 및 흐름 검증)
├── configs.py              # ⚙️ 환경별 설정 (Dev, Test, Prod)
├── migrations/             # 🗄️ DB 마이그레이션 스크립트
├── requirements.txt        # 📦 의존성 패키지 목록
└── README.md               # 📘 프로젝트 가이드
```

### 데이터 처리 흐름
1.  **Request**: 클라이언트(브라우저)가 요청을 보냅니다.
2.  **Route**: `app/main` 또는 `app/auth`의 뷰 함수가 요청을 받습니다.
3.  **Service/Model**: 필요한 데이터를 `models.py`에서 조회하거나 비즈니스 로직을 처리합니다.
4.  **Response**: `utils.py`의 표준 포맷(`success_response`)으로 JSON 또는 HTML을 반환합니다.

---

## 🚀 시작하기 (Getting Started)

개발 환경을 처음 세팅하는 신입 개발자를 위한 단계별 가이드입니다.

### 1. 사전 요구사항 (Prerequisites)
- **Python 3.8 이상**: 터미널에서 `python --version`으로 확인하세요.
- **Git**: 소스 코드 버전 관리 도구.

### 2. 설치 및 실행 (Setup & Run)

**Step 1. 프로젝트 클론 및 이동**
```bash
git clone <repository-url>
cd antigravity_workflows
```

**Step 2. 가상환경 생성 및 활성화**
독립적인 패키지 관리를 위해 가상환경을 사용합니다.
```bash
# Mac/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**Step 3. 의존성 설치**
```bash
pip install -r requirements.txt
```

**Step 4. 데이터베이스 초기화**
```bash
# 마이그레이션 정보를 바탕으로 DB 테이블 생성
flask db upgrade
```

**Step 5. 서버 실행**
```bash
flask run
```
브라우저에서 `http://127.0.0.1:5000`으로 접속하여 확인합니다.

### 3. 트러블슈팅 (Troubleshooting)
- **"Module not found" 에러**: 가상환경(`(venv)`)이 활성화되어 있는지 확인하고 `pip install -r requirements.txt`를 다시 실행하세요.
- **포트 충돌 ("Address already in use")**: 이미 다른 프로세스가 5000번 포트를 사용 중입니다. `flask run -p 5001`로 포트를 변경하세요.

---

## 🤝 협업 가이드 (Collaboration)

우리 팀은 **Git-Flow** 전략과 **Convetional Commits**를 따릅니다.

### 1. Git 브랜치 전략
- **`main`**: 언제든 배포 가능한 **안정 버전**. (직접 push 금지)
- **`develop`**: 개발 중인 기능이 모이는 **통합 브랜치**.
- **`feature/*`**: 개별 기능을 개발하는 브랜치.
    - **명명 규칙**: GitHub Issue 번호와 제목을 조합 (예: `feature/1-login-page`)

### 2. 커밋 메시지 규칙 (Conventional Commits)
커밋 메시지는 `타입: 제목` 형식을 따릅니다.

- **`feat`**: 새로운 기능 추가 (예: `feat: 회원가입 API 구현`)
- **`fix`**: 버그 수정
- **`docs`**: 문서 수정 (README, Docstring 등)
- **`refactor`**: 코드 리팩토링 (기능 변경 없음)
- **`test`**: 테스트 코드 추가/수정
- **`chore`**: 설정 변경, 패키지 매니저 등

---

## 📝 개발 컨벤션 (Development)

### 1. TDD 워크플로우 (Red-Green-Refactor)
1.  **Red**: 구현할 기능에 대한 **실패하는 테스트**를 먼저 작성합니다.
2.  **Green**: 테스트를 통과하기 위한 **최소한의 코드**를 작성합니다.
3.  **Refactor**: 중복을 제거하고 코드를 개선합니다. (테스트는 계속 통과해야 함)

```bash
# 전체 테스트 실행
make test
# 또는
pytest
```

### 2. 코드 및 문서 스타일
- **변수명/함수명**: 영문 `snake_case` 사용.
- **클래스명**: 영문 `PascalCase` 사용.
- **Docstring**: 모든 모듈, 클래스, 함수에는 **Google Style의 한국어 주석**을 필수로 작성합니다.

```python
def example_function(param):
    """함수에 대한 설명.

    Args:
        param (str): 파라미터 설명.

    Returns:
        bool: 반환값 설명.
    """
    pass
```

---

## 📚 참고 자료
- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [Flask-Login 공식 문서](https://flask-login.readthedocs.io/)
- [Pytest 공식 문서](https://docs.pytest.org/)
