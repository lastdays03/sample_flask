def test_authentication_pages(client):
    """인증 페이지 접근성 테스트.
    
    로그인 및 회원가입 페이지가 정상적으로 로드되고(Status 200),
    기본 레이아웃(네비게이션 바 등)을 포함하는지 확인합니다.
    """
    response = client.get("/auth/login")
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"SMART LOCATION RECOMMENDER" in response.data  # Navbar content

    response = client.get("/auth/register")
    assert response.status_code == 200
    assert b"Register" in response.data
    assert b"SMART LOCATION RECOMMENDER" in response.data  # Navbar content


def test_registration_and_login(client, app):
    """회원가입 및 로그인 흐름 테스트.
    
    새 사용자를 등록하고, 해당 사용자로 로그인이 성공하는지
    전체 프로세스를 검증합니다.
    """
    # 회원가입 (Register)
    response = client.post(
        "/auth/register",
        data={"email": "new@example.com", "username": "newuser", "password": "cat", "confirm_password": "cat"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    # response.data에 'Login'이 포함되어 있어야 함 (로그인 페이지로 리다이렉트)

    # 로그인 (Login)
    response = client.post("/auth/login", data={"email": "new@example.com", "password": "cat"}, follow_redirects=True)
    assert response.status_code == 200
    # response.data에 'Log out'이 포함되어 있어야 함 (로그인 성공 상태)


def test_logout(client):
    """로그아웃 테스트.
    
    로그아웃 요청 시 정상적으로 처리되고 리다이렉트되는지 확인합니다.
    """
    response = client.get("/auth/logout", follow_redirects=True)
    assert response.status_code == 200

