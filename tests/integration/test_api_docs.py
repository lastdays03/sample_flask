def test_swagger_ui_access(client):
    """Swagger UI 엔드포인트 접근 테스트"""
    response = client.get("/api/docs")
    # 초기에는 설정되지 않았으므로 404가 예상되지만, 
    # TDD Red 단계에서는 '접속 성공(200)'을 기대하는 테스트를 작성하고
    # 실제 실행 시 404로 실패함을 확인합니다.
    assert response.status_code == 200
    assert b"SwaggerUIBundle" in response.data

def test_openapi_spec_access(client):
    """OpenAPI 스펙 JSON 접근 테스트"""
    response = client.get("/api/openapi.json")
    assert response.status_code == 200
    assert response.is_json
