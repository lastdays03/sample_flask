from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config_name="default"):
    """Flask 애플리케이션 팩토리 함수.
    
    지정된 설정 이름을 기반으로 Flask 애플리케이션을 생성하고 초기화합니다.
    데이터베이스, 마이그레이션, 로그인 매니저 및 로깅 설정을 수행하고
    블루프린트를 등록합니다.

    Args:
        config_name (str): 적용할 설정 구성의 이름 (기본값: "default").

    Returns:
        Flask: 설정이 완료된 Flask 애플리케이션 인스턴스.
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # 로깅 설정
    from app.utils.logging import RequestIDMiddleware, RequestIdFilter
    from pythonjsonlogger import jsonlogger  # Legacy import for compatibility with some versions, or use jsonlogger directly
    import logging
    import sys
    from logging.handlers import RotatingFileHandler
    import os

    # Request ID Middleware 적용
    RequestIDMiddleware(app)

    if not app.debug and not app.testing:
        if not os.path.exists("logs"):
            os.mkdir("logs")
            
        file_handler = RotatingFileHandler("logs/antigravity.log", maxBytes=10240, backupCount=10)
        
        # Production 환경 등에서 JSON 로깅 적용 (config_name 기반 판단 또는 별도 플래그)
        # 여기서는 app.config['ENV'] 나 config_name 인자를 활용할 수 있으나, 
        # 직관적으로 flask config에 'LOG_FORMAT'을 추가하는 것이 좋음.
        # 일단 production 모드일 때 (debug=False, testing=False) 기본 적용하되,
        # 기존 텍스트 포맷과 구분을 위해 포맷터 교체
        
        # Request ID Filter 적용
        file_handler.addFilter(RequestIdFilter())
        
        if config_name == "production":
             # JSON Formatter
            formatter = jsonlogger.JsonFormatter(
                "%(asctime)s %(levelname)s %(request_id)s %(message)s %(pathname)s %(lineno)d"
            )
            file_handler.setFormatter(formatter)
        else:
            # Text Formatter (with request_id)
            formatter = logging.Formatter(
                "%(asctime)s %(levelname)s [%(request_id)s] %(message)s [in %(pathname)s:%(lineno)d]"
            )
            file_handler.setFormatter(formatter)

        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info("Antigravity startup")

    # 개발/테스트 환경에서도 로그가 콘솔에 출력되도록 보장합니다
    # (Flask 기본 설정이 이를 처리하지만, 필요시 명시적으로 설정 가능)
    # 현재는 운영 환경 유사 모드에서의 파일 로깅이 핵심입니다.

    from app import models

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .errors import errors as errors_blueprint

    app.register_blueprint(errors_blueprint)

    # API 설정 (flask-smorest)
    from flask_smorest import Api
    api = Api(app)
    
    
    from app.api.example import api_bp as example_api_blueprint
    api.register_blueprint(example_api_blueprint)
    
    from app.api.health import blp as health_blp
    api.register_blueprint(health_blp)

    # 보안 설정 (Flask-Talisman)
    from flask_talisman import Talisman
    
    csp = {
        'default-src': "'self'",
        'style-src': ["'self'", "'unsafe-inline'", "cdn.jsdelivr.net", "fonts.googleapis.com"],
        'script-src': ["'self'", "'unsafe-inline'", "cdn.jsdelivr.net", "use.fontawesome.com", "cdnjs.cloudflare.com"],
        'font-src': ["'self'", "fonts.gstatic.com", "use.fontawesome.com"],
        'img-src': ["'self'", "data:"]
    }
    
    Talisman(app, force_https=not (app.testing or app.debug), content_security_policy=csp)

    # Rate Limiting (Flask-Limiter)
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=[app.config.get("RATELIMIT_DEFAULT", "200 per day")],
        storage_uri=app.config.get("RATELIMIT_STORAGE_URL", "memory://")
    )

    return app
