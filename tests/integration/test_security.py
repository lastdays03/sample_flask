def test_security_headers(client):
    """보안 헤더 존재 여부 테스트"""
    response = client.get("/")
    
    # HSTS (Production only or forced)
    # 개발 환경이라도 Talisman 기본 설정이면 헤더가 붙을 수 있음.
    # 단, force_https=True가 기본이므로 로컬 테스트 시 302 리다이렉트가 발생하거나
    # content_security_policy 헤더가 있어야 함.
    
    assert "Content-Security-Policy" in response.headers
    assert "X-Content-Type-Options" in response.headers
    assert "X-Frame-Options" in response.headers
