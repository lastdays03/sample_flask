def test_request_id_header(client):
    """응답 헤더에 X-Request-ID가 포함되는지 테스트"""
    response = client.get("/")
    assert "X-Request-ID" in response.headers
    
def test_request_id_persistence(client):
    """요청 간 Request ID가 달라지는지 확인"""
    resp1 = client.get("/")
    resp2 = client.get("/")
    
    id1 = resp1.headers.get("X-Request-ID")
    id2 = resp2.headers.get("X-Request-ID")
    
    assert id1 is not None
    assert id2 is not None
    assert id1 != id2
