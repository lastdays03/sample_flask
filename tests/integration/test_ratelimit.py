import time

def test_rate_limiting(client):
    """Rate Limit 동작 테스트"""
    # 임계치를 매우 낮게 설정한 엔드포인트가 필요하거나 전역 설정 테스트
    # 여기서는 전역 설정이 적용되지 않은 상태에서 테스트하므로 실패해야 함 (Red)
    # 실제 구현 후에는 config에서 RATELIMIT_DEFAULT = "100 per day" 등으로 설정될 예정
    
    # 429 확인을 위해서는 특정 엔드포인트를 반복 호출
    # 구현 전에는 제한이 없으므로 루프를 돌아도 200 OK
    
    # 이 테스트는 Talisman/Limiter 미적용 시에는 통과(제한 없음)하므로
    # '제한이 걸려야 한다'는 조건으로 작성.
    
    # 하지만 기본 설정(200 per day)으로는 테스트가 오래 걸리므로
    # RateLimit 전용 Mock 헤더나 설정이 필요함.
    # 여기서는 "Limiter가 적용된 상태"인지를 확인하는 헤더 검사로 대체 가능?
    # Flask-Limiter는 X-RateLimit-Limit 헤더를 내려줌.
    
    response = client.get("/")
    # 아직 Limiter 미적용 상태 -> 헤더 없음 -> Assert Fail
    assert "X-RateLimit-Limit" in response.headers
