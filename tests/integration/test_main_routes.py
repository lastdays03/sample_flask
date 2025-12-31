def test_dashboard_access(client):
    """대시보드 접근성 테스트.
    
    메인 페이지('/')가 정상적으로 로드되고, 인덱스 템플릿과 
    차트 캔버스 요소들을 렌더링하는지 확인합니다.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Dashboard" in response.data
    assert b"SMART LOCATION RECOMMENDER" in response.data
    # 대시보드 콘텐츠가 로드되는지 확인하기 위해 캔버스 요소 검사
    assert b'<canvas id="myAreaChart"' in response.data
    assert b'<canvas id="myBarChart"' in response.data


def test_main_api_endpoints(client):
    """메인 API 엔드포인트 테스트.
    
    자치구(District), 건물(Building), 예측(Prediction) 데이터 API가
    올바른 JSON 구조와 데이터를 반환하는지 검증합니다.
    """

    # 자치구(District) 데이터 테스트
    response = client.post("/district")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    assert "district_name" in data["data"][0]

    # 건물(Building) 데이터 테스트
    response = client.post("/building")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    assert "building_use" in data["data"][0]

    # 위치 예측(Location Prediction) 데이터 테스트
    response = client.post("/predict/location")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    assert "legal_dong_name" in data["data"][0]


def test_api_method_not_allowed(client):
    """API 메서드 허용 확인 테스트.
    
    API 엔드포인트가 GET 요청을 거부하고 405 Method Not Allowed를
    반환하는지 확인합니다.
    """
    response = client.get("/district")
    assert response.status_code == 405

