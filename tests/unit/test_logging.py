import pytest
from app import create_app


def test_logging_configuration():
    """로깅 설정 테스트.
    
    애플리케이션 로거가 핸들러를 포함하여 올바르게 설정되었는지 확인합니다.
    """
    app = create_app("testing")
    logger = app.logger

    # 핸들러 부착 여부 확인
    assert logger.hasHandlers()

    # 테스트 환경에서는 설정에 따라 파일 핸들러가 없을 수도 있지만,
    # 기본 설정은 있어야 함.
    # 에러 없이 로그가 남는지 검증.
    try:
        logger.info("Test Info Log")
        logger.error("Test Error Log")
    except Exception as e:
        pytest.fail(f"Logging raised exception: {e}")
