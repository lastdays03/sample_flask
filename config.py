import os


class Config:
    """기본 설정 클래스.
    
    모든 환경에 공통으로 적용되는 기본 설정을 포함합니다.
    """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard-to-guess-string"
    WTF_CSRF_ENABLED = True  # CSRF 보호 명시적 활성화
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Documentation Settings (flask-smorest)
    API_TITLE = "Antigravity API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/api"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # Rate Limiting
    RATELIMIT_DEFAULT = "200 per day"
    RATELIMIT_STORAGE_URL = "memory://"
    RATELIMIT_HEADERS_ENABLED = True

    @staticmethod
    def init_app(app):
        """설정별 초기화 메서드.
        
        애플리케이션 생성 시 추가적인 설정 작업을 수행하기 위해
        하위 클래스에서 오버라이드할 수 있습니다.
        
        Args:
            app: Flask 애플리케이션 인스턴스.
        """
        pass


class DevelopmentConfig(Config):
    """개발 환경 설정 클래스.
    
    디버그 모드를 활성화하고 로컬 데이터베이스를 사용합니다.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or "sqlite:///local.sqlite"


class TestingConfig(Config):
    """테스트 환경 설정 클래스.
    
    테스트 모드를 활성화하고 인메모리 데이터베이스를 사용합니다.
    테스트 용이를 위해 CSRF 보호를 비활성화합니다.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """운영 환경 설정 클래스.
    
    운영 환경에 적합한 데이터베이스 설정을 사용하며,
    보안을 위해 SECRET_KEY 환경 변수 설정을 강제합니다.
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    @classmethod
    def init_app(cls, app):
        """운영 환경 초기화.
        
        SECRET_KEY가 환경 변수로 설정되어 있는지 확인합니다.
        
        Args:
            app: Flask 애플리케이션 인스턴스.
            
        Raises:
            ValueError: SECRET_KEY가 설정되지 않은 경우 발생.
        """
        Config.init_app(app)
        env_key = os.environ.get("SECRET_KEY")
        if not env_key:
            raise ValueError("SECRET_KEY environment variable is required in production")
        app.config["SECRET_KEY"] = env_key


    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///data.sqlite"



config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
