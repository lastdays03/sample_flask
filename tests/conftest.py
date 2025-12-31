import pytest
from app import create_app, db


@pytest.fixture
def app():
    """테스트용 Flask 애플리케이션 픽스처.
    
    테스트 설정으로 앱을 생성하고, 데이터베이스를 설정/해제합니다.
    테스트가 진행되는 동안 애플리케이션 컨텍스트를 유지합니다.
    
    Yields:
        Flask: 설정된 Flask 애플리케이션 인스턴스.
    """
    app = create_app("testing")

    # 애플리케이션 컨텍스트 생성

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """테스트용 클라이언트 픽스처.
    
    HTTP 요청을 시뮬레이션할 수 있는 클라이언트를 반환합니다.
    
    Args:
        app: 'app' 픽스처.
        
    Returns:
        FlaskClient: 테스트 클라이언트.
    """
    return app.test_client()


@pytest.fixture
def runner(app):
    """테스트용 CLI 러너 픽스처.
    
    Click CLI 명령을 시뮬레이션할 수 있는 러너를 반환합니다.
    
    Args:
        app: 'app' 픽스처.
        
    Returns:
        FlaskCliRunner: 테스트 CLI 러너.
    """
    return app.test_cli_runner()

