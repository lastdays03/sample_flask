def test_security_headers(client):
    """보안 헤더 존재 여부 및 CSP 설정 테스트"""
    response = client.get("/")
    
    # 1. 필수 보안 헤더 존재 여부 확인
    assert "Content-Security-Policy" in response.headers
    assert "X-Content-Type-Options" in response.headers
    assert "X-Frame-Options" in response.headers

    # 2. CSP 세부 정책 확인 (CDN 허용 여부)
    csp = response.headers["Content-Security-Policy"]
    
    # Bootstrap & External CSS
    assert "cdn.jsdelivr.net" in csp
    assert "fonts.googleapis.com" in csp
    
    # External Scripts
    assert "use.fontawesome.com" in csp
    assert "cdnjs.cloudflare.com" in csp
    
    # External Fonts
    assert "fonts.gstatic.com" in csp
