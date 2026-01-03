# Sample Flask 🧪

> **개발 워크플로우 학습 및 Agentic Coding 실험을 위한 Flask 샘플 프로젝트입니다.**
> 이 프로젝트는 단순한 애플리케이션 구현을 넘어, **일관된 개발 환경 구축, 자동화된 워크플로우, 그리고 AI Agent와의 협업**을 테스트하고 검증하는 데 목적이 있습니다.

---

## 📖 프로젝트 소개 (Introduction)

이 애플리케이션은 사용자 관리 및 기본적인 데이터 API 기능을 포함한 **표준 Flask 애플리케이션 템플릿**입니다. 실제 비즈니스 로직보다는 **견고한 프로젝트 구조와 개발 프로세스**에 초점을 맞추고 있습니다.

### 주요 기능 (Key Features)
1.  **사용자 관리**: 회원가입, 로그인, 로그아웃 (Flask-Login, Flask-WTF).
2.  **데이터 시각화 API**: 자치구별, 건물 용도별, 위치별 예측 데이터 제공 (Bar, Area, Table).
3.  **환경 표준화**: `Makefile`, `pyproject.toml` 등을 통한 팀 단위 개발 환경 통일.
4.  **자동화 워크플로우**: 테스트 자동화, 코드 품질 검사(Lint/Format) 등의 파이프라인 구축.

---

## 🏗️ 아키텍처 및 구조 (Architecture)

확장성과 유지보수를 위해 기능별로 모듈(Blueprint)을 분리했습니다. 상세한 아키텍처는 [Architecture Guide](docs/architecture.md)를 참고하세요.

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
├── configs.py              # ⚙️ 환경별 설정 (Dev, Test, Prod)
├── migrations/             # 🗄️ DB 마이그레이션 스크립트
├── requirements.txt        # 📦 의존성 패키지 목록
└── README.md               # 📘 프로젝트 가이드
```

### API 요약 (API Summary)
상세 명세는 [API Reference](docs/api_reference.md)를 참고하세요.

| 모듈 | 메소드 | 엔드포인트 | 설명 |
|---|---|---|---|
| **Auth** | POST | `/auth/login` | 사용자 로그인 및 세션 생성 |
| **Auth** | POST | `/auth/register` | 신규 사용자 등록 |
| **Auth** | GET | `/auth/logout` | 로그아웃 및 세션 종료 |
| **Main** | POST | `/district` | 자치구별 변동률 데이터 조회 |
| **Main** | POST | `/building` | 건물 용도별 평균 가격 조회 |
| **Main** | POST | `/predict/location` | 위치별 예측 상세 데이터 조회 |

### 데이터 처리 흐름
1.  **Request**: 클라이언트(브라우저)가 요청을 보냅니다.
2.  **Route**: `app/main` 또는 `app/auth`의 뷰 함수가 요청을 받습니다.
3.  **Service/Model**: 필요한 데이터를 `models.py`에서 조회하거나 비즈니스 로직을 처리합니다.
4.  **Response**: `utils.py`의 표준 포맷(`success_response`)으로 JSON 또는 HTML을 반환합니다.

---

## ⚙️ 프로젝트 도구 및 설정 (Project Tools)

개발 환경 표준화와 생산성 향상을 위해 사용되는 주요 설정 파일들에 대한 설명입니다. 이 파일들은 모든 개발자가 동일한 환경에서 작업할 수 있도록 Git에 포함되어 관리됩니다.

### 1. `Makefile` (명령어 단축키)
복잡한 터미널 명령어들을 간단한 단축키(매크로)로 실행할 수 있도록 정의한 파일입니다. 개발자는 긴 명령어를 외울 필요가 없습니다.

- **`make test`**: 전체 테스트를 실행합니다. (`python -m pytest`)
- **`make lint`**: 코드 스타일을 검사합니다. (`flake8 .`)
- **`make format`**: 코드를 자동으로 포매팅합니다. (`black .`)
- **`make coverage`**: 테스트 커버리지를 측정하고 리포트를 출력합니다.
- **`make all`**: 포매팅, 린팅, 커버리지 측정을 한 번에 수행합니다.

### 2. `.flake8` (스타일 가이드)
Python 코드의 스타일 규칙을 정의하는 설정 파일입니다. 팀원 간의 코드 일관성을 유지하기 위해 사용됩니다.
- **주요 역할**: 문법 오류 체크, PEP8 스타일 준수 여부 확인, 사용하지 않는 변수 감지 등.
- **설정 공유**: 프로젝트 루트에 포함되어 모든 개발자가 동일한 규칙을 적용받습니다.

### 3. `pyproject.toml` (빌드 및 도구 설정)
Python 프로젝트의 표준 설정 파일로, 빌드 시스템과 다양한 개발 도구의 설정을 통합 관리합니다.
- **Black 설정**: 코드 포매터인 Black의 설정을 정의합니다.
    - `line-length = 120`: 한 줄의 최대 길이를 120자로 제한합니다. (기존 88자보다 여유롭게 설정)
    - `target-version = ['py38']`: Python 3.8 버전을 기준으로 코드를 변환합니다.

### 4. `app/config.py` (환경 설정)
애플리케이션 실행 환경(개발, 테스트, 운영)에 따른 설정을 파이썬 클래스 형태로 관리합니다.

- **`Config`**: 모든 환경의 공통 설정 (기본 Secret Key 등).
- **`DevelopmentConfig`**: 개발용 (Debug 모드 활성화, 로컬 SQLite 사용).
- **`TestingConfig`**: 테스트용 (인메모리 DB 사용, CSRF 비활성화).
- **`ProductionConfig`**: 운영용 (환경변수 강제, 보안 설정 강화).

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
