def test_health_check(client):
    """Health check endpoint verification"""
    response = client.get("/health")
    
    # Expecting 200 OK
    assert response.status_code == 200
    
    # Expecting specific JSON structure
    data = response.get_json()
    assert data["status"] == "ok"
    assert "version" in data
