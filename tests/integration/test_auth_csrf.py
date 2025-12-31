def test_duplicate_registration(client, app):
    """중복 회원가입 테스트.
    
    이미 등록된 이메일로 가입 시도 시 BusinessException(400)이 
    발생하는지 확인합니다.
    """
    # 첫 번째 회원가입
    client.post(
        "/auth/register",
        data={"email": "dup@example.com", "username": "user1", "password": "pass", "confirm_password": "pass"},
        follow_redirects=True,
    )

    # 두 번째 회원가입 (중복 시도)
    response = client.post(
        "/auth/register",
        data={"email": "dup@example.com", "username": "user2", "password": "pass", "confirm_password": "pass"},
        follow_redirects=True,
    )
    # 전역 에러 핸들러가 BusinessException에 대해 400을 반환함
    assert response.status_code == 400
    assert b"Email already registered" in response.data


def test_csrf_protection_enabled(app, client):
    """CSRF 보호 기능 테스트.
    
    CSRF 설정이 활성화된 상태에서 토큰 없이 요청을 보낼 때
    400 에러 및 CSRF 관련 에러 메시지가 반환되는지 확인합니다.
    """
    # 일시적으로 CSRF 활성화
    app.config["WTF_CSRF_ENABLED"] = True

    # CSRF 토큰 없이 로그인 시도 (AJAX 시뮬레이션)
    response = client.post(
        "/auth/login",
        data='{"email": "test@example.com", "password": "pass"}',
        content_type="application/json"
    )

    assert response.status_code == 400  # CSRF 위반 시 400 반환 예상
    data = response.get_json()
    assert data["status"] == "error"
    # The message is generic "Validation Error", details are in payload
    assert "Validation Error" in data["message"]
    # Check payload for csrf_token error
    assert "csrf_token" in data["payload"]
    assert "CSRF" in data["payload"]["csrf_token"][0] or "Token" in data["payload"]["csrf_token"][0]


    # Revert config
    app.config["WTF_CSRF_ENABLED"] = False
