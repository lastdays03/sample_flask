import logging


def test_login_failure_exception_handling(client, app):
    """로그인 실패 예외 처리 테스트.
    
    잘못된 정보로 로그인 시도 시 BusinessException이 발생하고,
    적절한 에러 응답(400)을 반환하는지 확인합니다.
    """

    # JSON 요청을 통해 BusinessException 유발
    response = client.post(
        "/auth/login",
        data='{"email": "wrong@example.com", "password": "wrongpassword"}',
        content_type="application/json"
    )

    # JSON 요청에 대해 표준 에러 래퍼를 기대함
    # 현재 HTML이나 비표준 JSON이 반환될 경우 이 테스트는 실패함 (Red)
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "Invalid email or password" in data["message"]
    # assert data["payload"] is None or isinstance(data["payload"], dict)


def test_login_failure_logging(client, caplog):
    """로그인 실패 로깅 테스트.
    
    로그인 실패 시 예외 상황이 로그에 기록되는지 확인합니다.
    """
    with caplog.at_level(logging.ERROR):
        client.post(
            "/auth/login", data={"email": "wrong@example.com", "password": "wrongpassword"}, follow_redirects=True
        )

        assert "CoreException caught: Invalid email or password." in caplog.text

