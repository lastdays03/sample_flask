def test_config_is_loaded(app):
    """앱 설정 로드 테스트.
    
    테스트 환경 설정이 올바르게 로드되었는지(TESTING=True, 인메모리 DB) 확인합니다.
    """
    assert app.config["TESTING"] is True
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"


def test_app_exists(app):
    """앱 인스턴스 존재 테스트.
    
    Flask 애플리케이션 인스턴스가 정상적으로 생성되었는지 확인합니다.
    """
    assert app is not None


def test_production_config_enforces_secret_key(monkeypatch):
    """ProductionConfig Secret Key 강제화 테스트.
    
    환경 변수에 SECRET_KEY가 없으면 ProductionConfig.init_app 호출 시
    ValueError가 발생하는지 확인합니다.
    """
    from config import ProductionConfig
    from flask import Flask
    
    app = Flask(__name__)
    
    # Ensure SECRET_KEY is unset
    monkeypatch.delenv("SECRET_KEY", raising=False)
    
    # Load config
    app.config.from_object(ProductionConfig)
    
    # init_app should raise ValueError because SECRET_KEY is missing/default
    import pytest
    with pytest.raises(ValueError, match="SECRET_KEY environment variable is required in production"):
        ProductionConfig.init_app(app)


def test_production_config_works_with_secret_key(monkeypatch):
    """ProductionConfig 정상 동작 테스트.
    
    환경 변수에 SECRET_KEY가 제공되면 init_app이 성공하고
    앱 설정에 올바르게 적용되는지 확인합니다.
    """
    from config import ProductionConfig
    from flask import Flask
    
    app = Flask(__name__)
    
    monkeypatch.setenv("SECRET_KEY", "super-secret-key")
    
    app.config.from_object(ProductionConfig)
    ProductionConfig.init_app(app)
    
    assert app.config["SECRET_KEY"] == "super-secret-key"



