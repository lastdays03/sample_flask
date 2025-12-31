# Backlog: 상용화 대비 기술 부채 및 개선 목록

## 1. 보안 (Security) 🛡️

- [ ] **Security Headers 적용**: `Flask-Talisman` 도입하여 HTTPS 강제(HSTS), CSP, X-Frame-Options 등 보안 헤더 설정.
- [ ] **Rate Limiting**: `Flask-Limiter` 도입하여 API 무차별 대입 공격 방지 (특히 로그인/회원가입).
- [ ] **Password Policy**: 비밀번호 복잡도 검사(길이, 특수문자 등) 추가.

## 2. 확장성 및 성능 (Scalability & Performance) 🚀
- [ ] **Real Database Migration**: SQLite를 PostgreSQL 또는 MySQL로 전환. `docker-compose`에 DB 서비스 추가.
- [ ] **Caching Layer**: Redis 도입. `Flask-Caching`을 사용하여 자주 조회되는 API 캐싱 및 세션 저장소로 활용.
- [ ] **Application Server**: `Gunicorn` 또는 `uWSGI` 설정 추가 및 `Dockerfile` 최적화 (Multi-stage build).
- [ ] **Async Task Queue**: 이메일 발송, 예측 모델 실행 등 무거운 작업 처리를 위한 `Celery` + `RabbitMQ/Redis` 도입.

## 3. 관측 가능성 (Observability) 👁️
- [ ] **Error Tracking**: `Sentry` 연동하여 런타임 에러 자동 수집 및 알림 구성.
- [ ] **Metrics & Monitoring**: `/metrics` 엔드포인트 구현 (Prometheus 호환) 및 Grafana 대시보드 구성.
- [ ] **Health Check**: L4/L7 로드밸런서 연동을 위한 `/health` 엔드포인트 표준화.

## 4. 핵심 기능 (Core Features) 🧩
- [ ] **Real Data Integration**: `app/main/mock_data.py`를 실제 DB 모델(`RealEstateData`)과 쿼리로 교체.
- [ ] **User Management**:
  - 비밀번호 재설정 (Email 발송)
  - 프로필 수정 (이름, 비밀번호 변경)
  - 회원 탈퇴
- [ ] **Admin Dashboard**: 사용자 관리 및 데이터 통계 확인을 위한 관리자 페이지(`Flask-Admin`).

## 5. DevOps & CI/CD 🛠️
- [ ] **CI Pipeline**: GitHub Actions 워크플로우 작성 (Lint, Test, Build).
- [ ] **Environment Separation**: Prod/Stage/Dev 환경별 설정 및 배포 전략 수립.
